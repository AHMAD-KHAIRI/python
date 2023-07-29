# Challenge: Fill up form page and click sign up using Selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

URL = "http://secure-retreat-92358.herokuapp.com/"

# Location of chromedriver:
chrome_driver_path = r"C:\Users\ahmad\Development\chromedriver.exe"
 
chrome_options = Options() #Create a Options class, necessarly to keep open the Chrome Browser
chrome_options.add_experimental_option("detach", True)
 
service = Service(executable_path=chrome_driver_path) #Create a Service class to handle the driver
driver = webdriver.Chrome(service=service, options=chrome_options)
 
driver.maximize_window() #This is just for maximize the window.

driver.get(URL)

first_name = driver.find_element(by=By.NAME, value="fName")
first_name.send_keys("Abc")

last_name = driver.find_element(by=By.NAME, value="lName")
last_name.send_keys("Abc")

email = driver.find_element(by=By.NAME, value="email")
email.send_keys("abc@abc.com")

signup_button = driver.find_element(by=By.TAG_NAME, value="button")
signup_button.send_keys(Keys.ENTER)

# driver.quit()