# Bombay High Court Scraper

A web scraper for the **Bombay High Court** website. It downloads cause lists and case data — case details, parties, and orders — for structured analysis of court records that are otherwise only viewable one case at a time.

This scraper produced the dataset behind the study *[Do court vacations matter: evidence from the Bombay High Court](https://blog.theleapjournal.org/2024/09/do-court-vacations-matter-evidence-from.html)* (The Leap Blog, 2024).

## What it does

- Reads the court website's search options and sets case parameters.
- Walks cause lists and case tables for a given scope.
- Parses case details and saves structured output.
- Uses Selenium + ChromeDriver to drive the site.

## Setup

```bash
virtualenv bhc_scraper
source bhc_scraper/bin/activate
pip3 install -r requirements.txt
# install chromedriver (e.g. sudo apt-get install chromium-chromedriver)
```

See `DOC/documentation.md` for full setup notes and `DOC/project_plan.md` for design.

## Layout

```
SRC/
├── homepage.py            # entry / site landing
├── get_options.py         # read search options
├── set_case_params.py     # configure query params
├── parse_causelist.py     # walk cause lists
├── parse_case_details.py  # extract case details
├── save_case_table.py     # persist structured output
└── scraper.py             # orchestration
```
