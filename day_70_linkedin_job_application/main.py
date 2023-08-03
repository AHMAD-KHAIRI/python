import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

load_dotenv()

def click_signin():
    try:
        sign_in = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Sign in"))
            )
            # driver.find_element(By.LINK_TEXT, "Sign in"
    finally:
        sign_in.click()

def enter_username():
    ACCOUNT_EMAIL = os.environ.get("ACCOUNT_EMAIL")
    try:
        input_text_username = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "username"))
            )
        # driver.find_element(By.ID, "username")
    finally:
        input_text_username.send_keys(ACCOUNT_EMAIL)
        value = input_text_username.get_attribute("value")

def enter_password():
    ACCOUNT_PASSWORD = os.environ.get("ACCOUNT_PASSWORD")
    try:
        input_text_password = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "password"))
            )
        # driver.find_element(By.ID, "password")
    finally:
        input_text_password.send_keys(ACCOUNT_PASSWORD)
        input_text_password.send_keys(Keys.ENTER)


URL = "https://www.linkedin.com/jobs/search?keywords=Python%20Developer&location=Malaysia&geoId=106808692&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0"

# Location of chromedriver:
chrome_driver_path = r"C:\Users\ahmad\Development\chromedriver.exe"
 
chrome_options = Options() #Create a Options class, necessarily to keep open the Chrome Browser
chrome_options.add_experimental_option("detach", True)
 
service = Service(executable_path=chrome_driver_path) #Create a Service class to handle the driver
driver = webdriver.Chrome(service=service, options=chrome_options)
 
driver.maximize_window() #This is just for maximize the window.

driver.get(URL)
click_signin()
enter_username()
enter_password()
# driver.quit()
