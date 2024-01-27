import os, requests, smtplib
from dotenv import load_dotenv

# load python environment variable
load_dotenv()

SENDER_EMAIL = os.environ.get("SENDER_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")
RECEIVER_EMAIL = os.environ.get("RECEIVER_EMAIL")

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

# https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=IBM&apikey=demo
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
# https://newsapi.org/v2/everything?q=Apple&from=2023-07-16&sortBy=popularity&apiKey=API_KEY
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

AV_API_KEY = os.environ.get("AV_API_KEY")
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")

stock_parameters = {
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK_NAME,
    "interval":"5min",
    "apikey": AV_API_KEY
    }

news_parameters = {
    "q": COMPANY_NAME,
    "from":"2024",
    "apiKey": NEWS_API_KEY
    }


# STEP 1: fetch data from alphavantage Api
response = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)
response.raise_for_status()
stock_data = response.json()["Time Series (Daily)"]

# TODO 1. Get yesterday's closing stock price
# yesterdays_closing_price = float(stock_data["Time Series (Daily)"]["2023-07-14"]["4. close"])
stock_list = [value for (key, value) in stock_data.items()]
yesterdays_closing_price = float(stock_list[0]["4. close"])

# TODO 2. Get the day before yesterday's closing stock price
day_before_yesterday_closing_price = float(stock_list[1]["4. close"])
# day_before_yesterday_closing_price = float(stock_data["Time Series (Daily)"]["2023-07-13"]["4. close"])

# TODO 3. Find the positive difference between 1 and 2
difference = yesterdays_closing_price - day_before_yesterday_closing_price
up_down = None
if difference > 0:
    up_down = "📈"
else:
    up_down = "📉"

# TODO 4. Work out the percentage difference in price
difference_percent = (difference / yesterdays_closing_price) * 100
print(difference_percent)

# TODO 5. If difference in percent is more than 5%, get news
if abs(difference_percent) > 1:
    print("Get news.")
    # STEP 2: fetch data from newsapi
    response = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
    response.raise_for_status()
    news_data = response.json()["articles"]
    # TODO 1. 
    news_slice = news_data[:3]
    # print(news_slice)
    article_title = news_slice[0]["title"]
    article_description = news_slice[0]["description"]

    # STEP 3: send an email with article's title and description
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=SENDER_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr= SENDER_EMAIL, 
            to_addrs=RECEIVER_EMAIL, 
            msg=f"Subject: {STOCK_NAME}: {article_title}\n\n{article_description}"
            )