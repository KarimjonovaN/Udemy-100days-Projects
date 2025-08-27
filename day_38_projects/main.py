import requests
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()

GENDER = "Female"
WEIGHT_KG = "53"
HEIGHT_CM = "1.63"
AGE = "21"


APP_ID = os.environ.get("Tracking_Application_APP_ID")
print(APP_ID)
API_KEY =os.environ.get("Tracking_Application_API_KEY")
YOUR_TOKEN = os.environ.get("Tracking_Application_YOUR_TOKEN")

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = os.environ.get("Tracking_Application_SHEET_ENDPOINT")

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()

# step 4

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

bearer_headers = {
    "Authorization": f"Bearer {YOUR_TOKEN}"}

for exercise in result["exercises"]:
    print(exercise)
    sheet_inputs = {
        "sheet1": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
        }
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs, headers=bearer_headers)

    print(sheet_response.text)

