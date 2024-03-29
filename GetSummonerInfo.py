import requests
import json
import csv

api_key = "RGAPI-d2d06417-85aa-46d9-9208-7b1e95a7e4d8"
base_url = "https://jp1.api.riotgames.com"
endpoint = "/lol/summoner/v4/summoners/by-name/Nello#S913"

url = base_url + endpoint
headers = {"X-Riot-Token": api_key}

try:
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        print(response.text)
        summoner_data = response.json()
        print("Summoner Data:")
        print(f"Summoner Name: {summoner_data['name']}")
        print(f"Summoner Level: {summoner_data['summonerLevel']}")
        print(f"Summoner ID: {summoner_data['id']}")
        print(f"Account ID: {summoner_data['accountId']}")
    else:
        print(f"Error: {response.status_code}")
        print(response.json())  # エラーレスポンスの詳細を表示

except Exception as e:
    print(f"エラーが発生しました: {e}")

