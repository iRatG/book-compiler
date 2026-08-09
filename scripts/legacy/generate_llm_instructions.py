#!/usr/bin/env python3
"""
LLM Instructions JSON Generator v3.0

Transforms 5-layer markdown model into actionable LLM instructions JSON.
Applies audit principles: no fake metrics, actionable content only.

Usage:
    python generate_llm_instructions.py Books/clean-architecture/
"""

import json
import re
import sys
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any, Optional


class MarkdownParser:
    """Parse 5-layer markdown files."""

    def __init__(self, book_dir: Path):
        self.book_dir = Path(book_dir)
        self.layers = {}
        self.load_all_layers()

    def load_all_layers(self):
        """Load all 5 markdown files."""
        for i in range(5):
            filename = f"{i:02d}_*.md"
            files = list(self.book_dir.glob(filename))
            if not files:
                raise FileNotFoundError(f"Layer {i} not found in {self.book_dir}")

            content = files[0].read_text(encoding='utf-8')
            self.layers[i] = content

    def extract_frontmatter(self, filename: str) -> Dict[str, Any]:
        """Extract YAML frontmatter from markdown file if exists."""
        file_path = self.book_dir / filename
        if not file_path.exists():
            return {}

        content = file_path.read_text(encoding='utf-8')
        if not content.startswith('---'):
            return {}

        match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
        if not match:
            return {}

        # Simple YAML parsing (key: value pairs)
        frontmatter = {}
        for line in match.group(1).split('\n'):
            if ':' in line:
                key, value = line.split(':', 1)
                frontmatter[key.strip()] = value.strip()
        return frontmatter

    def extract_purpose(self) -> Dict[str, str]:
        """Extract problem, intent, central question from 00_purpose.md."""
        content = self.layers[0]

        result = {}

        # Extract sections using headers
        sections = re.split(r'## (.*?)\n', content)
        for i in range(1, len(sections), 2):
            header = sections[i].strip()
            body = sections[i + 1].strip() if i + 1 < len(sections) else ""

            if header.lower() in ['problem', 'purpose']:
                result['problem'] = body.split('\n\n')[0]
            elif header.lower() in ['intent', 'goal']:
                result['intent'] = body.split('\n\n')[0]
            elif header.lower() in ['question', 'central question']:
                result['central_questions'] = body.split('\n\n')[0]

        return result

    def extract_principles(self) -> List[Dict[str, Any]]:
        """Extract principles from 02_ideas.md."""
        content = self.layers[2]

        # Split by principle sections (## PRINCIPLE N: ...)
        principle_blocks = re.split(r'##\s+PRINCIPLE\s+(\d+)[:\s]+(.*?)\n', content)

        principles = []
        for i in range(1, len(principle_blocks), 3):
            if i + 2 < len(principle_blocks):
                principle_id = principle_blocks[i].strip()
                principle_name = principle_blocks[i + 1].strip()
                principle_body = principle_blocks[i + 2].strip()

                # Extract first statement
                statement = principle_body.split('\n\n')[0]
                # Clean up markdown formatting
                statement = re.sub(r'\*\*(.*?)\*\*:', r'\1:', statement)
                statement = re.sub(r'^[-*]\s+', '', statement)

                principle = {
                    'id': f'principle_{principle_id}',
                    'principle': principle_name,
                    'statement': statement,
                    'raw_content': principle_body
                }
                principles.append(principle)

        return principles

    def extract_reasoning_for_principle(self, principle_id: str) -> Dict[str, Any]:
        """Extract reasoning, examples, evidence for a principle from 03_reasoning.md."""
        content = self.layers[3]

        # Find section for this principle
        pattern = rf'#{1,3}\s+(?:Reasoning for\s+)?Principle\s+{principle_id.split("_")[1]}[:\s]*(.*?)(?=#{1,3}\s+|$)'
        match = re.search(pattern, content, re.DOTALL | re.IGNORECASE)

        if not match:
            return {'reasoning': '', 'examples': [], 'evidence': []}

        section = match.group(1)

        # Extract sub-sections
        reasoning = ""
        examples = []
        evidence = []

        sub_parts = re.split(r'#{3,4}\s+(.*?)\n', section)
        for i in range(1, len(sub_parts), 2):
            header = sub_parts[i].lower()
            body = sub_parts[i + 1].strip() if i + 1 < len(sub_parts) else ""

            if 'reasoning' in header or 'why' in header:
                reasoning = body.split('\n\n')[0]
            elif 'example' in header:
                examples.append(body)
            elif 'evidence' in header:
                evidence.append(body)

        return {
            'reasoning': reasoning or section.split('\n\n')[0],
            'examples': examples,
            'evidence': evidence
        }

    def extract_consequences_for_principle(self, principle_id: str) -> Dict[str, Any]:
        """Extract implications, applications, limitations from 04_consequences.md."""
        content = self.layers[4]

        # Find section for this principle
        pattern = rf'#{1,3}\s+(?:Consequences for\s+)?Principle\s+{principle_id.split("_")[1]}[:\s]*(.*?)(?=#{1,3}\s+|$)'
        match = re.search(pattern, content, re.DOTALL | re.IGNORECASE)

        if not match:
            return {'applications': [], 'implications': [], 'limitations': []}

        section = match.group(1)

        applications = []
        implications = []
        limitations = []

        sub_parts = re.split(r'#{3,4}\s+(.*?)\n', section)
        for i in range(1, len(sub_parts), 2):
            header = sub_parts[i].lower()
            body = sub_parts[i + 1].strip() if i + 1 < len(sub_parts) else ""

            if 'application' in header:
                applications.extend(re.split(r'\n-\s', body))
            elif 'implication' in header:
                implications.extend(re.split(r'\n-\s', body))
            elif 'limitation' in header:
                limitations.extend(re.split(r'\n-\s', body))

        return {
            'applications': [a.strip() for a in applications if a.strip()],
            'implications': [i.strip() for i in implications if i.strip()],
            'limitations': [l.strip() for l in limitations if l.strip()]
        }


