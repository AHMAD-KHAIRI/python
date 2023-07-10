# console: pip install requests
import requests

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

# we can simply use the requests module:
response.raise_for_status()

# to get the actual data from the endpoint:
data = response.json()
# print(data)
# data = response.json()["iss_position"]
longitude = response.json()["iss_position"]["longitude"]
latitude = response.json()["iss_position"]["latitude"]
iss_position_tuple = (longitude, latitude)
print(iss_position_tuple)