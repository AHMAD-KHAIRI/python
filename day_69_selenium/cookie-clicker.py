from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

URL = "http://orteil.dashnet.org/experiments/cookie/"

# Location of chromedriver:
chrome_driver_path = r"C:\Users\ahmad\Development\chromedriver.exe"
 
chrome_options = Options() #Create a Options class, necessarily to keep open the Chrome Browser
chrome_options.add_experimental_option("detach", True)
 
service = Service(executable_path=chrome_driver_path) #Create a Service class to handle the driver
driver = webdriver.Chrome(service=service, options=chrome_options)
 
driver.maximize_window() #This is just for maximize the window.

driver.get(URL)

# find the cookie
cookie = driver.find_element(by=By.ID, value="cookie")

time_now = time.time()
print(time_now)
# timeout = 10 # in seconds

# while time_now < time_now + timeout:
    # click on the cookie
    # cookie.click()    

# find the money (cookies)
# money = driver.find_element(by=By.ID, value="money")
# print(money.text)