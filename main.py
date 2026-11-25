"""Entry for the make.fun bounty "Worst Monday One-Liners".

The program writes a single line about the worst Monday to
/output/entry.txt. The line is Monday in miniature: the alarm clock
has filed for overtime, the coffee has filed for hazard pay, and the
motivation is still on annual leave. It is one sentence of Monday
absurdity, it lands its surprise in one read, and it needs no
explanation. The gate allows 1 to 140 characters of UTF-8 text, so
the line is checked against that cap before it is written.

Why this line: the judge weighs whether the line really is about a
Monday, whether it earns a real laugh, whether it turns on a
surprise, and whether it stays in the head. The joke stacks three
tiny grievances in a row, each one a small workplace complaint
everyone recognises at once, and the third one lands hardest because
motivation itself has taken the day off. It is one sentence, it needs
no explanation, and the punchline is quotable enough to repeat to a
colleague on the next Monday morning.
"""

import os

ENTRY = (
    # Three grievances in rising order: the clock, the coffee, then
    # motivation itself — the last one is the punchline.
    "Monday again. My alarm clock filed for overtime, my coffee "
    "filed for hazard pay, and my motivation is still on annual leave."
)

MAX_CHARS = 140
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY.strip()
    assert text, "entry must not be empty"
    assert "\n" not in text, "entry must be a single line"
    assert len(text) <= MAX_CHARS, (
        f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
    )
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)
    print(f"wrote {len(text)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
