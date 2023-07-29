# Challenge: Get hold of the total number of articles in Wikipedia main website
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
 
# Location of chromedriver:
chrome_driver_path = r"C:\Users\ahmad\Development\chromedriver.exe"
 
chrome_options = Options() #Create a Options class, necessarly to keep open the Chrome Browser
chrome_options.add_experimental_option("detach", True)
 
service = Service(executable_path=chrome_driver_path) #Create a Service class to handle the driver
driver = webdriver.Chrome(service=service, options=chrome_options)
 
driver.maximize_window() #This is just for maximize the window.

URL = "https://en.wikipedia.org/wiki/Main_Page"
driver.get(URL)

# total_articles = driver.find_element(by=By.CSS_SELECTOR, value="#articlecount a")
# print(total_articles.text)

# interacting with the website e.g. clicking a link
# total_articles.click()

# more_featured_articles = driver.find_element(by=By.LINK_TEXT, value="More featured articles")
# more_featured_articles.click()

# interacting with the website e.g. typing on a search bar and pressing enter like on the keyboard
search = driver.find_element(by=By.NAME, value="search")
# use method send_keys to type the string in the input field and press Enter
search.send_keys("Python", Keys.ENTER)


driver.quit()