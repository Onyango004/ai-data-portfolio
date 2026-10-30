# Annotation Guidelines: Sentiment (v1)

Label the overall sentiment the writer expresses toward the product, service, place, or situation.

| Label | Use when |
|---|---|
| positive | The writer is clearly satisfied, praising, thanking, or recommending |
| negative | The writer is clearly dissatisfied, complaining, or warning others |
| neutral | Facts only, questions, instructions, or no opinion expressed |
| skip | Text is unreadable or cannot be judged (excluded from agreement) |

## Edge cases
- **Sarcasm:** label the intended meaning ("Great, another update that breaks everything" = negative).
- **Mixed sentiment:** if one side clearly dominates, use it. If truly balanced, use neutral.
- **Mild praise** ("it's fine", "I guess it works", "not bad"): decide once and apply it consistently. Write your rule here after your first pass.
- **Facts with an implied opinion** ("Order arrived 3 weeks late"): negative.
- **Questions and requests** ("Does the app support...?", "Please send me the form"): neutral.
- **Other languages and code-switching:** label by meaning. Do not skip the sample because of language.
- **Business facts** (opening hours, prices, dates): neutral.

## Changelog
- v1: initial rules.
- v2: _add the rules you clarify after reviewing disagreements._
