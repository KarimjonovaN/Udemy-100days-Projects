import time
import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC

load_dotenv()

PROMISED_DOWN = 150
PROMISED_UP = 100
CHROME_DRIVER_PATH = ""
TWITTER_EMAIL = os.environ["TWITTER_EMAIL"]
TWITTER_PASSWORD =os.environ[ "TWITTER_PASSWORD"]

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(options=chrome_options)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        wait = WebDriverWait(self.driver, 60)

        time.sleep(2)
        start_button = self.driver.find_element(By.CSS_SELECTOR, value=".start-button a")
        start_button.click()

        time.sleep(30)
        download = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".download-speed"))).text
        upload = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".upload-speed"))).text

        self.down = download
        self.up = upload

    def tweet_provider(self):
        self.driver.get("https://twitter.com/login")
        wait = WebDriverWait(self.driver, 30)  # wait up to 30s for each element

        email_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="text"]')))
        email_input.clear()
        email_input.send_keys(TWITTER_EMAIL)

        next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Next']")))
        next_button.click()

        password_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="password"]')))
        password_input.clear()
        password_input.send_keys(TWITTER_PASSWORD)
        password_input.send_keys(Keys.ENTER)

        try:
            login_button = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-testid="LoginForm_Login_Button"]'))
            )
            login_button.click()
        except:
            pass  # sometimes Enter already logs in

        # --- TWEET BOX ---
        tweet_compose = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div[aria-label="What\'s happening?"]'))
        )

        tweet = (f"Hey Internet Provider, why is my internet speed "
                 f"{self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?")
        tweet_compose.send_keys(tweet)

        tweet_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-testid="tweetButtonInline"]')))
        tweet_button.click()
        self.driver.quit()


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
print(f"Download speed: {bot.down}")
print(f"Upload speed: {bot.up}")
bot.tweet_provider()