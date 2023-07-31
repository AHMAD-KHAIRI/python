from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

URL = "http://orteil.dashnet.org/experiments/cookie/"

def click_cookie_for_five_seconds():
    clicker = True
    start_time = time.time() + 5
    while clicker:
        cookie.click()
        if (start_time - time.time()) < 0:
            clicker = False

def buy_upgrade():
    items = driver.find_elements(By.CSS_SELECTOR, "#store > div:not(.grayed)")
    items[-1].click()


# Location of chromedriver:
chrome_driver_path = r"C:\Users\ahmad\Development\chromedriver.exe"
 
chrome_options = Options() #Create a Options class, necessarily to keep open the Chrome Browser
chrome_options.add_experimental_option("detach", True)
 
service = Service(executable_path=chrome_driver_path) #Create a Service class to handle the driver
driver = webdriver.Chrome(service=service, options=chrome_options)
 
driver.maximize_window() #This is just for maximize the window.

driver.get(URL)

cookie = driver.find_element(by=By.ID, value="cookie")

end = time.time() + 300 # ends after 5 minutes
while time.time() < end:
    click_cookie_for_five_seconds()
    buy_upgrade()

time.sleep(2)
score = float(driver.find_element(By.ID, "cps").text.split(" : ")[1])
print(f"Your score is {score} cookies/second.")