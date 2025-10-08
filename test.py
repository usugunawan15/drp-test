#!/usr/bin/env python3
"""
create_test_file.py
Safe script: only creates a text file named 'test_output.txt'
containing the word 'testing'. No external dependencies.
"""

from pathlib import Path

def main():
    filename = Path("test_output.txt")
    content = "testing\n"

    # Tulis file baru atau timpa jika sudah ada
    filename.write_text(content, encoding="utf-8")
    print(f"✅ File created: {filename.resolve()}")
    print(f"   Content: {content.strip()}")

if __name__ == "__main__":
    main()
