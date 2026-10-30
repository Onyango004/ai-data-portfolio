# Text Annotation & Inter-Annotator Agreement

An annotation project that mirrors real AI data work: label 200 text samples against written guidelines, label them a second time, then measure how consistent the labels are using Cohen's kappa, and refine the guidelines from the disagreements.

## Goal
Show that I can follow annotation guidelines, spot ambiguous cases, and measure labeling quality, not just label data.

## Data
200 short synthetic texts (customer reviews and support-style messages) in English, Kiswahili, and mixed English/Kiswahili. The texts were written with AI assistance to resemble real feedback; they are **not** real customer data. All labels were assigned by me.

## What's inside
- `annotation_guidelines.md` - label definitions and edge-case rules
- `data/pass1_labeling_sheet.csv` - the 200 texts for the first labeling pass
- `data/pass2_labeling_sheet.csv` - the same texts in a different order for the second pass
- `merge_passes.py` - joins the two sheets by id into `data/annotations.csv`
- `agreement.py` - percent agreement, Cohen's kappa, confusion matrix, and a list of disagreements

## How to run
```bash
python merge_passes.py     # after both sheets are labeled
python agreement.py        # prints the results and writes disagreements.csv
```
No external libraries needed (Python 3.8+).

## Method
1. Labeled all 200 texts using the guidelines (pass 1).
2. After a gap of at least a day, relabeled the shuffled sheet without looking at pass 1 (pass 2).
3. Computed agreement and reviewed every disagreement.
4. Updated the guidelines (v1 to v2) to fix the unclear rules. Original labels were not changed.

## Results
_Replace with your real numbers:_
- Samples compared: 
- Percent agreement: 
- Cohen's kappa: 
- Most common disagreement: 
- Language breakdown (English vs Kiswahili vs mixed), if you checked: 

## What I learned
_Two or three sentences: which cases were hardest, what rule you added, and what you would do differently._
