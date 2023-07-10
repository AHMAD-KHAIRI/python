import smtplib, pandas, random
from datetime import datetime

my_email = "ak.test.smtp.python@gmail.com"
# Gmail app: python_birthday_wisher
my_app_password = "mghdwtncpaiajeeb"

# 1. Check if today matches a birthday in birthdays.csv
today = datetime.now()
today_tuple = (today.month, today.day)

# 2. Import birthdays.csv as dataframe
data = pandas.read_csv("birthdays.csv")
# below is for pythonanywhere:
# data = pandas.read_csv("./automated_birthday_wisher/birthdays.csv")

# 3. Create a dictionary from birthdays.csv that is formatted like this:
# birthdays_dict = {
    # (birthday_month, birthday_day): data_row
    # }
# use dictionary comprehension keyword: new_dict = {new_key:new_value for (index, data_row) in data.iterrows()}
# birthdays_dict = {(data_row["month"], (data_row["day"])): data_row for (index, data_row) in data.iterrows()}
birthdays_dict = {(data_row.month, (data_row.day)): data_row for (index, data_row) in data.iterrows()}

# 4. Compare if today's month/day tuple matches one of the keys in the birthdays dictionary
if today_tuple in birthdays_dict:
    birthday_name = birthdays_dict[today_tuple]
    # 5. If there is a match, pick a random letter from letter templates folder
    file_path = f"./letter_templates/letter_{random.randint(1,3)}.txt"
    # below is for pythonanywhere:
    # file_path = f"./automated_birthday_wisher/letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        # replace the placeholder with the birthday name
        contents = contents.replace("[NAME]", birthday_name["name"])

# 5. Send the letter generated using SMTP
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_app_password)
        connection.sendmail(
            from_addr= my_email, 
            to_addrs=birthday_name["email"], 
            msg=f"Subject:Happy Birthday!\n\n{contents}"
            )      
# YourName,your_own@email.com,today_year,today_month,today_day
# name,email,year,month,day