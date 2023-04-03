import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

url="https://v3.football.api-sports.io/fixtures?league=135&season=2022&date=2023-04-02"
    
key = os.getenv('API_KEY')

payload = {}

headers = {
  'x-rapidapi-key': key,
  'x-rapidapi-host': 'v3.football.api-sports.io'
}

response = requests.get(
    url,
    headers=headers,
    data=payload
)
json_response = response.json()

assert response.status_code == 200
assert json_response['errors'] == []
assert json_response['get'] == 'fixtures'
for i in range(len(json_response['response'])):
    assert json_response['response'][i]['fixture']['status']['short'] == 'FT'


with open ('request.json', 'w') as f:
    f.write(json.dumps(json_response))



response_2 = requests.get(
    url,
    headers={'Authorization': "iZ4RAvZAG2ROqH19VDp06O41hVDKC37C5qh621ZJERQ9Sdl4gAlsB7l4SZQ"},
    data=payload
)
json_response_2 = response_2.json()

assert json_response_2['errors']['token'] != ''
