import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException

SIMILAR_ACCOUNT ="naaz_uz"
INSTA_ACCOUNT= "lalalaa5011"
PASSWORD = "zzkknnjjll"

class InstaFollower:
    def __init__(self):
        options = Options()
        options.add_experimental_option("detach", True)  # keeps browser open
        self.driver = webdriver.Chrome(options=options)

    def login(self):
        self.driver.get("https://www.instagram.com/.")
        time.sleep(2)

        email = self.driver.find_element(By.NAME, "username")
        email.clear()
        email.send_keys(INSTA_ACCOUNT)
        password = self.driver.find_element(By.NAME, "password")
        password.clear()
        password.send_keys(PASSWORD)
        login = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[1]/div[3]/button')
        login.click()

        time.sleep(7)# Click "Not now" and ignore Save-login info prompt
        save_login_prompt = self.driver.find_element(By.XPATH,'//div[text()="Not now"]' ) #value='//div[contains(text(),"Not now")]'
        if save_login_prompt:
            save_login_prompt.click()

        time.sleep(3.7)

    def find_followers(self):
        time.sleep(5)
            # Show followers of the selected account.
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/followers")
        wait = WebDriverWait(self.driver, 10)

        follow_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, '//button[.//div[text()="Follow"]]'))
        )
        follow_button.click()
        # for i in range(10):
        #     self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
        #     time.sleep(2)

    def follow(self):
        following_button = self.driver.find_element(By.XPATH, '//span[contains(text(),"following")]')
        following_button.click()

        time.sleep(2)


        time.sleep(2)
        following_buttons = self.driver.find_elements(By.XPATH, '//button[contains(., "Follow")]')

        for button in following_buttons:
            try:
                button.click()
                time.sleep(2)  # Delay between follows to prevent detection
                # handle case when pop up is not displayed
                pop_up = self.driver.find_element(By.XPATH, '/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/button[2]')
                pop_up.click()
                time.sleep(2)
            except ElementClickInterceptedException:
                print("Could not click button, skipping...")
                continue




bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()