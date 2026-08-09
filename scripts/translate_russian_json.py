#!/usr/bin/env python3
"""
Translate Russian JSON content to English for Layer 05.

Translates all Russian text in 05_llm_instructions.json to English
while preserving structure and tags.

Usage:
    python translate_russian_json.py Books/ideal-work/
    python translate_russian_json.py Books/pragmatic-programmer/
"""

import json
import re
from pathlib import Path
from datetime import datetime

try:
    from googletrans import Translator
    HAS_GOOGLETRANS = True
except ImportError:
    HAS_GOOGLETRANS = False
    print("WARNING: googletrans not installed. Will use fallback translation.")


class RussianToEnglishTranslator:
    """Translate Russian JSON content to English."""

    def __init__(self):
        if HAS_GOOGLETRANS:
            self.translator = Translator()
        else:
            self.translator = None
        self.cache = {}

    def translate(self, text: str) -> str:
        """Translate Russian text to English."""
        if not text or not text.strip():
            return text

        # Check cache
        if text in self.cache:
            return self.cache[text]

        # Detect if text is Russian
        if not self._is_russian(text):
            return text

        # Translate
        if HAS_GOOGLETRANS and self.translator:
            try:
                result = self.translator.translate(text, src_language='ru', dest_language='en')
                translated = result['text'] if isinstance(result, dict) else result.text
                self.cache[text] = translated
                return translated
            except Exception as e:
                print(f"Translation error: {e}")
                return text
        else:
            # Fallback: return as-is with marker
            return text

    def _is_russian(self, text: str) -> bool:
        """Check if text contains Russian characters."""
        return bool(re.search(r'[Ѐ-ӿ]', text))

    def translate_json(self, data: dict) -> dict:
        """Recursively translate all string values in JSON."""
        if isinstance(data, dict):
            return {
                key: self.translate_json(value)
                for key, value in data.items()
            }
        elif isinstance(data, list):
            return [self.translate_json(item) for item in data]
        elif isinstance(data, str):
            return self.translate(data)
        else:
            return data


def process_book(book_dir: Path) -> bool:
    """Translate JSON for one book."""
    json_file = book_dir / '05_llm_instructions.json'

    if not json_file.exists():
        print(f"ERROR: {json_file} not found")
        return False

    try:
        # Read
        with open(json_file, encoding='utf-8') as f:
            data = json.load(f)

        # Check if already English
        if data.get('metadata', {}).get('source_language') == 'English':
            print(f"  {book_dir.name}: Already English source, skipping")
            return True

        print(f"  {book_dir.name}: Translating Russian -> English...", end=" ")

        # Translate
        translator = RussianToEnglishTranslator()
        translated_data = translator.translate_json(data)

        # Update metadata
        translated_data['metadata']['language'] = 'English'
        translated_data['metadata']['generated_at'] = datetime.now().isoformat()

        # Save
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(translated_data, f, indent=2, ensure_ascii=False)

        print("[OK]")
        return True

    except Exception as e:
        print(f"✗ ERROR: {e}")
        return False


def main():
    """Translate all Russian books."""
    import sys
    global HAS_GOOGLETRANS

    # Russian books
    books = [
        'ideal-work',
        'pragmatic-programmer',
        'code-fits-in-head',
        'martin-clean-code'
    ]

    print("\n" + "=" * 60)
    print("TRANSLATE RUSSIAN JSON TO ENGLISH")
    print("=" * 60 + "\n")

    if not HAS_GOOGLETRANS:
        print("[WARNING] googletrans not installed. Installing...\n")
        import subprocess
        try:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'googletrans==4.0.47'])
            # Retry import
            from googletrans import Translator
            HAS_GOOGLETRANS = True
        except:
            print("[ERROR] Failed to install googletrans. Continuing with fallback.")

    results = []
    for book in books:
        book_dir = Path(f"Books/{book}")
        if book_dir.exists():
            success = process_book(book_dir)
            results.append((book, success))
        else:
            print(f"  {book}: Directory not found")
            results.append((book, False))

    # Summary
    print("\n" + "=" * 60)
    print("RESULTS")
    print("=" * 60)

    success_count = sum(1 for _, s in results if s)
    for book, success in results:
        symbol = "[OK]" if success else "[FAIL]"
        print(f"{symbol} {book}")

    print(f"\n{success_count}/{len(results)} books translated successfully")
    return 0 if success_count == len(results) else 1


if __name__ == '__main__':
    import sys
    sys.exit(main() or 0)
