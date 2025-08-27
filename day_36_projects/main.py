from http.client import responses
import os
import requests
import smtplib
from _datetime import datetime
from twilio.rest import Client
from PIL.ImageChops import difference
from dotenv import load_dotenv

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = os.environ["STOCK_ENDPOINT"]
NEWS_ENDPOINT =os.environ["NEWS_ENDPOINT"]

TWILIO_AUTH_TOKEN = os.environ["TWILIO_AUTH_TOKEN"]
TWILIO_SID = os.environ["TWILIO_SID"]
STOKE_API_KEY = os.environ["STOKE_API_KEY"]
NEWS_API_KEY = os.environ["NEWS_API_KEY"]

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").


today = datetime.now()
today_tuple =(today.month, today.day)

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
stoke_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOKE_API_KEY
}
response = requests.get(STOCK_ENDPOINT, stoke_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key,value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)

#TODO 2. - Get the day before yesterday's closing stock price
day_before_yesterday_data =data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing_price)

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price)) #absolute value function
print(difference)

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
dif_percent = (difference/float(yesterday_closing_price)) * 100
print(dif_percent)

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").


    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
if dif_percent > 1:
    news_params= {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
    three_articles = articles[:3]
    print(three_articles)


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
    formatted_articles = [f"Headline: {article ['title']}.\nBrief: {article ['description']}" for article in three_articles]

    # message = "Stock News:\n\n" + "\n\n".join(formatted_articles)
    #
    # #TODO 9. - Send each article .
    # with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    #     connection.starttls()
    #     connection.login(user=MY_EMAIL, password=PASSWORD)
    #     connection.sendmail(
    #         from_addr=MY_EMAIL,
    #         to_addrs=MY_EMAIL,
    #         msg=message.encode("utf-8") # <-- Simple UTF-8 fix here
    #     )
    #     print("Email sent successfully!")

    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    # TODO 8. - Send each article as a separate message via Twilio.
    for article in formatted_articles:
        msg = f"{COMPANY_NAME}: {dif_percent}% \n {article}"
        message = client.messages.create(
            body=article[:10],
            from_=+17343367123,
            to= +4915226265953
        )
        print("message send")

#Optional TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

