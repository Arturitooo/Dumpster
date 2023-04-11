import requests

from datetime import datetime

USERNAME = "arturitooo"
TOKEN = "asdsdgsd431234esdf"
GRAPHID = f"graph{USERNAME}"

today = datetime.now()
DATE = today.strftime("%Y%m%d")

PIXELA_CREATE_ENDPOINT = "https://pixe.la/v1/users"
PIXELA_GRAPH_ENDPOINT = f"{PIXELA_CREATE_ENDPOINT}/{USERNAME}/graphs"
PIXELA_ADDVALUE_ENDPOINT = f"{PIXELA_CREATE_ENDPOINT}/{USERNAME}/graphs/{GRAPHID}"
PIXELA_UPDATEVALUE_ENDPOINT = f"{PIXELA_CREATE_ENDPOINT}/{USERNAME}/graphs/{GRAPHID}/{DATE}"

user_pce_params = {
"token":TOKEN,
"username":USERNAME,
"agreeTermsOfService":"yes",
"notMinor":"yes",
}

user_pge_params = {
    "id":GRAPHID,
    "name":"Coding graph",
    'unit':"minutes",
    "type":"float",
    "color":"sora",
}

user_pave_params = {
    "date":DATE,
    "quantity":"15",
}

user_puve_params = {
    "quantity":"115",
}

#for the second (and 3rd) request - you have to use "header" to authenticate as a user, otherwise you would be forced to add sensitive data to the url
headers = {
    "X-USER-TOKEN":TOKEN
}

#esponse = requests.post(url=PIXELA_CREATE_ENDPOINT, json = user_pce_params)
#response = requests.post(url = PIXELA_GRAPH_ENDPOINT, json = user_pge_params, headers= headers)
#response = requests.post(url = PIXELA_ADDVALUE_ENDPOINT, json = user_pave_params, headers=headers)
#response = requests.put(url = PIXELA_UPDATEVALUE_ENDPOINT, json = user_puve_params, headers = headers)

response = requests.delete(url = PIXELA_UPDATEVALUE_ENDPOINT, headers=headers)

print(response)
print(response.text)

