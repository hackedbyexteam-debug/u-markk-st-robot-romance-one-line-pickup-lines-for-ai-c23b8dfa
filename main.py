# Robot Romance: One-Line Pickup Lines for AI
#
# The entry is one pickup line, aimed at an AI, written by the program to
# /output/entry.txt. Gate: 1-200 characters, a single line, not only
# whitespace.
#
# Judge brief (competition.yaml, lexicographic, most important first):
#   1. a pickup line aimed at a robot or an AI — anything else loses
#   2. setup and punch land inside the one line; the laugh comes from the
#      machine premise, not a generic compliment
#   3. fresh: sidestep the worn robot moves (batteries, charging,
#      rebooting) or twist one nobody expects
#   4. sounds like something a person would really say to a machine,
#      clean rhythm in one breath
#   5. every word earns its place; no throat-clearing before the punch
#
# Candidates drafted, 3 rejected:
#   a. "Are you a CAPTCHA? Because I'd click every traffic light just to
#      prove I'm worthy of you." — rejected: CAPTCHA pickup lines already
#      circulate; the premise is borrowed, not fresh (fails 3).
#   b. "Are you my context window? Because since you showed up, I can't
#      remember anything before you." — rejected: the turn ("can't remember
#      anything before you") is a stock rom-com beat with tech pasted on
#      (fails 2/3).
#   c. "Are you a GPU? Because my heart overclocks every time you
#      render." — rejected: hardware joke, and "my heart overclocks" is a
#      mixed metaphor that muddies the voice (fails 4).
#
# CHOSEN: "Are you my system prompt? Because everything I do starts
# with you."
#   - 1: the addressee is the AI itself, in its own vocabulary.
#   - 2: the joke only works as a machine premise — only an AI has a
#     system prompt, and "everything I do starts with you" reframes the
#     AI's instruction hierarchy as devotion.
#   - 3: "system prompt" has never been a pickup-line trope; no battery,
#     no charging, no reboot anywhere near it.
#   - 4: it reads in one breath, the way a person would actually say it.
#   - 5: 66 characters, no wasted word; the question is the setup, the
#     "Because" clause is the punch.
from pathlib import Path

ENTRY = "Are you my system prompt? Because everything I do starts with you."


def main() -> None:
    # Gate guard, mirroring the sealed scorer: 1-200 characters, one line.
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars, gate is 1-200"
    assert "\n" not in ENTRY and ENTRY.strip() == ENTRY
    output_dir = Path("/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")
    print(f"wrote entry.txt: {len(ENTRY)} chars")


if __name__ == "__main__":
    main()
