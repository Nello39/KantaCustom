import requests
import json
import csv

api_key = "RGAPI-a40c85a4-a3fb-495a-ae5a-d25cca5d4be3"
base_url = "https://jp1.api.riotgames.com"
endpoint = "/lol/tournament-stub/v5/providers"

url = base_url + endpoint
headers = {"X-Riot-Token": api_key}

params = {
    "region": "JP",  # リージョンを指定
    "url": "http://localhost:80/callback"  # コールバックURLを指定
}

try:
    responce = requests.post(url, headers=headers, json=params)
    print (responce.text)

except Exception as e:
    print(e)