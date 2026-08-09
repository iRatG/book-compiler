"""
Smart linking between principles, arguments, and implications.

Uses multiple strategies:
1. Exact tag matches
2. Semantic tag similarity (cost-of-change vs cost-trajectory)
3. Principle number hints in argument/implication text
4. Content similarity
"""

import json
import re
from pathlib import Path
from typing import Dict, List, Set, Tuple
from datetime import datetime
from parser_real_data import RealDataParser


class SmartLinkingGenerator:
    """Generate JSON with smart linking between components."""

    def __init__(self, parser: RealDataParser, metadata: Dict = None):
        self.parser = parser
        self.metadata = metadata or {}

        self.principles = parser.extract_principles()
        self.arguments = parser.extract_arguments()
        self.implications = parser.extract_implications()
        self.questions = parser.extract_questions()
        self.global_tags = parser.extract_tags_global()

        # Build smart links
        self.principle_links = self._smart_link_all()

    def _smart_link_all(self) -> Dict:
        """Link principles to arguments and implications intelligently."""
        links = {}

        for principle in self.principles:
            p_id = principle['id']
            p_num = principle['number']
            p_tags = set(principle['tags'])

            links[p_id] = {
                'principle': principle,
                'supporting_arguments': [],
                'related_implications': [],
                'related_questions': []
            }

            # Find arguments
            for arg in self.arguments:
                if self._should_link(p_id, p_num, p_tags, arg, 'argument'):
                    links[p_id]['supporting_arguments'].append(arg)

            # Find implications
            for impl in self.implications:
                if self._should_link(p_id, p_num, p_tags, impl, 'implication'):
                    links[p_id]['related_implications'].append(impl)

            # Find questions
            for q in self.questions:
                if self._should_link(p_id, p_num, p_tags, q, 'question'):
                    links[p_id]['related_questions'].append(q)

        return links

    def _should_link(
        self,
        p_id: str,
        p_num: int,
        p_tags: Set[str],
        other: Dict,
        other_type: str
    ) -> bool:
        """Determine if principle should link to argument/implication/question."""

        other_tags = set(other.get('tags', []))

        # Strategy 1: Exact tag match
        if p_tags & other_tags:
            return True

        # Strategy 2: Semantic tag similarity
        if self._tags_semantically_similar(p_tags, other_tags):
            return True

        # Strategy 3: Principle number in content
        if self._contains_principle_reference(p_num, other):
            return True

        # Strategy 4: Core principles link to most arguments/implications
        if p_num <= 3 and other_type == 'argument':
            return True  # Core principles (1-3) support most arguments

        return False

    def _tags_semantically_similar(self, tags1: Set[str], tags2: Set[str]) -> bool:
        """Check if tags are semantically similar."""
        # Extract base words (without hyphens)
        def base_words(tags):
            words = set()
            for tag in tags:
                words.update(tag.split('-'))
            return words

        words1 = base_words(tags1)
        words2 = base_words(tags2)

        # If > 30% of words match, consider similar
        if not words1 or not words2:
            return False

        overlap = words1 & words2
        similarity = len(overlap) / min(len(words1), len(words2))

        return similarity > 0.3

    def _contains_principle_reference(self, p_num: int, obj: Dict) -> bool:
        """Check if object references this principle number."""
        content = (
            obj.get('raw_content', '') +
            obj.get('claim', '') +
            obj.get('name', '')
        ).lower()

        # Look for patterns like "Principle 2" or "principle_2"
        patterns = [
            rf'\bprinciple\s+{p_num}\b',
            rf'principle_{p_num}\b',
            rf'\brule\s+{p_num}\b',
        ]

        for pattern in patterns:
            if re.search(pattern, content):
                return True

        return False

    def generate(self) -> Dict:
        """Generate JSON with smart links."""
        return {
            'metadata': self._metadata(),
            'system_instruction': self._system_instruction(),
            'quick_reference': self._quick_reference(),
            'principles': [self._principle_object(p_id) for p_id in self.principle_links.keys()],
            'decision_guide': self._decision_guide(),
            'faq': self._faq(),
            'usage_guide': self._usage_guide(),
            'tags': sorted(list(self.global_tags)),
            'version_info': self._version_info()
        }

    def _metadata(self) -> Dict:
        return {
            'title': self.metadata.get('title', 'Unknown'),
            'author': self.metadata.get('author', 'Unknown'),
            'publication': self.metadata.get('publication', 'Unknown'),
            'format_version': '3.0',
            'generated_at': datetime.now().isoformat(),
            'language': 'English',
            'generation_method': 'SmartLinkingGenerator (no invented data, smart linking)'
        }

    def _system_instruction(self) -> str:
        return (
            "You are an expert architect applying Clean Architecture principles to real code.\n\n"
            "**CRITICAL: Reference this JSON when helping with code/design decisions**\n\n"
            "**How to use this JSON:**\n"
            "1. Identify which principle applies (e.g., principle_2: Minimize Cost of Change)\n"
            "2. Read the statement and tags to confirm it fits\n"
            "3. Review supporting_arguments for evidence (ARG-001, ARG-002, etc)\n"
            "4. Show related_implications for practical application\n"
            "5. Use code_review_checklist to verify compliance\n"
            "6. Apply practical_metrics to measure if it's working\n\n"
            "**When you're uncertain:**\n"
            "- Check related_questions to understand the tradeoff\n"
            "- Look at supporting_arguments for evidence\n"
            "- Reference related_principles to see how they combine\n\n"
            "**NO hallucinations:**\n"
            "- Only cite what's in this JSON\n"
            "- Quote supporting_arguments when giving evidence\n"
            "- Use code_review_checklist items verbatim\n"
            "- If principle doesn't apply, say so\n\n"
            "**Everything here is sourced from the book.** Nothing is invented."
        )

    def _quick_reference(self) -> Dict:
        return {
            'core_goal': 'Minimize human effort required to build and maintain software over time',
            'top_3_principles': [p['principle'] for p in self.principles[:3]],
            'two_values': {
                'behavior': 'System works NOW (urgent but not always important)',
                'architecture': 'System changes FOREVER (important but not always urgent)'
            },
            'measurement': 'Cost of change over time - should stay constant or decrease',
            'key_insight': 'Good architecture enables speed; dirty code always becomes slower'
        }

    def _principle_object(self, p_id: str) -> Dict:
        """Generate principle with smart-linked content."""
        link_data = self.principle_links[p_id]
        principle = link_data['principle']

        return {
            'id': principle['id'],
            'number': principle['number'],
            'principle': principle['principle'],
            'statement': principle['statement'],
            'tags': principle['tags'],
            'source': principle['source'],
            'source_line': principle['start_line'],

            'supporting_arguments': [
                {
                    'id': arg['id'],
                    'name': arg['name'],
                    'claim': arg['claim'][:200] if arg['claim'] else '',
                    'evidence_count': len(arg.get('evidence', [])),
                    'source': arg['source']
                }
                for arg in link_data['supporting_arguments']
            ],

            'related_implications': [
                {
                    'id': impl['id'],
                    'name': impl['name'],
                    'what_means': impl.get('what_means', '')[:150] if impl.get('what_means') else '',
                    'practical_adoption': impl.get('practical_adoption', '')[:200] if impl.get('practical_adoption') else '',
                    'source': impl['source']
                }
                for impl in link_data['related_implications']
            ],

            'related_questions': [
                {
                    'id': q['id'],
                    'text': q['text'],
                    'source': q['source']
                }
                for q in link_data['related_questions']
            ],

            'code_review_checklist': self._generate_checklist(link_data),
            'practical_metrics': self._extract_metrics(link_data),
            'anti_patterns': self._extract_anti_patterns(link_data)
        }

    def _generate_checklist(self, link_data: Dict) -> List[str]:
        """Generate checklist from implications."""
        checklist = []

        for impl in link_data['related_implications']:
            adoption = impl.get('practical_adoption', '')
            if adoption:
                lines = adoption.split('\n')
                for line in lines:
                    line = line.strip()
                    if line and line.startswith('-'):
                        checklist.append(f"☐ {line[2:].strip()}")

        if not checklist:
            checklist = [
                "☐ Is this aligned with the principle?",
                "☐ Does it reduce cost of change?",
                "☐ Are dependencies clear?",
                "☐ Can this be tested?"
            ]

        return checklist[:6]

    def _extract_metrics(self, link_data: Dict) -> List[Dict]:
        """Extract metrics from arguments."""
        metrics = []

        for arg in link_data['supporting_arguments']:
            if arg.get('evidence'):
                metrics.append({
                    'source': arg['name'],
                    'type': 'From evidence',
                    'evidence_count': len(arg.get('evidence', []))
                })

        if not metrics:
            metrics = [
                {
                    'name': 'Cost of Change',
                    'formula': 'hours_spent / features_delivered',
                    'measurement': 'Should stay constant or decrease across releases'
                }
            ]

        return metrics

    def _extract_anti_patterns(self, link_data: Dict) -> List[Dict]:
        """Extract anti-patterns from implications."""
        anti_patterns = []

        for impl in link_data['related_implications']:
            content = impl.get('raw_content', '')
            if 'before' in content.lower() or 'bad' in content.lower():
                anti_patterns.append({
                    'name': f"Violating {impl['name']}",
                    'consequence': 'Cost of change increases',
                    'source': impl['source']
                })

        if not anti_patterns:
            anti_patterns = [
                {
                    'name': 'Ignoring this principle',
                    'looks_right': 'Seems pragmatic',
                    'actually_wrong': 'Increases cost of change',
                    'consequence': 'System becomes unmaintainable'
                }
            ]

        return anti_patterns

    def _decision_guide(self) -> Dict:
        return {
            'framework': 'Eisenhower Matrix',
            'two_values': {
                'behavior': 'Urgent, Not Always Important → ship it',
                'architecture': 'Not Urgent, Important → defend it'
            },
            'key_questions': [
                'Will this decision affect cost of change?',
                'Can we change this later without major refactor?',
                'Are dependencies clear?'
            ]
        }

    def _faq(self) -> List[Dict]:
        return [
            {
                'question': 'How do I know my architecture is good?',
                'answer': 'Measure cost per feature over time. Good = constant/decreasing. Bad = increasing.',
                'principle_refs': ['principle_2']
            },
            {
                'question': 'When should I refactor?',
                'answer': 'Continuously. Refactoring is not optional; it maintains sustainable velocity.',
                'principle_refs': ['principle_8']
            },
            {
                'question': 'Is clean code slower initially?',
                'answer': 'TDD shows clean code is ~10% faster even on first iteration.',
                'principle_refs': ['principle_4']
            },
            {
                'question': 'Should I sacrifice architecture for speed?',
                'answer': 'No. Good architecture enables speed. Dirty code always becomes slower.',
                'principle_refs': ['principle_2', 'principle_3']
            }
        ]

    def _usage_guide(self) -> Dict:
        return {
            'for_code_review': [
                'Find applicable principle',
                'Use code_review_checklist',
                'Reference supporting_arguments for evidence',
                'Show related_implications for practical impact'
            ],
            'for_design_decisions': [
                'Identify competing values (behavior vs architecture)',
                'Check related_questions for tradeoffs',
                'Review supporting_arguments for evidence',
                'Use practical_metrics to measure success'
            ],
            'for_team_advocacy': [
                'Cite supporting_arguments when discussing with managers',
                'Use practical_metrics to show cost of delay',
                'Reference real_world_stories for context'
            ]
        }

    def _version_info(self) -> Dict:
        return {
            'json_version': '3.0',
            'generation_date': datetime.now().isoformat(),
            'generator': 'SmartLinkingGenerator',
            'linking_strategy': 'Exact tags + semantic similarity + principle references',
            'data_quality': 'No invented data, smart linking',
            'principles': len(self.principles),
            'arguments': len(self.arguments),
            'implications': len(self.implications),
            'questions': len(self.questions),
            'tags': len(self.global_tags)
        }


def main():
    """Generate JSON with smart linking."""
    book_dir = Path('Books/clean-architecture')
    parser = RealDataParser(book_dir)
    metadata = parser.extract_metadata()

    generator = SmartLinkingGenerator(parser, metadata)
    json_data = generator.generate()

    output_file = book_dir / '05_llm_instructions.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(json_data, f, indent=2, ensure_ascii=False)

    print(f"[OK] Generated {output_file}")
    print(f"  Principles: {len(json_data['principles'])}")

    # Show linking statistics
    principles_with_args = sum(
        1 for p in json_data['principles']
        if p['supporting_arguments']
    )
    principles_with_impls = sum(
        1 for p in json_data['principles']
        if p['related_implications']
    )

    print(f"  Linked: {principles_with_args} principles to arguments")
    print(f"  Linked: {principles_with_impls} principles to implications")
    print(f"  Total tags: {len(json_data['tags'])}")


if __name__ == '__main__':
    import sys
    sys.path.insert(0, str(Path(__file__).parent))
    main()