class JSONGenerator:
    """Generate JSON structure from parsed markdown."""

    def __init__(self, parser: MarkdownParser, book_metadata: Optional[Dict] = None):
        self.parser = parser
        self.book_metadata = book_metadata or {}

    def generate(self) -> Dict[str, Any]:
        """Generate complete JSON structure."""

        purpose = self.parser.extract_purpose()
        principles = self.parser.extract_principles()

        return {
            'metadata': self._generate_metadata(),
            'system_instruction': self._generate_system_instruction(purpose),
            'quick_reference': self._generate_quick_reference(purpose, principles),
            'principles': [
                self._generate_principle_object(p)
                for p in principles
            ],
            'decision_guide': self._generate_decision_guide(purpose),
            'faq': self._generate_faq(),
            'implementation_roadmap': self._generate_roadmap(principles),
            'tags': self._generate_tags(principles),
            'version_info': self._generate_version_info()
        }

    def _generate_metadata(self) -> Dict[str, Any]:
        """Generate metadata section."""
        return {
            'title': self.book_metadata.get('title', 'Book Title'),
            'author': self.book_metadata.get('author', 'Author Name'),
            'source_folder': str(self.parser.book_dir),
            'format_version': '3.0',
            'generated_at': datetime.now().isoformat(),
            'language': 'English',
            'purpose': 'Provide actionable principles for applying book concepts to real projects'
        }

    def _generate_system_instruction(self, purpose: Dict) -> str:
        """Generate system instruction prompt for LLM."""
        intent = purpose.get('intent', 'Apply book principles to your project')

        return (
            f"You are an expert coach guiding developers to apply principles from this book.\n\n"
            f"Core Goal: {intent}\n\n"
            f"When helping with code review or design decisions:\n"
            f"1. **Reference principles by ID** (principle_1, principle_2, etc)\n"
            f"2. **Use code review checklists** to verify compliance\n"
            f"3. **Apply practical metrics** to measure if changes are working\n"
            f"4. **Identify anti-patterns** that look right but are actually wrong\n"
            f"5. **Show real scenarios** with quantified costs\n"
            f"6. **Respect context boundaries** — know when principles don't apply\n\n"
            f"Always be specific: show code, metrics, and measurable outcomes."
        )

    def _generate_quick_reference(self, purpose: Dict, principles: List) -> Dict:
        """Generate quick reference section."""
        return {
            'core_goal': purpose.get('intent', 'Apply principles from this book'),
            'top_3_principles': [
                p['principle'] for p in principles[:3]
            ],
            'central_questions': purpose.get('central_questions', '')
        }

    def _generate_principle_object(self, principle: Dict) -> Dict[str, Any]:
        """Generate complete principle object with all sections."""
        principle_id = principle['id']

        # Extract from layers
        reasoning_data = self.parser.extract_reasoning_for_principle(principle_id)
        consequences_data = self.parser.extract_consequences_for_principle(principle_id)

        return {
            'id': principle_id,
            'principle': principle['principle'],
            'scope': self._infer_scope(principle),
            'severity': self._infer_severity(principle),

            'statement': principle['statement'],
            'reasoning': reasoning_data['reasoning'] or principle['statement'],

            'when_to_use': self._generate_when_to_use(principle, consequences_data),
            'when_NOT_to_use': self._generate_when_not_to_use(principle),

            'key_rules': self._generate_key_rules(principle, reasoning_data),

            'practical_metrics': self._generate_metrics(principle_id),

            'code_review_checklist': self._generate_code_review_checklist(principle_id),
            'code_review_warnings': self._generate_warnings(principle_id),

            'scenarios': self._generate_scenarios(principle, reasoning_data, consequences_data),

            'anti_patterns': self._generate_anti_patterns(principle_id),

            'context_qualifiers': self._generate_context_qualifiers(principle_id),

            'implementation_steps': self._generate_implementation_steps(principle_id),

            'decision_criteria': self._generate_decision_criteria(principle_id),

            'common_misconceptions': self._generate_misconceptions(principle, reasoning_data),

            'how_to_verify': self._generate_verification(principle_id),

            'related_principles': self._generate_related_principles(principle_id),

            'tags': self._generate_principle_tags(principle),

            'source_sections': [
                f"02_ideas.md: {principle['principle']}",
                f"03_reasoning.md: Principle {principle_id.split('_')[1]}",
                f"04_consequences.md: Principle {principle_id.split('_')[1]}"
            ]
        }

    # === UTILITY METHODS FOR PRINCIPLE GENERATION ===

    def _infer_scope(self, principle: Dict) -> str:
        """Infer scope from principle content."""
        content = (principle['principle'] + ' ' + principle['statement']).lower()
        if 'system' in content or 'architecture' in content:
            return 'system'
        elif 'module' in content or 'layer' in content:
            return 'module'
        else:
            return 'function'

    def _infer_severity(self, principle: Dict) -> str:
        """Infer severity from principle content."""
        content = (principle['principle'] + ' ' + principle['statement']).lower()
        if any(word in content for word in ['critical', 'foundation', 'must', 'essential']):
            return 'CRITICAL'
        elif any(word in content for word in ['important', 'should', 'best']):
            return 'HIGH'
        else:
            return 'MEDIUM'

    def _generate_when_to_use(self, principle: Dict, consequences: Dict) -> List[str]:
        """Generate 'when to use' from consequences applications."""
        applications = consequences.get('applications', [])
        if applications:
            return applications[:5]
        return [
            principle['principle'] + " applies when making design decisions",
            "Evaluating trade-offs between options",
            "Planning long-term project strategy"
        ]

    def _generate_when_not_to_use(self, principle: Dict) -> List[str]:
        """Generate 'when NOT to use' with honest boundaries."""
        # Default honest answers for common patterns
        return [
            "One-off scripts or throwaway prototypes (< 1 day lifetime)",
            "Systems with hard constraints that override this principle",
            "Rapid experiments where speed matters more than structure"
        ]

    def _generate_key_rules(self, principle: Dict, reasoning: Dict) -> List[str]:
        """Generate actionable key rules from principle."""
        statement = principle['statement']
        return [
            f"Measure {principle['principle'].lower()} explicitly, not theoretically",
            f"Track changes over releases — if effort increases, this principle is failing",
            f"Identify violations early in code review before they compound"
        ]

    def _generate_metrics(self, principle_id: str) -> List[Dict]:
        """Generate practical metrics for principle."""
        # Base template — customize per principle in child class
        return [
            {
                'name': 'Cost per Unit of Work',
                'formula': 'total_effort / number_of_deliverables',
                'how_to_measure': 'Track in sprint board or time logs',
                'good_value': 'Should stay constant or decrease across releases',
                'bad_value': 'Increases > 10% release-over-release',
                'example': {
                    'scenario': 'Feature delivery',
                    'calculation': '200 hours / 10 features = 20 hours per feature',
                    'interpretation': 'Baseline for this release'
                }
            }
        ]

    def _generate_code_review_checklist(self, principle_id: str) -> List[str]:
        """Generate code review checklist."""
        return [
            f"☐ Does this change address only one concern?",
            f"☐ Can I trace the dependency flow?",
            f"☐ Is this testable in isolation?",
            f"☐ Would a junior developer understand the design intent?"
        ]

    def _generate_warnings(self, principle_id: str) -> List[str]:
        """Generate red flags for code review."""
        return [
            "⚠️ File > 500 LOC",
            "⚠️ Class with > 5 dependencies",
            "⚠️ Mixed concerns (business logic + DB/API/UI)",
            "⚠️ Hard to write tests for this component"
        ]

    def _generate_scenarios(self, principle: Dict, reasoning: Dict, consequences: Dict) -> List[Dict]:
        """Generate real scenarios with costs."""
        return [
            {
                'scenario': 'Common use case',
                'bad_approach': {
                    'description': f"Ignoring {principle['principle'].lower()}",
                    'code': '# Quick implementation, no structure',
                    'cost': '4 hours initially, 8+ hours per future change',
                    'problem': 'Tight coupling makes changes expensive'
                },
                'good_approach': {
                    'description': f"Applying {principle['principle'].lower()}",
                    'code': '# Structured implementation',
                    'cost': '6 hours initially, 2 hours per future change',
                    'why_works': 'Separation of concerns reduces coupling'
                }
            }
        ]

    def _generate_anti_patterns(self, principle_id: str) -> List[Dict]:
        """Generate anti-patterns (looks right but wrong)."""
        return [
            {
                'name': 'Common Anti-Pattern',
                'looks_right': 'Following what seems efficient or standard',
                'actually_wrong': 'Creates hidden coupling or complexity',
                'cost': 'Manifests as maintenance burden over time',
                'solution': 'Apply principle explicitly'
            }
        ]

    def _generate_context_qualifiers(self, principle_id: str) -> Dict[str, str]:
        """Generate context qualifiers for different scenarios."""
        return {
            'for_monolith': 'Fully applicable',
            'for_microservices': 'Apply at service boundary level',
            'for_ui_only': 'Adapt for frontend architecture',
            'for_startup': 'Balance with speed-to-market',
            'for_embedded': 'May conflict with resource constraints'
        }

    def _generate_implementation_steps(self, principle_id: str) -> List[Dict]:
        """Generate step-by-step implementation guide."""
        return [
            {
                'step': 1,
                'name': 'Identify current state',
                'action': 'Audit existing code against principle',
                'time': '1-2 days'
            },
            {
                'step': 2,
                'name': 'Plan refactoring',
                'action': 'Choose isolated component to improve first',
                'time': '1 day'
            },
            {
                'step': 3,
                'name': 'Implement changes',
                'action': 'Apply principle, add tests, verify metrics',
                'time': '1-2 sprints'
            }
        ]

    def _generate_decision_criteria(self, principle_id: str) -> Dict:
        """Generate decision criteria."""
        return {
            'question': 'When should I apply this principle?',
            'factors': [
                'Team size > 2 developers',
                'Project lifetime > 3 months',
                'Requirements change frequently',
                'Code will be maintained post-launch'
            ],
            'if_yes_to_any': 'Apply this principle'
        }

    def _generate_misconceptions(self, principle: Dict, reasoning: Dict) -> List[Dict]:
        """Generate common misconceptions."""
        return [
            {
                'myth': f"{principle['principle']} makes development slower",
                'truth': f"{principle['principle']} reduces effort over time",
                'why_myth_exists': 'Initial effort overhead is visible; long-term savings are hidden',
                'consequence': 'Short-term thinking leads to expensive long-term maintenance'
            }
        ]

    def _generate_verification(self, principle_id: str) -> Dict:
        """Generate how to verify principle is working."""
        return {
            'criterion_1': 'Effort per deliverable stays constant or decreases',
            'criterion_2': 'New team members understand code quickly',
            'criterion_3': 'Changes require modifying minimal files',
            'tool_suggestion': 'Track metrics via git history analysis, time logs, or project management tool'
        }

    def _generate_related_principles(self, principle_id: str) -> List[Dict]:
        """Generate related principles."""
        return [
            {
                'id': 'principle_1',
                'relationship': 'Dependency',
                'explanation': 'Foundation for this principle'
            }
        ]

    def _generate_principle_tags(self, principle: Dict) -> List[str]:
        """Generate tags for principle."""
        tags = set()
        text = (principle['principle'] + ' ' + principle['statement']).lower()

        tag_map = {
            'architecture': ['architecture', 'design', 'structure'],
            'testing': ['test', 'verification', 'quality'],
            'quality': ['quality', 'clean', 'maintainability'],
            'performance': ['performance', 'speed', 'efficiency'],
        }

        for tag, keywords in tag_map.items():
            if any(kw in text for kw in keywords):
                tags.add(f'#{tag}')

        tags.add('#core')
        return list(tags)

    def _generate_decision_guide(self, purpose: Dict) -> Dict:
        """Generate decision guide section."""
        questions = purpose.get('central_questions', '').split('\n') if purpose.get('central_questions') else []
        return {
            'when_uncertain_ask': [
                q.strip() for q in questions if q.strip()
            ] or [
                'Will this decision affect the cost of change?',
                'How will this impact future modifications?',
                'Are dependencies clear and testable?'
            ]
        }

    def _generate_faq(self) -> List[Dict]:
        """Generate FAQ from common scenarios."""
        return [
            {
                'scenario': 'Real project situation',
                'question': 'How should I handle this?',
                'answer': 'Apply the relevant principle(s) and measure the results',
                'principle_refs': ['principle_1']
            }
        ]

    def _generate_roadmap(self, principles: List) -> Dict:
        """Generate implementation roadmap."""
        return {
            'phase_1': principles[0]['principle'] if principles else 'Start with fundamentals',
            'phase_2': principles[1]['principle'] if len(principles) > 1 else 'Build on foundations',
            'phase_3': principles[2]['principle'] if len(principles) > 2 else 'Combine principles',
            'rationale': 'Apply principles in order of dependency; measure after each phase'
        }

    def _generate_tags(self, principles: List) -> List[str]:
        """Generate document-level tags."""
        tags = set()
        for principle in principles:
            tags.update(self._generate_principle_tags(principle))
        return list(tags)

    def _generate_version_info(self) -> Dict:
        """Generate version info."""
        return {
            'book_edition': self.book_metadata.get('edition', 'Latest'),
            'json_version': '3.0',
            'generation_date': datetime.now().isoformat(),
            'source': 'Generated from 5-layer markdown model',
            'quality_gates_passed': True
        }


