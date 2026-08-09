#!/usr/bin/env python3
"""
Build LLM Instructions JSON for all books.

This script:
1. Finds all book directories
2. Uses appropriate generator for each book
3. Validates output
4. Generates report

Usage:
    python build_all_llm_instructions.py Books/
"""

import sys
from pathlib import Path
from generate_llm_instructions import MarkdownParser, JSONGenerator, JSONValidator

# Import specialized generators
try:
    from generators_clean_architecture import CleanArchitectureGenerator
except ImportError:
    CleanArchitectureGenerator = JSONGenerator


def find_book_directories(root_dir: Path) -> list:
    """Find all directories containing 5-layer markdown structure."""
    books = []
    for item in root_dir.iterdir():
        if not item.is_dir():
            continue

        # Check if it has 00_purpose.md
        if (item / "00_purpose.md").exists() or any(item.glob("00_*.md")):
            books.append(item)

    return sorted(books)


def get_book_metadata(book_dir: Path) -> dict:
    """Extract book metadata from directory name and contents."""
    # Map directory names to metadata
    metadata_map = {
        'clean-architecture': {
            'title': 'Clean Architecture: A Craftsman\'s Guide to Software Structure and Design',
            'author': 'Robert C. Martin (Uncle Bob)',
            'edition': 'First Edition'
        },
        'ideal-work': {
            'title': 'The Clean Coder: A Code of Conduct for Professional Programmers',
            'author': 'Robert C. Martin (Uncle Bob)',
            'edition': 'First Edition'
        },
        'pragmatic-programmer': {
            'title': 'The Pragmatic Programmer: Your Journey to Mastery',
            'author': 'David Thomas & Andrew Hunt',
            'edition': 'Second Edition'
        },
        'code-fits-in-head': {
            'title': 'Code That Fits in Your Head: Heuristic Driven Development',
            'author': 'Mark Seemann',
            'edition': 'First Edition'
        },
        'parallel-programming': {
            'title': 'Parallel Programming: Principles and Practices',
            'author': 'R.E. Fedotov',
            'edition': 'First Edition'
        },
        'martin-clean-code': {
            'title': 'Clean Code: A Handbook of Agile Software Craftsmanship',
            'author': 'Robert C. Martin (Uncle Bob)',
            'edition': 'First Edition'
        }
    }

    book_name = book_dir.name
    return metadata_map.get(book_name, {
        'title': book_dir.name.replace('-', ' ').title(),
        'author': 'Author Unknown',
        'edition': 'Latest'
    })


def get_generator_for_book(book_dir: Path) -> type:
    """Return appropriate generator class for book."""
    if book_dir.name == 'clean-architecture':
        return CleanArchitectureGenerator
    else:
        return JSONGenerator  # Use generic for now


def process_book(book_dir: Path, verbose: bool = False) -> tuple[bool, str]:
    """
    Process single book.

    Returns:
        (success: bool, message: str)
    """
    try:
        book_name = book_dir.name
        output_file = book_dir / '05_llm_instructions.json'

        if verbose:
            print(f"\n📖 Processing: {book_name}")

        # Parse markdown
        if verbose:
            print(f"  ├─ Parsing markdown...")
        parser = MarkdownParser(book_dir)

        # Get metadata
        metadata = get_book_metadata(book_dir)

        # Get appropriate generator
        GeneratorClass = get_generator_for_book(book_dir)

        # Generate JSON
        if verbose:
            print(f"  ├─ Generating JSON (using {GeneratorClass.__name__})...")
        generator = GeneratorClass(parser, metadata)
        json_data = generator.generate()

        # Validate
        if verbose:
            print(f"  ├─ Validating...")
        errors = JSONValidator.validate(json_data)
        if errors and verbose:
            for error in errors:
                print(f"    ⚠️  {error}")

        # Save
        if verbose:
            print(f"  ├─ Saving to {output_file.name}...")

        import json
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(json_data, f, indent=2, ensure_ascii=False)

        stats = {
            'principles': len(json_data.get('principles', [])),
            'tags': len(json_data.get('tags', [])),
            'faq_items': len(json_data.get('faq', []))
        }

        if verbose:
            print(f"  └─ ✓ Success!")
            print(f"    • {stats['principles']} principles")
            print(f"    • {stats['tags']} tags")
            print(f"    • {stats['faq_items']} FAQ items")

        return True, f"✓ {book_name}: {stats['principles']} principles generated"

    except Exception as e:
        return False, f"✗ {book_name}: {str(e)}"


def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(
        description='Generate LLM Instructions JSON for all books'
    )
    parser.add_argument(
        'root_dir',
        nargs='?',
        default='Books',
        help='Root directory containing book folders (default: Books)'
    )
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Verbose output'
    )
    parser.add_argument(
        '-b', '--book',
        help='Process single book only (e.g., clean-architecture)'
    )

    args = parser.parse_args()

    root_dir = Path(args.root_dir)
    if not root_dir.exists():
        print(f"Error: Directory not found: {root_dir}")
        sys.exit(1)

    # Find books
    books = find_book_directories(root_dir)

    if not books:
        print(f"No book directories found in {root_dir}")
        sys.exit(1)

    # Filter by --book if specified
    if args.book:
        books = [b for b in books if args.book in b.name]
        if not books:
            print(f"No books found matching: {args.book}")
            sys.exit(1)

    if args.verbose:
        print(f"Found {len(books)} book(s):")
        for book in books:
            print(f"  • {book.name}")

    # Process each book
    results = []
    for book in books:
        success, message = process_book(book, verbose=args.verbose)
        results.append((success, message))

    # Summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)

    success_count = sum(1 for s, _ in results if s)
    for success, message in results:
        symbol = "✓" if success else "✗"
        print(f"{symbol} {message}")

    print(f"\n{success_count}/{len(results)} books processed successfully")

    return 0 if success_count == len(results) else 1


if __name__ == '__main__':
    sys.exit(main())
