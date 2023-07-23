import smtplib, os

SENDER_EMAIL = os.environ.get("SENDER_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")
RECEIVER_EMAIL = os.environ.get("RECEIVER_EMAIL")

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        with smtplib.SMTP("smtp.gmail.com", port=587) as self.connection:
            self.connection.starttls()
            self.connection.login(user=SENDER_EMAIL, password=MY_PASSWORD)

    def send_emails(self, emails, message):
        for email in emails:
            self.connection.sendmail(
                from_addr=SENDER_EMAIL,
                to_addrs=email,
                msg=f"Subject:New Low Price Flight!\n\n{message}".encode('utf-8')
            )