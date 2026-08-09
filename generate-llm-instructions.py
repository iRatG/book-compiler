#!/usr/bin/env python3
"""
Generate llm_instructions.json from book layers (02_ideas, 03_reasoning, 04_consequences).

Usage:
    python generate-llm-instructions.py <book_path>

Example:
    python generate-llm-instructions.py Books/clean-architecture
"""

import json
import re
from pathlib import Path
from typing import Optional
import sys


def extract_metadata(book_path: Path) -> dict:
    """Extract book metadata from README or folder name."""
    readme_path = book_path / "README.md"

    # Infer title from folder name
    folder_name = book_path.name
    title = folder_name.replace("-", " ").title()
    author = "Unknown"

    if readme_path.exists():
        readme = readme_path.read_text(encoding='utf-8')
        # Try to extract title from first heading
        match = re.search(r'^#\s+(.+)$', readme, re.MULTILINE)
        if match:
            title = match.group(1)
        # Try to extract author
        match = re.search(r'(?:Author|by)\s*[:—]\s*(.+)$', readme, re.MULTILINE | re.IGNORECASE)
        if match:
            author = match.group(1).strip()

    return {
        "title": title,
        "author": author,
        "source_folder": str(book_path),
        "format_version": "1.0"
    }


def extract_tags(text: str) -> list:
    """Extract hashtags from text."""
    return list(set(re.findall(r'#[\w-]+', text)))


def parse_ideas(ideas_path: Path) -> list:
    """Parse 02_ideas.md and extract principles."""
    if not ideas_path.exists():
        return []

    content = ideas_path.read_text(encoding='utf-8')
    principles = []

    # Try different heading patterns (PRINCIPLE, ПРИНЦИП, ИДЕЯ, Глава, etc.)
    patterns = [
        r'^## (?:PRINCIPLE|ПРИНЦИП|ИДЕЯ|Глава|IDEA|CONCEPT) \d+[:\s]',
        r'^## \d+\. ',
        r'^## [A-Za-zА-Яа-яЁё]+'
    ]

    blocks = None
    for pattern in patterns:
        test_split = re.split(pattern, content, flags=re.MULTILINE)
        if len(test_split) > 2:  # Found separator
            blocks = test_split
            break

    if blocks is None:
        # Fallback: split by any level-2 heading
        blocks = re.split(r'^## ', content, flags=re.MULTILINE)

    for i in range(1, len(blocks)):
        principle_block = blocks[i]
        if not principle_block.strip():
            continue

        # Extract principle ID and statement
        lines = principle_block.strip().split('\n')
        statement = ""
        tags = []

        # First non-empty line is usually the title/statement
        for line in lines:
            if line.strip() and not line.startswith('#'):
                statement = line.strip()
                break

        # Extract tags
        tags = extract_tags(principle_block)

        # Create principle ID from first heading
        principle_id = f"principle_{i}".lower()

        principles.append({
            "id": principle_id,
            "principle": statement if statement else f"Principle {i}",
            "tags": tags,
            "raw_text": principle_block,
            "source": "ideas"
        })

    return principles


def parse_reasoning(reasoning_path: Path) -> list:
    """Parse 03_reasoning.md and extract arguments with examples."""
    if not reasoning_path.exists():
        return []

    content = reasoning_path.read_text(encoding='utf-8')
    reasoning_blocks = []

    # Try different heading patterns
    patterns = [
        r'^## (?:ARG|ARGUMENT|АРГУМЕНТ|ДОКАЗАТЕЛЬСТВО)-\d+[:\s]',
        r'^## \d+\. ',
        r'^## [A-Za-zА-Яа-яЁё]+'
    ]

    blocks = None
    for pattern in patterns:
        test_split = re.split(pattern, content, flags=re.MULTILINE)
        if len(test_split) > 2:
            blocks = test_split
            break

    if blocks is None:
        blocks = re.split(r'^## ', content, flags=re.MULTILINE)

    for i in range(1, len(blocks)):
        arg_block = blocks[i]
        if not arg_block.strip():
            continue
        tags = extract_tags(arg_block)

        reasoning_blocks.append({
            "id": f"arg_{i}",
            "tags": tags,
            "raw_text": arg_block,
            "source": "reasoning"
        })

    return reasoning_blocks


