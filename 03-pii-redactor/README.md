# PII Redactor

A lightweight command-line tool that finds and masks personally identifiable
information (PII) in text datasets before they are shared or used for AI training.

## Goal
Show practical data-privacy awareness: AI training data often contains personal
details, and they need to be removed or masked safely.

## What it detects
| Type | Example | Replaced with |
|---|---|---|
| Email | jane@example.com | `[EMAIL]` |
| Phone (Kenya formats) | 0712 345 678, +254 712 345 678 | `[PHONE]` |
| National ID (when labeled) | ID No: 12345678 | `[NATIONAL_ID]` |
| IP address | 192.168.1.10 | `[IP]` |
| URL | https://example.com/x | `[URL]` |
| Titled names | Dr. Achieng, Mr Otieno Kamau | `[NAME]` |

## How to run
```bash
python redact.py sample_input.txt -o sample_output.txt
echo "Call 0712 345 678" | python redact.py
python -m unittest test_redact.py -v
```
No external libraries needed (Python 3.8+).

## Limitations (important)
- Rule-based: it will miss names without a title and unusual formats.
- Bare 8-digit numbers are only treated as IDs when labeled "ID".
- Not a substitute for human review on sensitive datasets.

## Next steps
- Add an NER model (spaCy) for names and places
- Add a CSV mode that redacts specific columns
- Log counts per PII type for a redaction report

## Security note
Test only with fake data. Never commit real personal information to GitHub.
