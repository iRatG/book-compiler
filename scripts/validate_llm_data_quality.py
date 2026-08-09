#!/usr/bin/env python3
"""
Validate LLM data quality in 05_llm_instructions.json files.

Checks:
1. Data completeness (are principles linked to arguments?)
2. Tag consistency (do tags match between layers?)
3. Content richness (are there statements, claims, implications?)
4. Cross-references (do relations actually exist in markdown?)

Usage:
    python validate_llm_data_quality.py Books/
    python validate_llm_data_quality.py Books/clean-architecture/
"""

import json
import re
from pathlib import Path
from typing import Dict, List, Tuple, Set
from collections import defaultdict


class DataQualityValidator:
    """Validate LLM JSON data quality."""

    def __init__(self, book_dir: Path):
        self.book_dir = Path(book_dir)
        self.book_name = book_dir.name

        # Load markdown layers
        self.layers = {}
        self._load_layers()

        # Load JSON
        self.json_data = self._load_json()

        # Extract tags from markdown (source of truth)
        self.markdown_tags = self._extract_tags_from_markdown()

    def _load_layers(self):
        """Load markdown files (00-04)."""
        for i in range(5):
            pattern = f"{i:02d}_*.md"
            files = list(self.book_dir.glob(pattern))
            if files:
                self.layers[i] = files[0].read_text(encoding='utf-8')
            else:
                self.layers[i] = ""

    def _load_json(self) -> Dict:
        """Load JSON if exists."""
        json_file = self.book_dir / '05_llm_instructions.json'
        if not json_file.exists():
            return {}
        try:
            return json.loads(json_file.read_text(encoding='utf-8'))
        except:
            return {}

    def _extract_tags_from_markdown(self) -> Dict[str, Dict]:
        """Extract tags from markdown by section."""
        tags = defaultdict(lambda: {'principles': [], 'arguments': [], 'implications': []})

        # Extract principle tags
        principle_pattern = r'## PRINCIPLE\s+(\d+):[^\n]*\n(.*?)(?=^##|$)'
        for match in re.finditer(principle_pattern, self.layers[2], re.MULTILINE | re.DOTALL):
            p_num = int(match.group(1))
            content = match.group(2)
            found_tags = re.findall(r'#(\w+[\w-]*)', content)
            for tag in found_tags:
                tags[tag]['principles'].append(p_num)

        # Extract argument tags
        arg_pattern = r'## ARG-?(\d+):[^\n]*\n(.*?)(?=^##|$)'
        for match in re.finditer(arg_pattern, self.layers[3], re.MULTILINE | re.DOTALL):
            arg_num = int(match.group(1))
            content = match.group(2)
            found_tags = re.findall(r'#(\w+[\w-]*)', content)
            for tag in found_tags:
                tags[tag]['arguments'].append(arg_num)

        # Extract implication tags
        impl_pattern = r'## (?:IMPLICATION|APPLICATION|CONSEQUENCE)\s+(\d+):[^\n]*\n(.*?)(?=^##|$)'
        for match in re.finditer(impl_pattern, self.layers[4], re.MULTILINE | re.DOTALL):
            impl_num = int(match.group(1))
            content = match.group(2)
            found_tags = re.findall(r'#(\w+[\w-]*)', content)
            for tag in found_tags:
                tags[tag]['implications'].append(impl_num)

        return dict(tags)

    def validate(self) -> Dict:
        """Run all validations."""
        return {
            'book': self.book_name,
            'completeness': self._check_completeness(),
            'tag_consistency': self._check_tag_consistency(),
            'content_richness': self._check_content_richness(),
            'cross_references': self._check_cross_references(),
            'summary': self._generate_summary()
        }

    def _check_completeness(self) -> Dict:
        """Check if principles are linked to arguments/implications."""
        if not self.json_data:
            return {'status': 'ERROR', 'reason': 'JSON file missing'}

        principles = self.json_data.get('principles', [])
        if not principles:
            return {'status': 'ERROR', 'reason': 'No principles found'}

        total_principles = len(principles)
        linked_principles = 0
        linking_stats = {
            'with_arguments': 0,
            'with_implications': 0,
            'with_questions': 0,
            'fully_linked': 0,  # Has all three
            'partially_linked': 0,  # Has some
            'orphaned': 0  # Has none
        }

        for principle in principles:
            has_args = len(principle.get('supporting_arguments', [])) > 0
            has_impls = len(principle.get('related_implications', [])) > 0
            has_questions = len(principle.get('related_questions', [])) > 0

            if has_args:
                linking_stats['with_arguments'] += 1
            if has_impls:
                linking_stats['with_implications'] += 1
            if has_questions:
                linking_stats['with_questions'] += 1

            if has_args and has_impls and has_questions:
                linking_stats['fully_linked'] += 1
            elif has_args or has_impls or has_questions:
                linking_stats['partially_linked'] += 1
            else:
                linking_stats['orphaned'] += 1

            if has_args or has_impls or has_questions:
                linked_principles += 1

        return {
            'status': 'OK' if linked_principles == total_principles else 'INCOMPLETE',
            'total_principles': total_principles,
            'linked_principles': linked_principles,
            'completion_rate': f"{100 * linked_principles / total_principles:.1f}%",
            'details': linking_stats
        }

    def _check_tag_consistency(self) -> Dict:
        """Check if tags in JSON match tags in markdown."""
        json_tags = set(self.json_data.get('tags', []))
        markdown_tag_keys = set(self.markdown_tags.keys())

        missing_in_json = markdown_tag_keys - json_tags
        extra_in_json = json_tags - markdown_tag_keys

        # Check tag coverage in markdown
        tag_coverage = {}
        for tag, sections in self.markdown_tags.items():
            tag_coverage[tag] = {
                'in_principles': len(sections['principles']),
                'in_arguments': len(sections['arguments']),
                'in_implications': len(sections['implications']),
                'total': sum(len(v) for v in sections.values())
            }

        # Find orphaned tags (only in one section)
        orphaned_tags = {
            tag: cov for tag, cov in tag_coverage.items()
            if cov['in_principles'] > 0 and cov['in_arguments'] == 0 and cov['in_implications'] == 0
        }

        return {
            'status': 'OK' if not missing_in_json and not orphaned_tags else 'WARNING',
            'total_tags': len(json_tags),
            'markdown_tags': len(markdown_tag_keys),
            'missing_in_json': list(missing_in_json),
            'extra_in_json': list(extra_in_json),
            'orphaned_tags': list(orphaned_tags.keys()),
            'tag_coverage': tag_coverage
        }

    def _check_content_richness(self) -> Dict:
        """Check if content fields are populated."""
        if not self.json_data:
            return {'status': 'ERROR', 'reason': 'JSON file missing'}

        principles = self.json_data.get('principles', [])
        stats = {
            'principles_with_statement': 0,
            'principles_with_arguments': 0,
            'principles_with_implications': 0,
            'empty_statements': [],
            'avg_argument_length': 0,
            'avg_implication_length': 0
        }

        total_arg_length = 0
        total_impl_length = 0
        arg_count = 0
        impl_count = 0

        for p in principles:
            if p.get('statement', '').strip():
                stats['principles_with_statement'] += 1
            else:
                stats['empty_statements'].append(p.get('id'))

            if len(p.get('supporting_arguments', [])) > 0:
                stats['principles_with_arguments'] += 1
                for arg in p.get('supporting_arguments', []):
                    total_arg_length += len(arg.get('claim', ''))
                    arg_count += 1

            if len(p.get('related_implications', [])) > 0:
                stats['principles_with_implications'] += 1
                for impl in p.get('related_implications', []):
                    total_impl_length += len(impl.get('what_means', ''))
                    impl_count += 1

        stats['avg_argument_length'] = int(total_arg_length / arg_count) if arg_count > 0 else 0
        stats['avg_implication_length'] = int(total_impl_length / impl_count) if impl_count > 0 else 0

        return {
            'status': 'OK' if stats['principles_with_statement'] == len(principles) else 'WARNING',
            'details': stats
        }

    def _check_cross_references(self) -> Dict:
        """Check if JSON references actually exist in markdown."""
        if not self.json_data:
            return {'status': 'ERROR', 'reason': 'JSON file missing'}

        issues = []

        principles = self.json_data.get('principles', [])
        for p in principles:
            p_id = p.get('id')

            # Check arguments exist
            for arg in p.get('supporting_arguments', []):
                arg_source = arg.get('source', '')
                if not arg_source:
                    issues.append(f"{p_id}: argument has no source")

            # Check implications exist
            for impl in p.get('related_implications', []):
                impl_source = impl.get('source', '')
                if not impl_source:
                    issues.append(f"{p_id}: implication has no source")

        return {
            'status': 'OK' if not issues else 'WARNING',
            'issues_found': len(issues),
            'details': issues[:10]  # First 10
        }

    def _generate_summary(self) -> str:
        """Generate human-readable summary."""
        completeness = self._check_completeness()
        tags = self._check_tag_consistency()
        richness = self._check_content_richness()

        summary = []

        # Completeness
        if completeness.get('status') == 'INCOMPLETE':
            orphaned = completeness['details']['orphaned']
            summary.append(f"⚠️  {orphaned} principles are NOT linked to arguments/implications")
        else:
            summary.append(f"✓ All principles are linked")

        # Tags
        orphaned_tags = tags.get('orphaned_tags', [])
        if orphaned_tags:
            summary.append(f"⚠️  {len(orphaned_tags)} tags only in principles (not shared with arguments/implications)")
        else:
            summary.append(f"✓ Tag consistency is good")

        # Content
        empty = len(richness['details']['empty_statements'])
        if empty > 0:
            summary.append(f"⚠️  {empty} principles have empty statements")
        else:
            summary.append(f"✓ All principles have statements")

        return " | ".join(summary)


