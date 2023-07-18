import os, requests
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

app_id = os.environ.get("APP_ID")
api_key = os.environ.get("API_KEY")

# Required HEADERS when accessing Nutritionix V2 API endpoints:
# x-app-id: Your app ID issued from developer.nutritionix.com)
# x-app-key: Your app key issued from developer.nutritionix.com)

GENDER = "male"
WEIGHT_KG = 70
HEIGHT_CM = 165
AGE = 37

nutritionix_exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_text = input("Which exercise did you do today? ")

headers = {
    "x-app-id": app_id,
    "x-app-key": api_key
    }
exercise_parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
    }
response = requests.post(url=nutritionix_exercise_endpoint, headers=headers, json=exercise_parameters)
exercise_data = response.json()

# Sheety: Add a row to your sheet using post()
today = datetime.now()
date_today = today.strftime("%d/%m/%Y")
time_now = today.strftime("%H:%M:%S")

sheety_endpoint = os.environ.get("SHEETY_API_ENDPOINT")
sheety_bearer_auth_token = os.environ.get("SHEETY_BEARER_AUTH_TOKEN")

for exercise in exercise_data["exercises"]:
    add_row_parameters = {
        "workout": {
            "date": date_today,
            "time": time_now,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    headers = {
        "Authorization": f"Bearer {sheety_bearer_auth_token}"
        }
    sheety_response = requests.post(url=sheety_endpoint, json=add_row_parameters, headers=headers)
    print(sheety_response.text)