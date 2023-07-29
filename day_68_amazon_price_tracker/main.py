import os
import requests
import smtplib
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

SENDER_EMAIL = os.environ.get("SENDER_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")
RECEIVER_EMAIL = os.environ.get("RECEIVER_EMAIL")


URL = "https://www.amazon.com/dp/B075CYMYK6"
header = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0",
    "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language" : "en-US, en;q=0.5",
    "Accept-Encoding" : "gzip, deflate, br",
    "upgrade-insecure-requests" : "1",
    "DNT":"1",
    "Connection":"close"
    }
parameters = {
    "ref_" : "cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6",
    "th" : 1
    }

response = requests.get(url=URL, headers=header, params=parameters)
amazon_website = response.text


soup = BeautifulSoup(amazon_website, "html.parser")
#   <span class="a-offscreen">$99.90</span>
find_price = soup.find(class_="a-offscreen").getText()
current_price = float(find_price.strip("$"))
print(current_price)

if current_price < 100:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=SENDER_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr= SENDER_EMAIL, 
            to_addrs=RECEIVER_EMAIL, 
            msg=f"Subject: Amazon Price Alert!\n\n The price for the item you wanted is now {current_price}.\nGet it now!"
            )