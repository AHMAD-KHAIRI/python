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
 
# url = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
# driver.get(url)

# price = driver.find_element(by=By.CLASS_NAME, value="a-price-whole")
# price = driver.find_element(by=By.CLASS_NAME, value="a-offscreen")
# print(price.text)

url1 = "https://www.python.org/"
driver.get(url1)

search_bar = driver.find_element(by=By.NAME, value="q")
print(search_bar) # outputs a selenium element: <selenium.webdriver.remote.webelement.WebElement (session="92acf5a2824bb591e29e149b085be776", element="A73FAFBA33798BC5A2DBE9C38BAF2DB9_element_6")>
print(search_bar.tag_name) # outputs the tag name : input
print(search_bar.get_attribute("placeholder")) # outputs the content inside the attribute

logo = driver.find_element(by=By.CLASS_NAME, value="python-logo")
print(logo.size) # output: {'height': 82, 'width': 290}

doc_link = driver.find_element(by=By.CSS_SELECTOR, value=".documentation-widget a")
print(doc_link.text)

# XPath - a way of locating a specific HTML element by a path structure
bug_link = driver.find_element(by=By.XPATH, value="/html/body/div/footer/div[2]/div/ul/li[3]/a")
print(bug_link.text)



# driver.close() # close() closes a single tab
driver.quit() # quit() closes the entire browser