"""Rule-based PII redaction for text files."""
import argparse
import re
import sys

# Order matters: more specific patterns run first.
PATTERNS = [
    ("EMAIL", re.compile(r"\b[\w.+-]+@[\w-]+(?:\.[\w-]+)+\b")),
    ("URL", re.compile(r"https?://\S+|www\.\S+")),
    ("NATIONAL_ID", re.compile(r"\bID(?:\s*(?:no\.?|number))?\s*[:#]?\s*\d{7,8}\b", re.I)),
    ("PHONE", re.compile(r"(?<!\w)(?:\+?254|0)[\s-]?[17]\d{2}[\s-]?\d{3}[\s-]?\d{3}(?!\d)")),
    ("IP", re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b")),
    ("NAME", re.compile(r"\b(?:Mr|Mrs|Ms|Miss|Dr|Prof)\.?\s+[A-Z][a-z]+(?:\s+[A-Z][a-z]+)?")),
]


def redact(text):
    """Return (redacted_text, counts_by_type)."""
    counts = {}
    for label, pattern in PATTERNS:
        text, n = pattern.subn(f"[{label}]", text)
        if n:
            counts[label] = n
    return text, counts


def main():
    parser = argparse.ArgumentParser(description="Mask PII in a text file or stdin.")
    parser.add_argument("input", nargs="?", help="input file (default: stdin)")
    parser.add_argument("-o", "--output", help="output file (default: stdout)")
    args = parser.parse_args()

    if args.input:
        with open(args.input, encoding="utf-8") as f:
            text = f.read()
    else:
        text = sys.stdin.read()

    redacted, counts = redact(text)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(redacted)
    else:
        print(redacted)

    summary = ", ".join(f"{k}: {v}" for k, v in counts.items()) or "nothing found"
    print(f"Redacted -> {summary}", file=sys.stderr)


if __name__ == "__main__":
    main()
