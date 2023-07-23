import requests, os
from dotenv import load_dotenv
from datetime import datetime
from datetime import timedelta
from pprint import pprint

load_dotenv()

today = datetime.now().date()
tomorrow = today + timedelta(days=1)
six_months_later = today + timedelta(days=30*6)
# tomorrow.strftime("%d/%m/%Y")
# six_months_later.strftime("%d/%m/%Y")

kiwi_api = os.environ.get("KIWI_API")
kiwi_endpoint = "https://api.tequila.kiwi.com/v2/search"
header = {
    "apikey": kiwi_api
    }
flight_search_parameters = {
    "fly_from": "KUL",
    "fly_to": "AUH",
    "date_from": "20/07/2023",
    "date_to": "20/08/2023",
    "curr": "MYR",
    }
    # "price_from": 1000,
    # "price_to": 5000

response = requests.get(url=kiwi_endpoint, headers=header, json=flight_search_parameters)
data = response.json()
print(data)


sheety_endpoint = os.environ.get("SHEETY_API_ENDPOINT")
# sheety_bearer_auth_token = os.environ.get("SHEETY_BEARER_AUTH_TOKEN")

# sheety_parameters = {
#     "price": {
#         "City": "",
#         "iataCode": "",
#         "lowestPrice": ""
#     }
# }
sheet_response = requests.get(url=sheety_endpoint)
sheet_data = sheet_response.json()
print(sheet_data)