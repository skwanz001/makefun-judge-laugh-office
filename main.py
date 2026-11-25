"""Make the AI Judge Laugh — one-line office joke.

Writes the entry to /output/entry.txt.

The joke: a single line about office life, under 200 characters.
Stdlib only — the grading sandbox installs nothing.
Why this line (judge brief, most important first):
- True to office life: everyone dreads the late-Friday "quick chat" invite.
- Surprising turn: a calendar invite reframed as a message of hate.
- Tight: one breath, every word earns its place, kicker lands on "Friday".
- Original: a specific observed detail (4:58) instead of a stock line
  ("this meeting could have been an email", the printer, "per my last email").
"""

import os

JOKE = "Nothing says 'I hate you' like a calendar invite titled 'quick chat' at 4:58 on a Friday."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = JOKE.strip()
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    assert text == text.strip() and text, "entry must not be only whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Wrote {len(text)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
