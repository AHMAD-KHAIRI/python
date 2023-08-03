# import requests, os
# from msgraph import generate_access_token, GRAPH_API_ENDPOINT
# from dotenv import load_dotenv

# load_dotenv()

# APPLICATION_ID = os.environ.get("APPLICATION_ID")

# APP_ID = APPLICATION_ID
# SCOPES = ['Mail.Send']

# access_token = generate_access_token(app_id=APP_ID, scopes=SCOPES)
# headers = {
#     'Authorization': 'Bearer ' + access_token['access_token']
# }

# endpoint = GRAPH_API_ENDPOINT + '/me/sendMail'
# # endpoint = GRAPH_API_ENDPOINT + '/user/<emial address>'

# request_body = {
#     'message': {
#         'toRecipients': [
#             {
#                 'emailAddress': {
#                     'address': 'ahmad.khairi@boschrexroth.com.my',
#                     'name': 'DummyAcct'
#                 }
#             }
#         ],
#         'subject': 'Check your email2',
#         'body': {
#             'contentType': 'text', # or html
#             'content': 'Check your email for the latest update'
#         },
#         'importance': 'low'
#     }
# }

# response = requests.post(endpoint, headers=headers, json=request_body)
# print(response.status_code)

import win32com.client as win32
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

outlook = win32.Dispatch("Outlook.Application")
mail = outlook.CreateItem(0)

mail.Subject = "Automating Outlook email as of " + datetime.now().strftime('%#d %b %Y %H:%M')
mail.To = os.environ.get("MAIL_TO")
mail.CC = os.environ.get("MAIL_CC")

mail.HTMLBody = r"""
Dear recipient,<br><br>
This is just a test email.<br><br>
This is created with Python.<br><br>
Best regards,<br>
AK
"""
# mail.Display()
mail.Send()