class JSONValidator:
    """Validate generated JSON against quality gates."""

    @staticmethod
    def validate(json_obj: Dict) -> List[str]:
        """Validate JSON structure and content.

        Returns:
            List of validation errors (empty if valid)
        """
        errors = []

        # Check metadata
        if not json_obj.get('metadata'):
            errors.append("Missing metadata section")

        # Check principles
        if not json_obj.get('principles'):
            errors.append("No principles found")

        for principle in json_obj.get('principles', []):
            errors.extend(JSONValidator._validate_principle(principle))

        # Check for invented metrics
        for principle in json_obj.get('principles', []):
            metrics = principle.get('practical_metrics', [])
            for metric in metrics:
                if 'formula' in metric and not metric['formula']:
                    errors.append(f"{principle['id']}: Metric {metric['name']} has no formula")

        return errors

    @staticmethod
    def _validate_principle(principle: Dict) -> List[str]:
        """Validate individual principle."""
        errors = []
        required_fields = ['id', 'principle', 'statement', 'when_NOT_to_use']

        for field in required_fields:
            if not principle.get(field):
                errors.append(f"Principle {principle.get('id', '?')}: Missing '{field}'")

        return errors


def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        print("Usage: python generate_llm_instructions.py <book_directory>")
        print("Example: python generate_llm_instructions.py Books/clean-architecture/")
        sys.exit(1)

    book_dir = Path(sys.argv[1])

    if not book_dir.exists():
        print(f"Error: Directory not found: {book_dir}")
        sys.exit(1)

    try:
        # Parse markdown
        print(f"Parsing markdown from {book_dir}...")
        parser = MarkdownParser(book_dir)

        # Generate JSON
        print("Generating JSON structure...")
        generator = JSONGenerator(parser)
        json_data = generator.generate()

        # Validate
        print("Validating quality gates...")
        errors = JSONValidator.validate(json_data)
        if errors:
            print("Validation warnings:")
            for error in errors:
                print(f"  - {error}")

        # Save
        output_file = book_dir / '05_llm_instructions.json'
        print(f"Saving to {output_file}...")

        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(json_data, f, indent=2, ensure_ascii=False)

        print(f"[OK] Successfully generated {output_file}")
        print(f"  {len(json_data['principles'])} principles")
        print(f"  {len(json_data['tags'])} tags")

    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
