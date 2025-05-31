import requests
import datetime as dt
import os

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")
POST_URL = os.environ.get("POST_URL")
USERNAME = os.environ.get("USERNAME")
PASSWORD = os.environ.get("PASSWORD")
BASIC_AUTH_TOKEN = os.environ.get("BASIC_AUTH_TOKEN")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

parameters = {
    "query": input("Tell me which exercise you did: ")
}

response1 = requests.post(url="https://trackapi.nutritionix.com/v2/natural/exercise",
                         json=parameters,
                         headers=headers)
response1.raise_for_status()

auth_headers = {
    "Authorization": BASIC_AUTH_TOKEN
}

date = str(dt.datetime.now().date()).replace("-", "/")
time = str(dt.datetime.now().time())

params = {
    "workout": {
        "date": date,
        "time": time,
        "exercise": str(response1.json()['exercises'][0]['name']),
        "duration": str(response1.json()['exercises'][0]['duration_min']),
        "calories": str(response1.json()['exercises'][0]['nf_calories'])
    }
}

response3 = requests.post(url=POST_URL, json=params, headers=auth_headers)
response3.raise_for_status()