#!/usr/bin/env python3
"""
Simple translation using urllib + Google Translate web interface.
Faster fallback when googletrans fails.
"""

import json
import urllib.parse
import urllib.request
import re
import time
from pathlib import Path


def translate_text(text: str, timeout=5) -> str:
    """Translate Russian text to English using Google Translate web interface."""
    if not text or len(text) < 2:
        return text

    try:
        # URL encode
        text_encoded = urllib.parse.quote(text)
        url = f"https://translate.googleapis.com/translate_a/single?client=gtx&sl=ru&tl=en&dt=t&q={text_encoded}"

        # Simple request with timeout
        request = urllib.request.Request(
            url,
            headers={'User-Agent': 'Mozilla/5.0'}
        )
        response = urllib.request.urlopen(request, timeout=timeout)
        result = response.read().decode('utf-8')

        # Extract translation (format: [[[translated_text, original_text, ...]]])
        match = re.search(r'\[\[\["([^"]*)"', result)
        if match:
            return match.group(1)
        return text

    except Exception as e:
        print(f"    [Translation failed for short text, keeping original]")
        return text


def translate_json_recursive(data, depth=0):
    """Recursively translate all strings in JSON."""
    if isinstance(data, dict):
        result = {}
        for key, value in data.items():
            result[key] = translate_json_recursive(value, depth + 1)
        return result

    elif isinstance(data, list):
        return [translate_json_recursive(item, depth + 1) for item in data]

    elif isinstance(data, str):
        # Only translate if contains Cyrillic
        if not re.search(r'[Ѐ-ӿ]', data):
            return data

        # Show progress
        if depth < 3 and len(data) > 10:
            preview = data[:50] + "..." if len(data) > 50 else data
            print(f"      Translating: {preview}")

        # Translate
        translated = translate_text(data)
        time.sleep(0.2)  # Rate limit
        return translated

    else:
        return data


def process_book(book_dir):
    """Translate one book's JSON."""
    json_file = book_dir / '05_llm_instructions.json'

    if not json_file.exists():
        return False, "JSON not found"

    try:
        with open(json_file, encoding='utf-8') as f:
            data = json.load(f)

        # Check if already English source
        if data.get('metadata', {}).get('source_language') == 'English':
            return True, "Already English source"

        print(f"\n    Translating content...")
        data = translate_json_recursive(data)

        # Update metadata
        data['metadata']['language'] = 'English'

        # Save
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        return True, "Translated"

    except Exception as e:
        return False, str(e)


def main():
    """Translate all Russian books."""
    books = [
        'ideal-work',
        'pragmatic-programmer',
        'code-fits-in-head',
        'martin-clean-code'
    ]

    print("\n" + "=" * 70)
    print("TRANSLATE RUSSIAN JSON TO ENGLISH (using Google Translate web API)")
    print("=" * 70)

    results = []
    for book in books:
        book_dir = Path(f"Books/{book}")
        if book_dir.exists():
            print(f"\n  [{book}]", end="")
            success, msg = process_book(book_dir)
            results.append((book, success, msg))
            status = "[OK]" if success else "[FAIL]"
            print(f" {status} {msg}")
        else:
            results.append((book, False, "Directory not found"))

    # Summary
    print("\n" + "=" * 70)
    success_count = sum(1 for _, s, _ in results if s)
    print(f"RESULT: {success_count}/{len(results)} books translated")
    print("=" * 70 + "\n")

    return 0 if success_count == len(results) else 1


if __name__ == '__main__':
    import sys
    sys.exit(main())
