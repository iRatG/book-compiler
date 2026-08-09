#!/usr/bin/env python3
"""Quick debug: why no linking between principles and arguments?"""

import json
from pathlib import Path

for book in ['ideal-work', 'pragmatic-programmer']:
    print(f"\n{'='*60}")
    print(f"{book.upper()}")
    print(f"{'='*60}")

    json_file = Path(f"Books/{book}/05_llm_instructions.json")
    with open(json_file, encoding='utf-8') as f:
        data = json.load(f)

    # Sample
    p = data['principles'][0]
    print(f"\nFirst Principle:")
    print(f"  Principle: {p['principle']}")
    print(f"  Tags: {p['tags']}")
    print(f"  Supporting args: {len(p['supporting_arguments'])}")
    print(f"  Related impls: {len(p['related_implications'])}")

    print(f"\nTotal arguments in book: {sum(len(p.get('supporting_arguments', [])) for p in data['principles'])}")
    print(f"Total implications in book: {sum(len(p.get('related_implications', [])) for p in data['principles'])}")

    # Debug: show metadata
    print(f"\nMetadata:")
    print(f"  Arguments count from quick_ref: {data['quick_reference'].get('arguments_count', 0)}")
    print(f"  Implications count from quick_ref: {data['quick_reference'].get('implications_count', 0)}")
