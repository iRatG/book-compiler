"""
Real Data Parser for Clean Architecture

Extracts ONLY what's actually in the markdown.
No invented data. Full source tracking.
"""

import re
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple


class RealDataParser:
    """Parse 5-layer markdown and extract only real data."""

    def __init__(self, book_dir: Path):
        self.book_dir = Path(book_dir)
        self.layers = {}
        self._load_layers()

    def _load_layers(self):
        """Load all 5 markdown files."""
        for i in range(5):
            pattern = f"{i:02d}_*.md"
            files = list(self.book_dir.glob(pattern))
            if not files:
                raise FileNotFoundError(f"Layer {i} file not found in {self.book_dir}")
            self.layers[i] = files[0].read_text(encoding='utf-8')
            self.layer_files = {i: files[0].name}

    def extract_metadata(self) -> Dict[str, str]:
        """Extract metadata from 00_purpose.md."""
        content = self.layers[0]

        metadata = {}

        # Extract from markdown headers
        if 'Book:' in content:
            match = re.search(r'\*\*Book:\*\*\s+(.+?)\n', content)
            if match:
                metadata['title'] = match.group(1).strip()

        if 'Author:' in content:
            match = re.search(r'\*\*Author:\*\*\s+(.+?)\n', content)
            if match:
                metadata['author'] = match.group(1).strip()

        if 'Publication:' in content:
            match = re.search(r'\*\*Publication:\*\*\s+(.+?)\n', content)
            if match:
                metadata['publication'] = match.group(1).strip()

        return metadata

    def extract_principles(self) -> List[Dict[str, Any]]:
        """Extract ONLY main PRINCIPLE 1, 2, 3... (not sub-sections)."""
        content = self.layers[2]

        # Split by PRINCIPLE N (main level only)
        # Pattern: ## PRINCIPLE N: Name
        pattern = r'##\s+PRINCIPLE\s+(\d+)[:\s]+(.+?)\n'
        matches = list(re.finditer(pattern, content))

        principles = []
        for i, match in enumerate(matches):
            principle_num = match.group(1).strip()
            principle_name = match.group(2).strip()

            # Get content until next PRINCIPLE or end
            start_pos = match.end()
            if i + 1 < len(matches):
                end_pos = matches[i + 1].start()
                principle_body = content[start_pos:end_pos]
            else:
                principle_body = content[start_pos:]

            # Extract statement/claim
            statement = self._extract_section(principle_body, ['Statement', 'Claim', 'Metaphor'])

            # Extract tags for this principle
            tags = self._extract_tags_from_section(principle_body)

            principle = {
                'id': f'principle_{principle_num}',
                'number': int(principle_num),
                'principle': principle_name,
                'statement': statement or principle_body.split('\n\n')[0],
                'raw_content': principle_body,
                'tags': tags,
                'source': f"02_ideas.md: PRINCIPLE {principle_num}",
                'start_line': content[:match.start()].count('\n') + 1
            }
            principles.append(principle)

        return principles

    def extract_arguments(self) -> List[Dict[str, Any]]:
        """Extract arguments from 03_reasoning.md."""
        content = self.layers[3]

        # Pattern: ## ARG-001: Name or ## Argument 1: Name
        pattern = r'##\s+(?:ARG-(\d+)|Argument\s+(\d+))[:\s]+(.+?)\n'
        matches = list(re.finditer(pattern, content))

        arguments = []
        for i, match in enumerate(matches):
            arg_num = match.group(1) or match.group(2)
            arg_name = match.group(3).strip()

            start_pos = match.end()
            if i + 1 < len(matches):
                end_pos = matches[i + 1].start()
                arg_body = content[start_pos:end_pos]
            else:
                arg_body = content[start_pos:]

            # Extract claim, evidence, tags
            claim = self._extract_section(arg_body, ['Claim', 'Argument'])
            evidence = self._extract_evidence(arg_body)
            tags = self._extract_tags_from_section(arg_body)

            argument = {
                'id': f'arg_{arg_num.zfill(3)}',
                'number': int(arg_num),
                'name': arg_name,
                'claim': claim,
                'evidence': evidence,
                'tags': tags,
                'raw_content': arg_body,
                'source': f"03_reasoning.md: Argument {arg_num}",
                'start_line': content[:match.start()].count('\n') + 1
            }
            arguments.append(argument)

        return arguments

    def extract_implications(self) -> List[Dict[str, Any]]:
        """Extract practical implications from 04_consequences.md."""
        content = self.layers[4]

        # Pattern: ## IMPLICATION N: Name or ## Application N: Name
        pattern = r'##\s+(?:IMPLICATION|APPLICATION|IMPLICATION)\s+(\d+)[:\s]+(.+?)\n'
        matches = list(re.finditer(pattern, content))

        implications = []
        for i, match in enumerate(matches):
            impl_num = match.group(1).strip()
            impl_name = match.group(2).strip()

            start_pos = match.end()
            if i + 1 < len(matches):
                end_pos = matches[i + 1].start()
                impl_body = content[start_pos:end_pos]
            else:
                impl_body = content[start_pos:]

            # Extract sections
            what_means = self._extract_section(impl_body, ['What this means'])
            example = self._extract_section(impl_body, ['Example', 'Code Example'])
            arch_application = self._extract_section(impl_body, ['Architectural application'])
            practical_adoption = self._extract_section(impl_body, ['Practical adoption'])
            why_matters = self._extract_section(impl_body, ['Why it matters'])
            tags = self._extract_tags_from_section(impl_body)

            implication = {
                'id': f'impl_{impl_num.zfill(3)}',
                'number': int(impl_num),
                'name': impl_name,
                'what_means': what_means,
                'example': example,
                'architectural_application': arch_application,
                'practical_adoption': practical_adoption,
                'why_matters': why_matters,
                'tags': tags,
                'raw_content': impl_body,
                'source': f"04_consequences.md: Implication {impl_num}",
                'start_line': content[:match.start()].count('\n') + 1
            }
            implications.append(implication)

        return implications

    def extract_questions(self) -> List[Dict[str, Any]]:
        """Extract central questions from 01_questions.md."""
        content = self.layers[1]

        # Pattern: ### Question N: ... or similar
        pattern = r'#{3,4}\s+(?:Question|Q)\s+(\d+)[:\s]+(.+?)\n'
        matches = list(re.finditer(pattern, content))

        questions = []
        for i, match in enumerate(matches):
            q_num = match.group(1).strip()
            q_text = match.group(2).strip()

            start_pos = match.end()
            if i + 1 < len(matches):
                end_pos = matches[i + 1].start()
                q_body = content[start_pos:end_pos]
            else:
                q_body = content[start_pos:]

            tags = self._extract_tags_from_section(q_body)

            question = {
                'id': f'question_{q_num.zfill(2)}',
                'number': int(q_num),
                'text': q_text,
                'tags': tags,
                'raw_content': q_body,
                'source': f"01_questions.md: Question {q_num}",
                'start_line': content[:match.start()].count('\n') + 1
            }
            questions.append(question)

        return questions

    def extract_tags_global(self) -> set:
        """Extract all unique tags across all layers."""
        all_tags = set()
        for i in range(5):
            tags = re.findall(r'#(\w+[\w-]*)', self.layers[i])
            all_tags.update(tags)
        return all_tags

    # === Helper Methods ===

    def _extract_section(self, text: str, headers: List[str]) -> Optional[str]:
        """Extract content after a specific header."""
        for header in headers:
            # Try exact match
            pattern = rf'\*\*{re.escape(header)}:\*\*\s+(.+?)(?=\n\n|\*\*|###|$)'
            match = re.search(pattern, text, re.DOTALL)
            if match:
                return match.group(1).strip()

            # Try case-insensitive
            pattern = rf'(?i){re.escape(header)}\s*:?\s+(.+?)(?=\n\n|\*\*|###|$)'
            match = re.search(pattern, text, re.DOTALL)
            if match:
                return match.group(1).strip()

        # Return first paragraph if nothing matched
        first_para = text.split('\n\n')[0]
        if first_para:
            return first_para.strip()
        return None

    def _extract_evidence(self, text: str) -> List[Dict[str, str]]:
        """Extract evidence blocks from reasoning section."""
        evidence_list = []

        # Look for "Evidence A:", "Evidence B:", etc
        pattern = r'###?\s+Evidence\s+([A-Z]):\s+(.+?)(?=###|Evidence|$)'
        matches = re.finditer(pattern, text, re.DOTALL)

        for match in matches:
            label = match.group(1)
            content = match.group(2).strip()
            evidence_list.append({
                'label': f'Evidence {label}',
                'content': content.split('\n\n')[0]
            })

        return evidence_list

    def _extract_tags_from_section(self, text: str) -> List[str]:
        """Extract #tags from section."""
        tags = re.findall(r'#(\w+[\w-]*)', text)
        return list(set(tags))  # unique

    def link_principle_to_arguments_and_implications(
        self,
        principles: List[Dict],
        arguments: List[Dict],
        implications: List[Dict],
        questions: List[Dict]
    ) -> Dict[str, Any]:
        """Link principles to supporting arguments and implications."""

        links = {}

        # Link by tags (principles and arguments/implications with same tags)
        principle_tags = {p['id']: set(p['tags']) for p in principles}
        arg_tags = {a['id']: set(a['tags']) for a in arguments}
        impl_tags = {i['id']: set(i['tags']) for i in implications}

        for principle in principles:
            p_id = principle['id']
            links[p_id] = {
                'principle': principle,
                'supporting_arguments': [],
                'related_implications': [],
                'related_questions': []
            }

            # Find arguments with overlapping tags
            for arg in arguments:
                if principle_tags[p_id] & arg_tags[arg['id']]:
                    links[p_id]['supporting_arguments'].append(arg)

            # Find implications with overlapping tags
            for impl in implications:
                if principle_tags[p_id] & impl_tags[impl['id']]:
                    links[p_id]['related_implications'].append(impl)

            # Find questions with overlapping tags
            for q in questions:
                q_tags = set(q['tags'])
                if principle_tags[p_id] & q_tags:
                    links[p_id]['related_questions'].append(q)

        return links


# Test usage
if __name__ == '__main__':
    import json

    parser = RealDataParser(Path('Books/clean-architecture'))

    # Extract all data
    metadata = parser.extract_metadata()
    principles = parser.extract_principles()
    arguments = parser.extract_arguments()
    implications = parser.extract_implications()
    questions = parser.extract_questions()
    tags = parser.extract_tags_global()

    print(f"[OK] Metadata: {metadata}")
    print(f"[OK] Principles found: {len(principles)}")
    for p in principles:
        print(f"  - {p['id']}: {p['principle']}")

    print(f"[OK] Arguments found: {len(arguments)}")
    print(f"[OK] Implications found: {len(implications)}")
    print(f"[OK] Questions found: {len(questions)}")
    print(f"[OK] Unique tags: {len(tags)}")
    print(f"  Tags: {', '.join(sorted(tags)[:10])}... ({len(tags)} total)")
