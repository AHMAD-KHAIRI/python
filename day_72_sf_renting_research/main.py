# deprecated
# # ZILLOW_URL = "https://www.zillow.com/homes/for_rent/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.66026534033203%2C%22east%22%3A-122.20639265966797%2C%22south%22%3A37.61337875552385%2C%22north%22%3A37.93685032995972%7D%2C%22mapZoom%22%3A11%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D"

# Listing link: a class="property-card-link" data-test="property-card-link" --> href
# link = soup.find(name="a", attrs={"data-test": "property-card-link"})
# Address: a class="property-card-link" data-test="property-card-addr"
# Price: span data-test="property-card-price"

# STEP 1: Scrape data using BeautifulSoup and requests

from bs4 import BeautifulSoup
import requests

PROPERTY_GURU_URL = "https://www.propertyguru.com.my/property-for-rent"

headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0",
    "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language" : "en-US, en;q=0.5",
    "Accept-Encoding" : "gzip, deflate, br",
    "upgrade-insecure-requests" : "1",
    "DNT":"1",
    "Connection":"close"
    }

parameters = {
    "listing_type": "rent",
    "market" : "residential",
    "freetext" : "cybersouth",
    "search" : "true"
    }

response = requests.get(url=PROPERTY_GURU_URL, headers=headers, params=parameters)
response.raise_for_status()
website = response.text
soup = BeautifulSoup(website, "html.parser")


list_of_links = []
all_anchor_tags = soup.find_all(name="a")
for tag in all_anchor_tags:
    print(tag.get("href"))

list_of_addresses = []
# list comprehension: new_list = [new_item for item in list]

list_of_prices = []
# list comprehension: new_list = [new_item for item in list]

# new_dict = {new_key: new_value for (key, value) in dict.items()}
new_dict = { n: {"address": list_of_addresses[n], "price": list_of_prices[n], "link": list_of_links[n]} for n in range(len(list_of_addresses))}
# print(new_dict)


# STEP 2: Use Selenium to fill up Google form
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os, time
from dotenv import load_dotenv

load_dotenv()

chrome_driver_path = r"C:\Users\ahmad\Development\chromedriver.exe" # Location of chromedriver:
 
chrome_options = Options() # Create an Options class, necessarily to keep open the Chrome Browser
chrome_options.add_experimental_option("detach", True)
 
service = Service(executable_path=chrome_driver_path) # Create a Service class to handle the driver
driver = webdriver.Chrome(service=service, options=chrome_options)
 
driver.maximize_window() #This is just to maximize the window.

GOOGLE_FORM_URL = os.environ.get("GOOGLE_FORM_URL")
driver.get(GOOGLE_FORM_URL)

def fill_address(n):
    try:
        address_of_property = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".Xb9hP input "))
            )
    # address_of_property = driver.find_element(By.CSS_SELECTOR, ".Xb9hP input ")
    finally:        
        address_of_property.send_keys(list_of_addresses[n])

def fill_price():
    try:
        price_of_property = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.Qr7Oae:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)"))
            )
    # price_of_property = driver.find_element(By.CSS_SELECTOR, "div.Qr7Oae:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)")
    finally:
        price_of_property.send_keys(list_of_prices[0])

def fill_link():
    try:
        link_of_property = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.Qr7Oae:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)"))
            )
    # link_of_property = driver.find_element(By.CSS_SELECTOR, "div.Qr7Oae:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)")
    finally:
        link_of_property.send_keys(list_of_links[0])

def click_submit():
    try:
        submit_btn = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".Y5sE8d > span:nth-child(3) > span:nth-child(1)"))
            )
    finally:
        submit_btn.click()

def fill_another_form():
    pass

for key, value in new_dict.items():
    address = value["address"]
    print(address)
    # fill_address(address)

    price = value["price"]
    # fill_price(price)
    
    link = value["link"]
    # fill_link(link)
    
    click_submit()
    fill_another_form()

driver.quit()