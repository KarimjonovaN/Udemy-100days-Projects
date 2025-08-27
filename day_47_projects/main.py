import os
from bs4 import BeautifulSoup
import requests
import smtplib
from dotenv import load_dotenv

load_dotenv()

practice_url ="https://appbrewery.github.io/instant_pot/"
live_url ="https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,ru;q=0.8"
}

response = requests.get(live_url, headers= header)
soup = BeautifulSoup(response.content, "html.parser")
print(soup.prettify())

price = soup.find(class_="a-offscreen").get_text()
without_currency = price.split("$")[1]
# print(without_currency)

float_price = float(without_currency)
print(float_price)


#SEND AN EMAIL
title = soup.find(id="productTitle").get_text().strip()
print(title)

TARGET_PRICE = 100

if float_price < TARGET_PRICE:
    message = f"{title} is on sale for {price}!!!"

    with smtplib.SMTP(os.environ["SMTP_ADDRESS"], port=587) as connection:
        connection.starttls()  # tls= Transport Layer Security
        connection.login(user= os.environ["MY_EMAIL"], password=os.environ["PASSWORD"])
        connection.sendmail(from_addr= os.environ["MY_EMAIL"],
                            to_addrs= "navruzakhon.karimjonova@gmail.com",
                            msg= f"Subject: Amazon Sale!\n\n{message}\n{live_url}".encode("utf-8")
                            )