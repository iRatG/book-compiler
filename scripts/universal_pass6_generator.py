#!/usr/bin/env python3
"""
Pass 6: Universal JSON Generator for LLM

Generates 05_llm_instructions.json for EACH book independently.
One JSON per book. Same universal algorithm, unique output per book.

Usage:
    python universal_pass6_generator.py Books/
    → Generates 05_llm_instructions.json for each book

    python universal_pass6_generator.py Books/clean-architecture/
    → Generates JSON for single book only
"""

import json
import re
from pathlib import Path
from typing import Dict, List, Set, Optional, Tuple
from datetime import datetime


class Pass6UniversalGenerator:
    """Pass 6: Transform markdown to JSON for LLM (per book)."""

    def __init__(self, book_dir: Path):
        self.book_dir = Path(book_dir)
        self.book_name = book_dir.name

        # Load markdown layers
        self.layers = {}
        self._load_layers()

        # Extract data
        self.metadata = self._extract_metadata()
        self.principles = self._extract_principles()
        self.arguments = self._extract_arguments()
        self.implications = self._extract_implications()
        self.questions = self._extract_questions()
        self.global_tags = self._extract_tags()

        # Link internally
        self.links = self._build_internal_links()

    def _load_layers(self):
        """Load markdown files (00-04)."""
        for i in range(5):
            pattern = f"{i:02d}_*.md"
            files = list(self.book_dir.glob(pattern))
            if not files:
                raise FileNotFoundError(f"Layer {i} file not found: {self.book_dir}")
            self.layers[i] = files[0].read_text(encoding='utf-8')

    def _extract_metadata(self) -> Dict:
        """Extract from 00_purpose.md."""
        content = self.layers[0]
        metadata = {}

        # Parse basic fields
        patterns = {
            'title': r'\*\*(?:Book|Title):\*\*\s+(.+)',
            'author': r'\*\*Author:\*\*\s+(.+)',
            'publication': r'\*\*Publication:\*\*\s+(.+)'
        }

        for key, pattern in patterns.items():
            match = re.search(pattern, content)
            if match:
                metadata[key] = match.group(1).strip()

        return metadata

    def _extract_principles(self) -> List[Dict]:
        """Extract main principles only (not subsections)."""
        content = self.layers[2]

        # Match ## PRINCIPLE N: or similar
        pattern = r'##\s+(?:PRINCIPLE|IDEA|RULE)\s+(\d+)[:\s]+(.+?)(?=\n|$)'
        matches = list(re.finditer(pattern, content))

        principles = []
        for i, match in enumerate(matches):
            p_num = int(match.group(1))
            p_name = match.group(2).strip()

            # Get content until next principle
            start = match.end()
            end = matches[i + 1].start() if i + 1 < len(matches) else len(content)
            p_content = content[start:end]

            # Extract statement
            statement = self._extract_first_paragraph(p_content)

            # Extract tags from this section
            tags = re.findall(r'#(\w+[\w-]*)', p_content)

            principle = {
                'id': f'principle_{p_num}',
                'number': p_num,
                'principle': p_name,
                'statement': statement,
                'tags': list(set(tags)),  # unique
                'source': f"02_ideas.md: PRINCIPLE {p_num}",
                'source_line': content[:match.start()].count('\n') + 1
            }
            principles.append(principle)

        return principles

    def _extract_arguments(self) -> List[Dict]:
        """Extract arguments/reasoning from 03_reasoning.md."""
        content = self.layers[3]

        pattern = r'##\s+(?:ARG-?|ARGUMENT|REASONING)\s*(\d+)[:\s]+(.+?)(?=\n|$)'
        matches = list(re.finditer(pattern, content, re.IGNORECASE))

        arguments = []
        for i, match in enumerate(matches):
            arg_num = int(match.group(1))
            arg_name = match.group(2).strip()

            start = match.end()
            end = matches[i + 1].start() if i + 1 < len(matches) else len(content)
            arg_content = content[start:end]

            # Extract first paragraph as claim
            claim = self._extract_first_paragraph(arg_content)

            # Extract tags
            tags = re.findall(r'#(\w+[\w-]*)', arg_content)

            argument = {
                'id': f'arg_{arg_num:03d}',
                'number': arg_num,
                'name': arg_name,
                'claim': claim,
                'tags': list(set(tags)),
                'source': f"03_reasoning.md: Argument {arg_num}",
                'source_line': content[:match.start()].count('\n') + 1
            }
            arguments.append(argument)

        return arguments

    def _extract_implications(self) -> List[Dict]:
        """Extract implications/applications from 04_consequences.md."""
        content = self.layers[4]

        pattern = r'##\s+(?:IMPLICATION|APPLICATION|CONSEQUENCE)\s*(\d+)[:\s]+(.+?)(?=\n|$)'
        matches = list(re.finditer(pattern, content, re.IGNORECASE))

        implications = []
        for i, match in enumerate(matches):
            impl_num = int(match.group(1))
            impl_name = match.group(2).strip()

            start = match.end()
            end = matches[i + 1].start() if i + 1 < len(matches) else len(content)
            impl_content = content[start:end]

            # Extract what means, practical adoption
            what_means = self._extract_section(impl_content, ['What', 'Means', 'Description'])
            practical = self._extract_section(impl_content, ['Practical', 'Adoption', 'Implementation'])

            tags = re.findall(r'#(\w+[\w-]*)', impl_content)

            implication = {
                'id': f'impl_{impl_num:03d}',
                'number': impl_num,
                'name': impl_name,
                'what_means': what_means,
                'practical_adoption': practical,
                'tags': list(set(tags)),
                'source': f"04_consequences.md: Implication {impl_num}",
                'source_line': content[:match.start()].count('\n') + 1
            }
            implications.append(implication)

        return implications

    def _extract_questions(self) -> List[Dict]:
        """Extract questions from 01_questions.md."""
        content = self.layers[1]

        pattern = r'#{2,4}\s+(?:QUESTION|Q)\s*(\d+)[:\s]+(.+?)(?=\n|$)'
        matches = list(re.finditer(pattern, content, re.IGNORECASE))

        questions = []
        for i, match in enumerate(matches):
            q_num = int(match.group(1))
            q_text = match.group(2).strip()

            start = match.end()
            end = matches[i + 1].start() if i + 1 < len(matches) else len(content)
            q_content = content[start:end]

            tags = re.findall(r'#(\w+[\w-]*)', q_content)

            question = {
                'id': f'question_{q_num:02d}',
                'number': q_num,
                'text': q_text,
                'tags': list(set(tags)),
                'source': f"01_questions.md: Question {q_num}",
                'source_line': content[:match.start()].count('\n') + 1
            }
            questions.append(question)

        return questions

    def _extract_tags(self) -> Set[str]:
        """Extract all unique tags from all layers."""
        all_tags = set()
        for i in range(5):
            tags = re.findall(r'#(\w+[\w-]*)', self.layers[i])
            all_tags.update(tags)
        return all_tags

    def _build_internal_links(self) -> Dict:
        """Link principles ↔ arguments ↔ implications (book-internal only)."""
        links = {}

        for principle in self.principles:
            p_id = principle['id']
            p_tags = set(principle['tags'])
            links[p_id] = {
                'principle': principle,
                'supporting_arguments': [],
                'related_implications': [],
                'related_questions': []
            }

            # Link arguments (same book only)
            for arg in self.arguments:
                if self._tags_match(p_tags, set(arg['tags'])):
                    links[p_id]['supporting_arguments'].append(arg)

            # Link implications (same book only)
            for impl in self.implications:
                if self._tags_match(p_tags, set(impl['tags'])):
                    links[p_id]['related_implications'].append(impl)

            # Link questions (same book only)
            for q in self.questions:
                if self._tags_match(p_tags, set(q['tags'])):
                    links[p_id]['related_questions'].append(q)

        return links

    def _tags_match(self, tags1: Set[str], tags2: Set[str]) -> bool:
        """Check if tags match (exact or semantic)."""
        # Exact match
        if tags1 & tags2:
            return True

        # Semantic match (shared words)
        words1 = set()
        for tag in tags1:
            words1.update(tag.split('-'))

        words2 = set()
        for tag in tags2:
            words2.update(tag.split('-'))

        overlap = words1 & words2
        if overlap and len(overlap) / min(len(words1), len(words2)) > 0.3:
            return True

        return False

    def generate(self) -> Dict:
        """Generate complete JSON structure."""
        return {
            'metadata': self._metadata_section(),
            'system_instruction': self._system_instruction_section(),
            'quick_reference': self._quick_reference_section(),
            'principles': [self._principle_object(p_id) for p_id in self.links.keys()],
            'decision_guide': self._decision_guide_section(),
            'faq': self._faq_section(),
            'tags': sorted(list(self.global_tags)),
            'version_info': self._version_info_section()
        }

    def _metadata_section(self) -> Dict:
        return {
            'title': self.metadata.get('title', 'Unknown'),
            'author': self.metadata.get('author', 'Unknown'),
            'publication': self.metadata.get('publication', 'Unknown'),
            'book_name': self.book_name,
            'format_version': '3.0',
            'generated_at': datetime.now().isoformat(),
            'language': 'English',
            'generation_pass': 'Pass 6: JSON Generation for LLM'
        }

    def _system_instruction_section(self) -> str:
        return (
            f"You are applying {self.metadata.get('title', 'this book')}'s principles to real work.\n\n"
            "**How to use this JSON:**\n"
            "1. Identify which principle applies\n"
            "2. Review supporting_arguments for evidence\n"
            "3. Check related_implications for practical application\n"
            "4. Use code_review_checklist items\n"
            "5. Apply practical_metrics to measure\n\n"
            "**RULES:**\n"
            "- Only cite what's in this JSON\n"
            "- Quote supporting_arguments\n"
            "- Use checklist items verbatim\n"
            "- If principle doesn't apply, say so\n\n"
            "Everything here is sourced from the book. Nothing is invented."
        )

    def _quick_reference_section(self) -> Dict:
        top_3 = [p['principle'] for p in self.principles[:3]]
        return {
            'book': self.book_name,
            'principles_count': len(self.principles),
            'top_3_principles': top_3,
            'questions_count': len(self.questions),
            'arguments_count': len(self.arguments),
            'implications_count': len(self.implications)
        }

    def _principle_object(self, p_id: str) -> Dict:
        """Generate principle with internal links only."""
        link = self.links[p_id]
        principle = link['principle']

        return {
            'id': principle['id'],
            'number': principle['number'],
            'principle': principle['principle'],
            'statement': principle['statement'],
            'tags': principle['tags'],
            'source': principle['source'],
            'source_line': principle['source_line'],

            'supporting_arguments': [
                {
                    'id': arg['id'],
                    'name': arg['name'],
                    'claim': arg['claim'][:150] if arg['claim'] else '',
                    'source': arg['source']
                }
                for arg in link['supporting_arguments']
            ],

            'related_implications': [
                {
                    'id': impl['id'],
                    'name': impl['name'],
                    'what_means': impl.get('what_means', '')[:100] if impl.get('what_means') else '',
                    'source': impl['source']
                }
                for impl in link['related_implications']
            ],

            'related_questions': [
                {
                    'id': q['id'],
                    'text': q['text'],
                    'source': q['source']
                }
                for q in link['related_questions']
            ]
        }

    def _decision_guide_section(self) -> Dict:
        return {
            'when_uncertain_ask': [q['text'] for q in self.questions[:5]],
            'framework': 'Reference supporting_arguments and related_implications'
        }

    def _faq_section(self) -> List[Dict]:
        return [
            {
                'question': 'How do I know this principle applies?',
                'answer': 'Check if your situation matches when_to_use context. Review related_questions.',
                'principle_refs': [p['id'] for p in self.principles[:2]]
            }
        ]

    def _version_info_section(self) -> Dict:
        return {
            'json_version': '3.0',
            'pass': 'Pass 6: JSON Generation for LLM',
            'generation_date': datetime.now().isoformat(),
            'book': self.book_name,
            'principles': len(self.principles),
            'arguments': len(self.arguments),
            'implications': len(self.implications),
            'questions': len(self.questions),
            'tags': len(self.global_tags),
            'data_quality': 'No invented data. All sourced from markdown.'
        }

    def _extract_first_paragraph(self, text: str) -> str:
        """Extract first paragraph from text."""
        para = text.split('\n\n')[0]
        return para.strip()

    def _extract_section(self, text: str, headers: List[str]) -> str:
        """Extract section after header."""
        for header in headers:
            pattern = rf'{re.escape(header)}[:\s]+(.+?)(?=\n\n|###|$)'
            match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)
            if match:
                return match.group(1).strip()[:200]
        return ''


