"""Compute inter-annotator agreement between two labeling passes."""
import csv
import os
import sys
from collections import Counter


def cohens_kappa(a, b):
    """Return (kappa, observed_agreement) for two equal-length label lists."""
    n = len(a)
    observed = sum(x == y for x, y in zip(a, b)) / n
    ca, cb = Counter(a), Counter(b)
    expected = sum((ca[l] / n) * (cb[l] / n) for l in set(a) | set(b))
    if expected == 1:
        return (1.0 if observed == 1 else 0.0), observed
    return (observed - expected) / (1 - expected), observed


def interpret(k):
    """Landis & Koch (1977) interpretation bands."""
    if k < 0:
        return "worse than chance"
    for limit, name in [(0.2, "slight"), (0.4, "fair"), (0.6, "moderate"),
                        (0.8, "substantial"), (1.01, "almost perfect")]:
        if k <= limit:
            return name


def main(path="data/annotations.csv"):
    if not os.path.exists(path):
        sys.exit(f"{path} not found. Label both sheets, then run merge_passes.py first.")

    rows = []
    with open(path, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            l1, l2 = r["label_pass1"].strip().lower(), r["label_pass2"].strip().lower()
            if l1 and l2 and "skip" not in (l1, l2):
                rows.append((r["id"], r["text"], l1, l2))

    if not rows:
        sys.exit("No complete rows found. Check your column names and labels.")

    a = [r[2] for r in rows]
    b = [r[3] for r in rows]
    kappa, observed = cohens_kappa(a, b)

    print(f"Samples compared:   {len(rows)}")
    print(f"Percent agreement:  {observed:.1%}")
    print(f"Cohen's kappa:      {kappa:.3f} ({interpret(kappa)})")

    labels = sorted(set(a) | set(b))
    print("\nConfusion matrix (rows = pass 1, columns = pass 2):")
    print(" " * 10 + "".join(f"{l:>10}" for l in labels))
    for l1 in labels:
        print(f"{l1:<10}" + "".join(
            f"{sum(1 for x, y in zip(a, b) if x == l1 and y == l2):>10}" for l2 in labels))

    diffs = [r for r in rows if r[2] != r[3]]
    confusions = Counter((r[2], r[3]) for r in diffs)
    print("\nMost common disagreements (pass1 -> pass2):")
    for (x, y), c in confusions.most_common(5):
        print(f"  {x} -> {y}: {c}")

    with open("disagreements.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["id", "text", "label_pass1", "label_pass2"])
        w.writerows(diffs)
    print(f"\nWrote {len(diffs)} disagreements to disagreements.csv")


if __name__ == "__main__":
    main(*sys.argv[1:2])
