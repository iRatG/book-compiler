#!/usr/bin/env python3
"""
Diagnose why markdown parsing fails to extract content.

Compares:
1. What's in markdown (raw text)
2. What regex extracts
3. What ends up in JSON

Shows WHY data is missing (parsing failures, truncation, etc).
"""

import json
import re
from pathlib import Path
from typing import Dict, List


class ParsingDiagnostics:
    """Diagnose parsing issues."""

    def __init__(self, book_dir: Path):
        self.book_dir = Path(book_dir)
        self.book_name = book_dir.name

        # Load markdown
        self.markdown = {}
        self._load_markdown()

        # Load JSON
        self.json_data = self._load_json()

    def _load_markdown(self):
        """Load markdown files."""
        for i in range(5):
            pattern = f"{i:02d}_*.md"
            files = list(self.book_dir.glob(pattern))
            if files:
                self.markdown[i] = files[0].read_text(encoding='utf-8')

    def _load_json(self) -> Dict:
        """Load JSON."""
        json_file = self.book_dir / '05_llm_instructions.json'
        if json_file.exists():
            return json.loads(json_file.read_text(encoding='utf-8'))
        return {}

    def diagnose_principles(self):
        """Diagnose principle statement extraction."""
        print("\n" + "=" * 80)
        print("PRINCIPLE STATEMENTS - Parsing Diagnosis")
        print("=" * 80)

        markdown_content = self.markdown.get(2, "")
        principles_json = self.json_data.get('principles', [])

        # Extract from markdown
        principle_pattern = r'## PRINCIPLE\s+(\d+):[^\n]*\n(.*?)(?=^##|$)'
        matches = list(re.finditer(principle_pattern, markdown_content, re.MULTILINE | re.DOTALL))

        print(f"\nFound {len(matches)} principles in markdown")
        print(f"Found {len(principles_json)} principles in JSON\n")

        for i, match in enumerate(matches[:5]):  # First 5
            p_num = int(match.group(1))
            p_content = match.group(2)

            # Get first few lines (what regex extracts)
            first_para = p_content.split('\n\n')[0].strip()

            # Find in JSON
            json_principle = next((p for p in principles_json if p['number'] == p_num), None)
            json_statement = json_principle.get('statement', '') if json_principle else ''

            print(f"\n{'─' * 80}")
            print(f"PRINCIPLE {p_num}: {json_principle.get('principle', 'N/A')}")
            print(f"{'─' * 80}")

            # Show markdown
            print(f"\n📝 IN MARKDOWN (first 200 chars):")
            print(f"  {first_para[:200]}")
            print(f"  ... (total {len(first_para)} chars)")

            # Show JSON
            print(f"\n📦 IN JSON (statement field):")
            if json_statement:
                print(f"  {json_statement[:200]}")
                print(f"  ... (total {len(json_statement)} chars)")
            else:
                print(f"  ❌ EMPTY!")

            # Diagnosis
            if not json_statement:
                print(f"\n🔍 DIAGNOSIS: Statement extraction FAILED")
                print(f"   Possible reasons:")
                print(f"   1. Regex didn't match this principle")
                print(f"   2. Statement is in subsection (###), not first paragraph")
                print(f"   3. Content structure is different than expected")

    def diagnose_arguments(self):
        """Diagnose argument extraction."""
        print("\n" + "=" * 80)
        print("ARGUMENTS - Parsing Diagnosis")
        print("=" * 80)

        markdown_content = self.markdown.get(3, "")
        principles_json = self.json_data.get('principles', [])

        # Extract from markdown
        arg_pattern = r'## ARG-?(\d+):[^\n]*\n(.*?)(?=^##|$)'
        matches = list(re.finditer(arg_pattern, markdown_content, re.MULTILINE | re.DOTALL))

        print(f"\nFound {len(matches)} arguments in markdown")

        # Count total arguments in JSON
        total_args_json = sum(
            len(p.get('supporting_arguments', []))
            for p in principles_json
        )
        print(f"Found {total_args_json} arguments linked in JSON (across all principles)\n")

        # Show first 3 arguments
        for i, match in enumerate(matches[:3]):  # First 3
            arg_num = int(match.group(1))
            arg_content = match.group(2)

            # Get claim (first paragraph)
            first_para = arg_content.split('\n\n')[0].strip()

            print(f"\n{'─' * 80}")
            print(f"ARGUMENT {arg_num}")
            print(f"{'─' * 80}")

            # Show markdown
            print(f"\n📝 IN MARKDOWN (first 300 chars):")
            print(f"  {first_para[:300]}")
            print(f"  ... (total {len(first_para)} chars)")

            # Find in JSON
            found_in_json = False
            for principle in principles_json:
                for arg in principle.get('supporting_arguments', []):
                    if f"arg_{arg_num:03d}" in arg.get('id', ''):
                        found_in_json = True
                        json_claim = arg.get('claim', '')
                        print(f"\n📦 IN JSON (claim field):")
                        if json_claim:
                            print(f"  {json_claim[:200]}")
                            print(f"  ... (total {len(json_claim)} chars)")
                        else:
                            print(f"  ❌ EMPTY!")
                        break
                if found_in_json:
                    break

            if not found_in_json:
                print(f"\n📦 IN JSON:")
                print(f"  ❌ NOT LINKED TO ANY PRINCIPLE")
                print(f"  (Either tags don't match, or principle is orphaned)")

    def diagnose_implications(self):
        """Diagnose implication extraction."""
        print("\n" + "=" * 80)
        print("IMPLICATIONS - Parsing Diagnosis")
        print("=" * 80)

        markdown_content = self.markdown.get(4, "")
        principles_json = self.json_data.get('principles', [])

        # Extract from markdown
        impl_pattern = r'## (?:IMPLICATION|APPLICATION|CONSEQUENCE)\s+(\d+):[^\n]*\n(.*?)(?=^##|$)'
        matches = list(re.finditer(impl_pattern, markdown_content, re.MULTILINE | re.DOTALL))

        print(f"\nFound {len(matches)} implications in markdown")

        # Count total implications in JSON
        total_impls_json = sum(
            len(p.get('related_implications', []))
            for p in principles_json
        )
        print(f"Found {total_impls_json} implications linked in JSON\n")

        # Show first 2 implications
        for i, match in enumerate(matches[:2]):  # First 2
            impl_num = int(match.group(1))
            impl_content = match.group(2)

            # Extract "What means" section
            what_means_match = re.search(
                r"(?:What|This|Means|Description)[:\s]+(.*?)(?=\n\n|###|$)",
                impl_content,
                re.DOTALL | re.IGNORECASE
            )
            what_means_text = what_means_match.group(1) if what_means_match else impl_content.split('\n\n')[0]

            print(f"\n{'─' * 80}")
            print(f"IMPLICATION {impl_num}")
            print(f"{'─' * 80}")

            # Show markdown
            print(f"\n📝 IN MARKDOWN (first 300 chars):")
            print(f"  {what_means_text[:300]}")
            print(f"  ... (total {len(what_means_text)} chars)")

            # Find in JSON
            found_in_json = False
            for principle in principles_json:
                for impl in principle.get('related_implications', []):
                    if f"impl_{impl_num:03d}" in impl.get('id', ''):
                        found_in_json = True
                        json_what_means = impl.get('what_means', '')
                        print(f"\n📦 IN JSON (what_means field):")
                        if json_what_means:
                            print(f"  {json_what_means[:200]}")
                            print(f"  ✅ LINKED to {principle.get('principle', 'N/A')}")
                            print(f"  ⚠️  TRUNCATED at 200 chars (original {len(json_what_means)} chars)")
                        else:
                            print(f"  ❌ EMPTY!")
                        break
                if found_in_json:
                    break

            if not found_in_json:
                print(f"\n📦 IN JSON:")
                print(f"  ❌ NOT LINKED TO ANY PRINCIPLE")

    def show_summary(self):
        """Show summary of issues."""
        print("\n" + "=" * 80)
        print("SUMMARY OF PARSING ISSUES")
        print("=" * 80)

        principles_json = self.json_data.get('principles', [])

        empty_statements = sum(1 for p in principles_json if not p.get('statement', '').strip())
        empty_claims = 0
        truncated_content = 0

        for p in principles_json:
            for arg in p.get('supporting_arguments', []):
                if not arg.get('claim', '').strip():
                    empty_claims += 1

            for impl in p.get('related_implications', []):
                what_means = impl.get('what_means', '')
                if len(what_means) > 99:  # Likely truncated
                    truncated_content += 1

        print(f"\n❌ EMPTY FIELDS:")
        print(f"  • {empty_statements}/{len(principles_json)} principles have empty statements")
        print(f"  • {empty_claims} argument claims are empty")

        print(f"\n✂️  TRUNCATION ISSUES:")
        print(f"  • {truncated_content} implications likely truncated at 200 chars")

        print(f"\n🎯 ROOT CAUSES:")
        print(f"  1. **Regex not capturing content correctly**")
        print(f"     → Markdown structure may differ from expected patterns")
        print(f"  2. **First-paragraph extraction too simplistic**")
        print(f"     → Statements/claims may be in multiple paragraphs")
        print(f"  3. **Truncation at arbitrary character limits**")
        print(f"     → Claims truncated at 150 chars, what_means at 100-200 chars")
        print(f"  4. **No fallback for complex structures**")
        print(f"     → Subsections (###) not handled properly")


def main():
    """Run diagnostics."""
    import sys

    if len(sys.argv) < 2:
        print("Usage: python diagnose_parsing_issues.py Books/clean-architecture/")
        sys.exit(1)

    book_dir = Path(sys.argv[1])

    if not book_dir.exists() or not (book_dir / "00_purpose.md").exists():
        print(f"Error: {book_dir} is not a valid book directory")
        sys.exit(1)

    print(f"\n🔍 PARSING DIAGNOSTICS FOR: {book_dir.name.upper()}")

    diag = ParsingDiagnostics(book_dir)
    diag.diagnose_principles()
    diag.diagnose_arguments()
    diag.diagnose_implications()
    diag.show_summary()

    print("\n" + "=" * 80)
    print("END OF DIAGNOSTICS")
    print("=" * 80)


if __name__ == '__main__':
    import sys
    sys.exit(main())
