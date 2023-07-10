import requests, smtplib, time
from datetime import datetime

# save my longitude and latitude position in a variable as CONSTANTS:
MY_LATITUDE = 3.073838
MY_LONGITUDE = 101.518349
# save my email info as CONSTANT for smtp:
MY_EMAIL = "ak.test.smtp.python@gmail.com"
MY_PASSWORD = "mghdwtncpaiajeeb"
TO_EMAIL = "khairihamzah85@gmail.com"

def is_iss_overhead():
    # request API from ISS endpoint:
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    # raise an exception if status code != 200:
    response.raise_for_status()
    # get the actual data from the endpoint and save it in a variable:
    data = response.json()
    # save the longitude and latitude in a variable:
    iss_longitude = float(data["iss_position"]["longitude"])
    iss_latitude = float(data["iss_position"]["latitude"])

    # check if my position is +/- 5 degrees of the iss position:
    if (MY_LATITUDE - 5) <= iss_latitude >= (MY_LATITUDE + 5) and (MY_LONGITUDE - 5) <= iss_longitude >= (MY_LONGITUDE + 5):
        return True

def is_it_night():
    # for the sunset and sunrise times API, we need to define the parameters:
    parameters = {
        "lat": MY_LATITUDE,
        "lng": MY_LONGITUDE,
        "formatted": 0
        }
    # request API from sunset and sunrise times API
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    # raise an exception if status code != 200:
    response.raise_for_status()
    # get the actual data from the endpoint:
    data = response.json()
    # save the sunrise/sunset hour in a variable:
    sunrise = int(data["results"]["sunrise"].split("T")[1].split("+")[0].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split("+")[0].split(":")[0])
    # check the time now (hour):
    time_now = datetime.now().hour
    # check if it is dark/night:
    if time_now >= sunset or time_now <= sunrise:
        return True

# loop continuously:
while True:
    # do a check every 60s
    time.sleep(60)
    # send an email to look up in the sky if it is dark and iss position is within range:
    if is_iss_overhead() and is_it_night():
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr= MY_EMAIL, 
                to_addrs=TO_EMAIL, 
                msg="Subject: The ISS is above you!\n\nLook up in the sky!"
                )