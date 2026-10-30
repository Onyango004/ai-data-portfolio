"""Join the two labeling sheets (matched by id) into data/annotations.csv."""
import csv
import sys

VALID = {"positive", "negative", "neutral", "skip"}


def read(path):
    out = {}
    with open(path, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            out[r["id"].strip()] = (r["text"], (r.get("label") or "").strip().lower())
    return out


def main(p1="data/pass1_labeling_sheet.csv", p2="data/pass2_labeling_sheet.csv",
         out="data/annotations.csv"):
    a, b = read(p1), read(p2)
    ids = sorted(a, key=int)
    problems = 0
    with open(out, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["id", "text", "label_pass1", "label_pass2"])
        for i in ids:
            text, l1 = a[i]
            l2 = b[i][1] if i in b else ""
            if i in b and b[i][0] != text:
                print(f"Warning: text differs for id {i} between the two sheets.")
            for name, label in (("pass 1", l1), ("pass 2", l2)):
                if not label:
                    print(f"Missing label: id {i} ({name})")
                    problems += 1
                elif label not in VALID:
                    print(f"Invalid label '{label}': id {i} ({name}). Use: {', '.join(sorted(VALID))}")
                    problems += 1
            w.writerow([i, text, l1, l2])
    print(f"\nWrote {len(ids)} rows to {out} ({problems} problem(s) to fix).")


if __name__ == "__main__":
    main(*sys.argv[1:4])
