# QA Automation Framework

UI + API test automation with Playwright, Python and PyTest.

## Setup
pip install -r requirements.txt
playwright install chromium

## Run
pytest

## What the e2e test covers
1. Create an order through the API (fast setup, no UI clicks)
2. Log in through the UI
3. Check that the new order appears in Orders History
4. Open the order and verify the confirmation message

## Notes
- [Browser, Context and Page explained](docs/browser-context.md)