## Day 53 – Zillow Data to Google Form (BS4 + Selenium)

Scrapes listings from a Zillow-like site using BeautifulSoup, then opens a Google Form and submits each listing's address, price, and link via Selenium.

---

### Features

- HTTP fetch and parsing with `requests` and `BeautifulSoup`
- Extracts addresses, prices, and links from the page
- Automates Google Form submission for each listing

---

### Requirements

- Python 3.9+
- Google Chrome installed
- Packages:
  - `requests`
  - `beautifulsoup4`
  - `selenium`
  - `python-dotenv`

Install:

```bash
pip install requests beautifulsoup4 selenium python-dotenv
```

---

### Environment Variables

Create a `.env` file in this folder with:

```
GOOGLE_FORM_LINK=https://docs.google.com/forms/...
```

---

### Run

```bash
python main.py
```


