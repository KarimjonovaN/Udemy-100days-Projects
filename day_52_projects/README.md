## Day 52 – Instagram Follower Bot (Selenium)

Automates logging into Instagram, navigating to a similar account's followers list, and attempting to follow accounts.

---

### Features

- Logs into Instagram with provided credentials
- Opens the followers list of a target account
- Clicks available "Follow" buttons with delays and basic interception handling

---

### Requirements

- Python 3.9+
- Google Chrome installed
- Packages:
  - `selenium`

Install:

```bash
pip install selenium
```

---

### Configure

Edit variables in `main.py`:

```
SIMILAR_ACCOUNT = "target_account"
INSTA_ACCOUNT = "your_username"
PASSWORD = "your_password"
```

---

### Run

```bash
python main.py
```

Note: Use responsibly and in accordance with Instagram's Terms of Service.