def parse_consequences(consequences_path: Path) -> list:
    """Parse 04_consequences.md and extract practical implications."""
    if not consequences_path.exists():
        return []

    content = consequences_path.read_text(encoding='utf-8')
    implications = []

    # Try different heading patterns
    patterns = [
        r'^## (?:IMPLICATION|СЛЕДСТВИЕ|ПРИМЕНЕНИЕ|APPLICATION)-\d+[:\s]',
        r'^## \d+\. ',
        r'^## [A-Za-zА-Яа-яЁё]+'
    ]

    blocks = None
    for pattern in patterns:
        test_split = re.split(pattern, content, flags=re.MULTILINE)
        if len(test_split) > 2:
            blocks = test_split
            break

    if blocks is None:
        blocks = re.split(r'^## ', content, flags=re.MULTILINE)

    for i in range(1, len(blocks)):
        impl_block = blocks[i]
        if not impl_block.strip():
            continue
        tags = extract_tags(impl_block)

        implications.append({
            "id": f"implication_{i}",
            "tags": tags,
            "raw_text": impl_block,
            "source": "consequences"
        })

    return implications


def extract_principle_details(principle_text: str) -> dict:
    """Extract reasoning and examples from principle text."""
    # Extract **Claim:**
    claim_match = re.search(r'\*\*(?:Claim|Statement):\*\*\s*(.+?)(?=\n\n|\*\*|\Z)', principle_text, re.DOTALL)
    claim = claim_match.group(1).strip() if claim_match else ""

    # Extract **Implication:** or **Why?:**
    implication_match = re.search(r'\*\*(?:Implication|Why):\*\*\s*(.+?)(?=\n\n|\*\*|\Z)', principle_text, re.DOTALL)
    implication = implication_match.group(1).strip() if implication_match else ""

    # Extract code blocks as examples
    examples = re.findall(r'```(?:\w+)?\n(.+?)\n```', principle_text, re.DOTALL)

    return {
        "claim": claim,
        "implication": implication,
        "examples": examples
    }


def generate_llm_instructions(book_path: str) -> dict:
    """Main function to generate complete llm_instructions.json."""
    book_path = Path(book_path)

    if not book_path.exists():
        raise ValueError(f"Book path not found: {book_path}")

    # Extract paths
    ideas_path = book_path / "02_ideas.md"
    reasoning_path = book_path / "03_reasoning.md"
    consequences_path = book_path / "04_consequences.md"

    # Extract metadata
    metadata = extract_metadata(book_path)

    # Parse all layers
    principles_raw = parse_ideas(ideas_path)
    reasoning_raw = parse_reasoning(reasoning_path)
    implications_raw = parse_consequences(consequences_path)

    # Build principle objects with details
    principles = []
    for principle in principles_raw:
        details = extract_principle_details(principle['raw_text'])
        principles.append({
            "id": principle["id"],
            "principle": principle["principle"],
            "reasoning": details.get("implication", details.get("claim", "")),
            "tags": principle["tags"],
            "key_rules": [],  # Will be populated from consequences
            "examples": [],  # Will be populated from reasoning
            "severity": "CRITICAL"
        })

    # Build FAQ from implications
    faq = []
    for impl in implications_raw:
        # Extract the first sentence as question
        lines = impl['raw_text'].strip().split('\n')
        if lines:
            what_line = lines[0]
            faq.append({
                "question": f"How should I apply: {what_line[:60]}...?",
                "answer": impl['raw_text'][:200] + "..."
            })

    # Assemble final structure
    result = {
        "metadata": metadata,
        "usage_instruction": f"Load this file at the start of a conversation. Reference principle IDs when making architectural decisions based on {metadata['title']}.",
        "system_instruction": f"You are guided by {metadata['title']} principles when making design decisions. Prioritize: minimizing cost of change, clarity, and long-term maintainability.",
        "principles": principles,
        "decision_workflows": [],
        "faq_for_llm": faq[:3]  # Limit to 3 FAQs
    }

    return result


def main():
    if len(sys.argv) < 2:
        print("Usage: python generate-llm-instructions.py <book_path>")
        print("Example: python generate-llm-instructions.py Books/clean-architecture")
        sys.exit(1)

    book_path = sys.argv[1]

    try:
        instructions = generate_llm_instructions(book_path)

        # Write to file
        output_path = Path(book_path) / "05_llm_instructions.json"
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(instructions, f, indent=2, ensure_ascii=False)

        print(f"[OK] Generated: {output_path}")
        print(f"  Principles: {len(instructions['principles'])}")
        print(f"  FAQ items: {len(instructions['faq_for_llm'])}")

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
