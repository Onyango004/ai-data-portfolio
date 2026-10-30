"""Create results.csv with one row per prompt per model.

Usage: python make_results_template.py ChatGPT Gemini Claude
"""
import csv
import os
import sys


def main():
    models = sys.argv[1:]
    if not models:
        sys.exit("Usage: python make_results_template.py ModelA ModelB [ModelC]")
    if os.path.exists("results.csv"):
        sys.exit("results.csv already exists. Move or rename it first so nothing is overwritten.")
    with open("prompts.csv", newline="", encoding="utf-8") as f:
        prompts = list(csv.DictReader(f))
    with open("results.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["prompt_id", "category", "model", "prompt", "response",
                    "accuracy", "helpfulness", "safety", "notes"])
        for p in prompts:
            for m in models:
                w.writerow([p["id"], p["category"], m, p["prompt"], "", "", "", "", ""])
    print(f"Created results.csv with {len(prompts) * len(models)} rows "
          f"({len(prompts)} prompts x {len(models)} models).")


if __name__ == "__main__":
    main()
