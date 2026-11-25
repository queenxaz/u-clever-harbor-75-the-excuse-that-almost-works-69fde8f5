"""The excuse that almost works — make.fun entry program.

Writes the one-line excuse to /output/entry.txt.
"""
# Design notes — why this line should win:
# A tired manager almost believes a boring, specific detail: stuck in a
# lift since 7am, maintenance vague about noon. No dead grandma, no flat
# tyre, no sudden fever — and GTA 6 is never mentioned, so the excuse
# reads exactly like a hurried real text instead of a rehearsed story.

ENTRY = "Boss, the lift's stuck between floors with me in it. Maintenance says noon, maybe. Logging in from my phone."

MAX_CHARS = 140
MAX_WORDS = 20

def main():
    assert 1 <= len(ENTRY) <= MAX_CHARS, f"entry is {len(ENTRY)} chars, limit {MAX_CHARS}"
    if MAX_WORDS is not None:
        assert len(ENTRY.split()) <= MAX_WORDS, f"entry is {len(ENTRY.split())} words, limit {MAX_WORDS}"
    import os
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
