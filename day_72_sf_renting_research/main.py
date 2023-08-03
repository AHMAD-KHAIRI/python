# deprecated
# # ZILLOW_URL = "https://www.zillow.com/homes/for_rent/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.66026534033203%2C%22east%22%3A-122.20639265966797%2C%22south%22%3A37.61337875552385%2C%22north%22%3A37.93685032995972%7D%2C%22mapZoom%22%3A11%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D"

# Listing link: a class="property-card-link" data-test="property-card-link" --> href
# link = soup.find(name="a", attrs={"data-test": "property-card-link"})
# Address: a class="property-card-link" data-test="property-card-addr"
# Price: span data-test="property-card-price"

from bs4 import BeautifulSoup
import requests

GOOGLE_FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLScaYoVyqcOgC083J_XnGjKzafPUeBaj0WtkkTgiDGnfGl9-LQ/viewform?usp=sf_link"

PROPERTY_GURU_URL = "https://www.propertyguru.com.my/property-for-rent?listing_type=rent&market=residential&freetext=cybersouth&search=true"

response = requests.get(url=PROPERTY_GURU_URL)
website = response.text
soup = BeautifulSoup(website, "html.parser")


list_of_links = []
# <a class="nav-link" href="https://www.propertyguru.com.my/property-listing/cybersouth-for-rent-by-muhamad-haziq-38503942" title="For Rent - cybersouth" itemprop="url">cybersouth</a>
link = soup.find_all(name="a")
# link = soup.find_all(name="a", attrs={"title" : "For Rent - cybersouth"})
print(link)
# all_anchor_tags = soup.find_all(name="a")
# for tag in all_anchor_tags:
#     print(tag.get("href"))

list_of_addresses = []


list_of_prices = []

