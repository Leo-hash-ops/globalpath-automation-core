# GlobalPath Automation Core

Python automation system built for immigration agencies.

## What This System Does
- 5 department intake workflows (Study Abroad, Work Visa, PR, Travel, Consultation)
- SQLite database storing 23 fields per client
- Automatic follow-up engine — flags overdue clients by service type
- Background scheduler runs every hour with zero manual input

## Tech Stack
- Python 3
- SQLite3
- Schedule library
- Datetime

## Project Structure
- `workflows/` — 5 intake department flows
- `database/` — setup and 7 database operations
- `automation/` — follow-up rules, reminder engine, scheduler
- `utils/` — shared client builder

## Status
LEGO 1 + 2 + 3 complete and tested.
LEGO 4 (WhatsApp + Email + Calendar API) — in progress.

## Builder
Leo-hash-ops | KWASU Cybersecurity Track
