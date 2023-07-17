import requests, os
from dotenv import load_dotenv

load_dotenv()


# GET: requests.get()
# POST: requests.post()
# PUT: requests.put()
# DELETE: requests.delete()

# STEP 1: Create your user account: Call /v1/users API by HTTP POST.
# pixela api
pixela_endpoint = "https://pixe.la/v1/users"
pixela_token = os.environ.get("PIXELA_TOKEN")
# define the parameters
user_parameters = {
    "token": pixela_token,
    "username": "ahmadkhairi",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
    }

# once user is created, comment out:
# response = requests.post(url=pixela_endpoint, json=user_parameters)
# print(response.text)
# output: {"message":"Success. Let's visit https://pixe.la/@ahmadkhairi , it is your profile page!","isSuccess":true}

# STEP 2: Create a graph definition: Call /v1/users/<username>/graphs by HTTP POST.
pixela_username = "ahmadkhairi"
graph_endpoint = f"{pixela_endpoint}/{pixela_username}/graphs"
graph_parameters = {
    "id": "graph1",
    "name": "Running Graph",
    "unit": "Km",
    "type": "float",
    "color": "sora"
    }
headers = {
    "X-USER-TOKEN": pixela_token
    }
# once graph is created, comment out:
# response = requests.post(url=graph_endpoint, headers=headers, json=graph_parameters)
# print(response.text)
# output: {"message":"Success.","isSuccess":true}

# STEP 3: Get the graph!
# browse: https://pixe.la/v1/users/ahmadkhairi/graphs/graph1.html

# STEP 4: Post value to the graph: Call /v1/users/<username>/graphs/<graphID> by HTTP POST.
# get the latest date in the format of yyyyMMdd
from datetime import datetime
# today = datetime(year=2023, month=7, day=2)
today = datetime.now()
# date_today = (str(today.date())).replace("-", "")
# alternatively, use the strftime() method:
date_today = today.strftime("%Y%m%d")
# print(date_today)

graph_id = "graph1"
post_to_graph_endpoint = f"{graph_endpoint}/{graph_id}"
post_to_graph_parameters = {
    "date": date_today,
    "quantity": input("How many kilometers did you run today? ")
    }
# to comment out. only send request when you want to update the graph/pixela!
response = requests.post(url=post_to_graph_endpoint, headers=headers, json=post_to_graph_parameters)
print(response.text)
# Output: {"message":"Success.","isSuccess":true}

# STEP 5: Update the quantity already registered as a "Pixel".
update_graph_endpoint = f"{post_to_graph_endpoint}/{date_today}"
update_graph_parameters = {
    "quantity": "5.64"
    }
# use requests.put() to update
# response = requests.put(url=update_graph_endpoint, headers=headers, json=update_graph_parameters)
# print(response.text)
# output: {"message":"Success.","isSuccess":true}


# STEP 6: Delete the registered "Pixel".
delete_graph_endpoint = f"{post_to_graph_endpoint}/{date_today}"
# response = requests.delete(url=delete_graph_endpoint, headers=headers)
# print(response.text)
# output: {"message":"Success.","isSuccess":true}
