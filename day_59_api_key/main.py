# request API from openweathermap.org using API key then use online JSON viewer: https://jsonviewer.stack.hu/
import requests
import pandas

# Call 5 day / 3 hour forecast data (Total 40 timestamps)
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast?"
MY_LATITUDE = 3.073838
MY_LONGITUDE = 101.518349
API_KEY = "5c1511bc746fb918893fe9821754b2cd"

parameters = {
    "lat": MY_LATITUDE,
    "lon": MY_LONGITUDE,
    "units": "metric",
    "appid": API_KEY
    }

# response = requests.get(url="https://api.openweathermap.org/data/2.5/weather", params=parameters)
response = requests.get(url=OWM_ENDPOINT, params=parameters)
# this line is for the response to raise an exception if there is an error status code (other than status code 200)
response.raise_for_status()
# the response can then be displayed as JSON format in terminal
weather_data = response.json()

will_rain = False

# attempt manually to do JSON parsing for the key "id" for the next 12 hours:
# weather_id_0 = weather_data["list"][0]["weather"][0]["id"]
# weather_id_1 = weather_data["list"][1]["weather"][0]["id"]
# weather_id_2 = weather_data["list"][2]["weather"][0]["id"]
# weather_id_3 = weather_data["list"][3]["weather"][0]["id"]
# print(weather_id_0, weather_id_1, weather_id_2, weather_id_3)
# if (weather_id_0 or weather_id_1 or weather_id_2 or weather_id_3) < 700:
#     will_rain = True


# attempt to use the python slice operator: 
# a[start:stop:step] --> start through not past stop, by step
# a[start:stop] --> items start through stop - 1
# a[start:] --> items start through the rest of the array
# a[:stop] --> items from the beginning through stop -1
# a[:] --> a copy of the whole array

# weather_slice = weather_data["list"][:4]
# for hour_data in weather_slice:
#     condition_code = hour_data["weather"][0]["id"]
#     if int(condition_code) < 700:
#         will_rain = True


# attempt: iterate over Pandas DataFrame
weather_dataframe = pandas.DataFrame(weather_data["list"][:4])
for (index, row) in weather_dataframe.iterrows():
    condition_code = row.weather[0]["id"]
    if int(condition_code) < 700:
        will_rain = True
# new_dict = {key:value for (key, value) in weather_dataframe}

if will_rain:
    print("Bring an umbrella.")
else:
    print("It will be sunny")