import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
from dotenv import load_dotenv
from bs4 import BeautifulSoup
import requests

load_dotenv()
GOOGLE_FORM_LINK = os.environ["GOOGLE_FORM_LINK"]


# PART ONE -- FIND DATA USING BEAUTIFULSOUP

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,ru;q=0.8"
}

zillow_url = "https://appbrewery.github.io/Zillow-Clone/"
response = requests.get(zillow_url, headers= header)
soup = BeautifulSoup(response.content, "html.parser")
# print(soup.prettify())

all_addresses = [ ]
all_address_elements = soup.select(".StyledPropertyCardDataWrapper address")
for address in all_address_elements:
    text = address.get_text()
    text = text.replace("\n", "").replace("|", "").strip()
    all_addresses.append(text)
print(f"Addresses: {len(all_addresses)}")
print(all_addresses)


all_prices = [ ]
all_price_elements = soup.select(".PropertyCardWrapper span")
for price in all_price_elements:
    text = price.get_text()
    text = text.split("+")[0]
    text = text.split("/")[0]
    all_prices.append(text)
print(f"Prices: {len(all_prices)}")
print(all_prices)

all_links = [ ]
all_link_elements = soup.select(".StyledPropertyCardDataWrapper a")
for link in all_link_elements:
    link.get_text()
    all_links.append(link["href"])
print(f"Links: {len(all_links)}")
print(all_links)


# PART TWO -- FILL IN THE GOOGLE FORM WITH THE HELP OF SELENIUM

options = Options()
options.add_experimental_option("detach", True)  # keeps browser open
driver = webdriver.Chrome(options=options)

wait = WebDriverWait(driver, 10)

for i in range(len(all_addresses)):
    driver.get(GOOGLE_FORM_LINK)
    time.sleep(2)  #  wait to load form

    address_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    price_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')

    address_input.send_keys(all_addresses[i])
    price_input.send_keys(all_prices[i])
    link_input.send_keys(all_links[i])

    submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
    submit_button.click()

    time.sleep(2)












