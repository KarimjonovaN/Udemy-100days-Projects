## Day 49 Projects – Selenium Gym Class Booker

Automates logging into the sample Gym site and booking Tuesday/Thursday 6:00 PM classes, then verifies bookings on the My Bookings page.

---

## Features

- Browser automation with Selenium (Chrome)
- Explicit waits using `WebDriverWait` and Expected Conditions
- Element location via CSS selectors, XPaths, and IDs
- Booking flow with status handling (Booked / Waitlisted)
- Verification step against the My Bookings page
- Chrome profile persistence via `--user-data-dir`

---

## How to Run

- Ensure Google Chrome is installed.
- Install dependencies:
  - `pip install selenium webdriver-manager`
- Run:
  - `python main.py`

Note: The script uses a local Chrome user data directory (`chrome_profile`) to persist session data.


