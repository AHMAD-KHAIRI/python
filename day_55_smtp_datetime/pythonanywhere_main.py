import smtplib, random

my_email = "ak.test.smtp.python@gmail.com"
my_app_password = "mghdwtncpaiajeeb"
recipient_email = "khairihamzah85@gmail.com"

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
        msg=f"Subject: Daily Motivation\n\n{quote}\nThis email is sent from PythonAnywhere"
        )