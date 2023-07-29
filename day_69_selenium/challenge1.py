# Challenge: Get hold of the upcoming events data from python.org website and store it in a dictionary

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
 
# Location of chromedriver:
chrome_driver_path = r"C:\Users\ahmad\Development\chromedriver.exe"
 
chrome_options = Options() #Create a Options class, necessarly to keep open the Chrome Browser
chrome_options.add_experimental_option("detach", True)
 
service = Service(executable_path=chrome_driver_path) #Create a Service class to handle the driver
driver = webdriver.Chrome(service=service, options=chrome_options)
 
driver.maximize_window() #This is just for maximize the window.

url1 = "https://www.python.org/"
driver.get(url1)

events_dates = []
upcoming_events_dates = driver.find_elements(by=By.CSS_SELECTOR, value=".event-widget time")
for date in upcoming_events_dates:
    events_dates.append(date.text)
print(events_dates)

events_names = []
upcoming_events_titles = driver.find_elements(by=By.CSS_SELECTOR, value=".event-widget .menu a")
for title in upcoming_events_titles:
    events_names.append(title.text)
print(events_names)

events_dict = {}
# the for loop way:
# for n in range (len(events_names)):
#     events_dict[n] = {
#         "time": events_dates[n],
#         "name": events_names[n],
#         }
# the dictionary comprehension way:
# new_dict = {new_key: new_value for (key, value) in dict.items()}
events_dict = { n: {"time": events_dates[n], "name": events_names[n]} for n in range(len(events_names))}
print(events_dict)

# events_dict = {
#     0: {
#         "time": "2023-07-29",
#         "name": "PythonCamp Leipzig"
#         },
#     1: {
#         "time": "2023-07-29",
#         "name": "PyCon PL 2023"
#         },
#         }
# new_dict = {index: for index in upcoming_events_dates}
# upcoming_events_dict = {date:event for (date, event) in }


driver.quit()
