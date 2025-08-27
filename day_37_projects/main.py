import os
import requests
from datetime import datetime
from dotenv import load_dotenv

TOKEN= os.environ["TOKEN"]
USERNAME = os.environ["USERNAME"]
GRAPH_ID = os.environ["GRAPH_ID"]


pixela_endpoint = os.environ["pixela_endpoint"]
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)


graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Gym Graph",
    "unit": "calory",
    "type": "int",
    "color": "kuro",
}
# authenticate the header
headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)


post_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
today = datetime.now()
# print(today.strftime("%Y%m%d"))
post_pixel = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "350",
}
# response = requests.post(url=post_pixel_endpoint, json=post_pixel, headers=headers)
# print(response.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime("%Y%m%d")}"

new_pixel_data = {
    "quantity": "300"
}
response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
print(response.text)
#
#
# delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime("%Y%m%d")}"

# response = requests.delete(url=post_pixel_endpoint, json=post_pixel, headers=headers)
# print(response.text)






