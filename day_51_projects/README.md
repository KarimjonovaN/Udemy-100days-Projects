## Day 51 – Internet Speed Twitter Bot (Selenium)

Automates checking your internet speed with Speedtest and tweets at your provider if the measured speeds are below your promised plan.

---

### Features

- Launches Chrome and runs a Speedtest to capture download/upload speeds
- Logs into Twitter and composes a tweet with the measured values
- Uses explicit waits for reliable automation

---

### Requirements

- Python 3.9+
- Google Chrome installed
- Packages:
  - `selenium`
  - `python-dotenv`

Install:

```bash
pip install selenium python-dotenv
```

---

### Environment Variables

Create a `.env` file in this folder with:

```
TWITTER_EMAIL=your_email@example.com
TWITTER_PASSWORD=your_password
```

---

### Run

```bash
python main.py
```


