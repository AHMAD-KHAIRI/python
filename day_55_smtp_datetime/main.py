import smtplib, random
import datetime as dt

my_email = "ak.test.smtp.python@gmail.com"
# Gmail app: python_birthday_wisher
my_app_password = "mghdwtncpaiajeeb"
recipient_email = "khairihamzah85@gmail.com"

# now = dt.datetime.now()
# weekday = now.weekday()
# print(weekday)

# # if it is Monday
# if weekday == 0:
with open("quotes.txt") as quote_file:
    all_quotes = quote_file.readlines()
    quote = random.choice(all_quotes)

# print(quote)
with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_app_password)
    connection.sendmail(
        from_addr= my_email, 
        to_addrs=recipient_email, 
        msg=f"Subject: Monday Motivation\n\n{quote}\nThis email is sent using Python SMTP"
        )


'''
# SMTP: Simple Mail Transfer Protocol
import smtplib

# Gmail: smtp.gmail.com
# Hotmail: smtp.live.com
# Outlook: outlook.office365.com
# Yahoo: smtp.mail.yahoo.com


my_email = "ak.test.smtp.python@gmail.com"
# Gmail app: python_birthday_wisher
my_app_password = "mghdwtncpaiajeeb"


# Google SMTP Port
with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_app_password)
    connection.sendmail(
        from_addr= my_email, 
        to_addrs="aktestsmtppython@yahoo.com", 
        msg="Subject:Hello!\n\nThis is a test email using Python SMTP"
        )

# Using this way forces us to close the connection at the end:
# connection = smtplib.SMTP("smtp.gmail.com", port=587)
# connection.starttls()
# connection.login(user=my_email, password=my_app_password)
# connection.sendmail(from_addr= my_email, to_addrs="aktestsmtppython@yahoo.com", msg="Subject:Hello!\n\nThis is a test email using Python SMTP")
# # connection.sendmail(from_addr= my_email, to_addrs="aktestsmtppython@yahoo.com", msg="Hello!")
# connection.close()


# datetime module
import datetime as dt

# how we can get the current date, time, year, month, etc
now = dt.datetime.now()
year = now.year
month = now.month
day_of_the_week = now.weekday()
print(day_of_the_week)

date_of_birth = dt.datetime(year=1985, month=9, day=27)
'''