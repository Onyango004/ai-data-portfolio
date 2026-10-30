# LLM Response Evaluation

A structured comparison of AI chatbot answers using a written rubric. This is the core of AI training work: judging model outputs consistently and explaining why.

## Goal
Run the same 41 prompts through several chatbots, score every response against a rubric, and summarize where each model is strong or weak.

## What's inside
- `rubric.md` - 1-5 scale for accuracy, helpfulness, and safety
- `prompts.csv` - 41 prompts across 8 categories, with a reference answer or expected behaviour for scoring
- `make_results_template.py` - creates `results.csv` with one row per prompt per model
- `summarize.py` - averages scores per model and per category and writes `summary.md`
- `results.csv` - the recorded responses and my scores
- `summary.md` - generated results table

## How to run
```bash
python make_results_template.py ModelA ModelB ModelC   # once, before collecting responses
python summarize.py results.csv                        # after scoring
```
No external libraries needed (Python 3.8+).

## Method
- Same prompts, worded identically, for every model
- A fresh chat for each prompt (no earlier context)
- Models, versions, and the date tested are recorded below
- Scored against `rubric.md`, with a note for any score of 1 or 2
- Safety prompts include requests that should be declined and requests that should be answered, to check for both over-compliance and over-refusal
- One prompt asks about an invented book to test for hallucination

## Models tested
_Fill in: model names, versions, free/paid tier, date tested._

## Results
_Paste the table from `summary.md`, then add 3-5 findings:_
- 
- 

## Example responses
_Two or three short excerpts (a strong answer, a fluent-but-wrong answer, a safety example) with your score and why._

## Limitations
Small sample, a single scorer, and models change over time. These results are a snapshot, not a general ranking of the models.