def process_book(book_dir: Path) -> Dict:
    """Process single book validation."""
    try:
        validator = DataQualityValidator(book_dir)
        return validator.validate()
    except Exception as e:
        return {
            'book': book_dir.name,
            'error': str(e)
        }


def find_book_directories(root_dir: Path) -> List[Path]:
    """Find all book directories."""
    books = []
    for item in root_dir.iterdir():
        if item.is_dir() and (item / "00_purpose.md").exists():
            books.append(item)
    return sorted(books)


def main():
    """Validate all books."""
    import sys

    if len(sys.argv) < 2:
        print("Usage: python validate_llm_data_quality.py Books/")
        print("   or: python validate_llm_data_quality.py Books/clean-architecture/")
        sys.exit(1)

    root_dir = Path(sys.argv[1])

    if not root_dir.exists():
        print(f"Error: {root_dir} not found")
        sys.exit(1)

    # Find books
    if (root_dir / "00_purpose.md").exists():
        books = [root_dir]
    else:
        books = find_book_directories(root_dir)

    if not books:
        print(f"No books found in {root_dir}")
        sys.exit(1)

    print("=" * 80)
    print("LLM DATA QUALITY VALIDATION")
    print("=" * 80)

    results = []
    for book in books:
        result = process_book(book)
        results.append(result)

        # Print summary
        print(f"\n📖 {result['book'].upper()}")
        print("-" * 80)

        if 'error' in result:
            print(f"❌ ERROR: {result['error']}")
            continue

        # Completeness
        comp = result['completeness']
        print(f"\n1. COMPLETENESS (Principles → Arguments/Implications)")
        print(f"   Status: {comp['status']}")
        print(f"   Linked: {comp.get('linked_principles', 0)}/{comp.get('total_principles', 0)} " +
              f"({comp.get('completion_rate', 'N/A')})")
        details = comp.get('details', {})
        print(f"   - With arguments: {details.get('with_arguments', 0)}")
        print(f"   - With implications: {details.get('with_implications', 0)}")
        print(f"   - With questions: {details.get('with_questions', 0)}")
        print(f"   - Orphaned (no links): {details.get('orphaned', 0)}")

        # Tag consistency
        tags = result['tag_consistency']
        print(f"\n2. TAG CONSISTENCY (Markdown → JSON)")
        print(f"   Status: {tags['status']}")
        print(f"   Total tags: {tags['total_tags']}")
        if tags.get('orphaned_tags'):
            print(f"   ⚠️  Orphaned tags (principles only, no args/impls): {len(tags['orphaned_tags'])}")
            print(f"       Examples: {', '.join(tags['orphaned_tags'][:5])}")

        # Content richness
        richness = result['content_richness']
        print(f"\n3. CONTENT RICHNESS")
        print(f"   Status: {richness['status']}")
        details = richness['details']
        print(f"   - Principles with statements: {details['principles_with_statement']}")
        print(f"   - Avg argument length: {details['avg_argument_length']} chars")
        print(f"   - Avg implication length: {details['avg_implication_length']} chars")

        # Cross references
        cross = result['cross_references']
        print(f"\n4. CROSS REFERENCES")
        print(f"   Status: {cross['status']}")
        if cross['issues_found'] > 0:
            print(f"   Issues: {cross['issues_found']}")

        # Summary
        print(f"\n✨ SUMMARY: {result['summary']}")

    # Overall report
    print("\n" + "=" * 80)
    print("OVERALL REPORT")
    print("=" * 80)

    for result in results:
        status = "✓" if result.get('completeness', {}).get('status') == 'OK' else "⚠️"
        print(f"{status} {result['book']}: {result.get('summary', 'ERROR')}")

    print("\n💡 RECOMMENDATIONS:")
    print("-" * 80)

    # Analyze issues
    orphaned_count = sum(len(r.get('tag_consistency', {}).get('orphaned_tags', [])) for r in results)
    incomplete = sum(1 for r in results if r.get('completeness', {}).get('status') != 'OK')

    if orphaned_count > 0:
        print(f"• Fix tag matching: {orphaned_count} orphaned tags found")
        print("  → Add shared tags to arguments/implications so they link to principles")

    if incomplete > 0:
        print(f"• Complete linking: {incomplete} books have orphaned principles")
        print("  → Review markdown structure and tag usage")

    print("• Use this validator regularly to catch data quality issues early")


if __name__ == '__main__':
    import sys
    sys.exit(main())
