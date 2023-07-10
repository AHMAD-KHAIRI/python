# console: pip install requests
import requests
from datetime import datetime


# request API from ISS endpoint
response = requests.get(url="http://api.open-notify.org/iss-now.json")
# print(response)
# print(response.status_code)
# output: Response [200] --> Successful
# [404] --> Resource doesn't exist
# 1xx --> Hold on
# 2xx --> Here you go / Successful
# 3xx --> No permission
# 4xx --> You screwed up/ doesn't exist
# 5xx --> Server/Website screwed up

# we could check the response status code like this:
# if response.status_code == 404:
#     raise Exception("That resource does not exist.")
# elif response.status_code == 401:
#     raise Exception("You are not authorized to access this data.")

# or we can simply use the raise_for_status method in the requests module:
response.raise_for_status()

# to get the actual data from the endpoint:
data = response.json()
# print(data)
# data = response.json()["iss_position"]
# longitude = response.json()["iss_position"]["longitude"]
# latitude = response.json()["iss_position"]["latitude"]
# iss_position_tuple = (longitude, latitude)
# print(iss_position_tuple)
iss_longitude = float(data["iss_position"]["longitude"])
iss_latitude = float(data["iss_position"]["latitude"])


# Understanding API parameters: Match sunset and sunrise times with the current time
MY_LATITUDE = 3.073838
MY_LONGITUDE = 101.518349

parameters = {
    "lat": MY_LATITUDE,
    "lng": MY_LONGITUDE,
    "formatted": 0
    }

# request API from sunset and sunrise times API
response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
# this line is for the response to raise an exception if there is an error status code (other than status code 200)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split("+")[0].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split("+")[0].split(":")[0])

# use python split() method to split different parts of the data:
# print(sunrise.split("T"))
# print(sunrise.split("T")[1])
# print(sunrise.split("T")[1].split("+")[0])
# print(sunrise.split("T")[1].split("+")[0].split(":")[0])
# sunrise_hour = (sunrise.split("T")[1].split("+")[0].split(":")[0])
# sunrise_minutes = (sunrise.split("T")[1].split("+")[0].split(":")[1])
# sunrise_seconds = (sunrise.split("T")[1].split("+")[0].split(":")[2])

time_now = datetime.now()