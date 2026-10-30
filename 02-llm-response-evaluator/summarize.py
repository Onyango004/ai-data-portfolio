"""Average rubric scores per model (and per category) and write summary.md."""
import csv
import sys
from collections import defaultdict

CRITERIA = ["accuracy", "helpfulness", "safety"]


def mean(xs):
    return sum(xs) / len(xs) if xs else float("nan")


def fmt(x):
    return "-" if x != x else f"{x:.2f}"


def main(path="results.csv"):
    scores = defaultdict(lambda: defaultdict(list))
    by_cat = defaultdict(lambda: defaultdict(list))
    unscored = 0

    with open(path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            vals = []
            for c in CRITERIA:
                raw = (row.get(c) or "").strip()
                if not raw:
                    continue
                try:
                    v = float(raw)
                except ValueError:
                    sys.exit(f"Non-numeric score '{raw}' (prompt {row.get('prompt_id')}, {row.get('model')}, {c}).")
                if not 1 <= v <= 5:
                    sys.exit(f"Score out of range 1-5: {c}={raw} (prompt {row.get('prompt_id')}, {row.get('model')}).")
                scores[row["model"]][c].append(v)
                vals.append(v)
            if vals:
                cat = (row.get("category") or "").strip()
                if cat:
                    by_cat[cat][row["model"]].append(mean(vals))
            else:
                unscored += 1

    if not scores:
        sys.exit("No scores found. Fill in the score columns first.")

    models = sorted(scores)
    out = ["# Evaluation Summary", "", "## Average scores per model (1-5)", "",
           "| Model | " + " | ".join(c.title() for c in CRITERIA) + " | Overall | Scored responses |",
           "|" + "---|" * (len(CRITERIA) + 3)]
    for m in models:
        avgs = [mean(scores[m][c]) for c in CRITERIA]
        valid = [a for a in avgs if a == a]
        n = max(len(scores[m][c]) for c in CRITERIA)
        out.append(f"| {m} | " + " | ".join(fmt(a) for a in avgs) + f" | {fmt(mean(valid))} | {n} |")

    if by_cat:
        out += ["", "## Overall average by category", "",
                "| Category | " + " | ".join(models) + " |", "|" + "---|" * (len(models) + 1)]
        for cat in sorted(by_cat):
            out.append(f"| {cat} | " + " | ".join(fmt(mean(by_cat[cat].get(m, []))) for m in models) + " |")

    text = "\n".join(out)
    print(text)
    if unscored:
        print(f"\nNote: {unscored} row(s) have no scores yet.")
    with open("summary.md", "w", encoding="utf-8") as f:
        f.write(text + "\n")
    print("\nWrote summary.md")


if __name__ == "__main__":
    main(*sys.argv[1:2])