def process_book(book_dir: Path, verbose: bool = False) -> Tuple[bool, str]:
    """Process single book, generate JSON."""
    try:
        if verbose:
            print(f"Processing: {book_dir.name}")

        generator = Pass6UniversalGenerator(book_dir)
        json_data = generator.generate()

        # Save
        output_file = book_dir / '05_llm_instructions.json'
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(json_data, f, indent=2, ensure_ascii=False)

        stats = {
            'principles': len(json_data['principles']),
            'arguments': generator.metadata.get('arguments_count', 0),
            'tags': len(json_data['tags'])
        }

        return True, f"[OK] {book_dir.name}: {stats['principles']} principles"

    except Exception as e:
        return False, f"[ERROR] {book_dir.name}: {str(e)}"


def find_book_directories(root_dir: Path) -> List[Path]:
    """Find all book directories with markdown files."""
    books = []
    for item in root_dir.iterdir():
        if item.is_dir() and (item / "00_purpose.md").exists():
            books.append(item)
    return sorted(books)


def main():
    """Generate JSON for all books or single book."""
    import sys

    if len(sys.argv) < 2:
        print("Usage: python universal_pass6_generator.py Books/")
        print("   or: python universal_pass6_generator.py Books/clean-architecture/")
        sys.exit(1)

    root_dir = Path(sys.argv[1])

    if not root_dir.exists():
        print(f"Error: {root_dir} not found")
        sys.exit(1)

    # Find books
    if (root_dir / "00_purpose.md").exists():
        # Single book
        books = [root_dir]
    else:
        # Multiple books
        books = find_book_directories(root_dir)

    if not books:
        print(f"No books found in {root_dir}")
        sys.exit(1)

    print(f"Generating JSON for {len(books)} book(s)...\n")

    results = []
    for book in books:
        success, message = process_book(book, verbose=True)
        results.append((success, message))

    print("\n" + "=" * 60)
    print("RESULTS")
    print("=" * 60)

    success_count = sum(1 for s, _ in results if s)
    for success, message in results:
        print(message)

    print(f"\n{success_count}/{len(results)} books processed successfully")

    return 0 if success_count == len(results) else 1


if __name__ == '__main__':
    import sys
    sys.exit(main())
