import requests
import json
import os
from dotenv import load_dotenv

class TestApi:
    def test_right_api_key(self):
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


    def test_wrong_api_key(self):
        url="https://v3.football.api-sports.io/fixtures?league=135&season=2022&date=2023-04-02"
        payload = {}
        headers = {
            'x-rapidapi-key': 'CHIAVE_FALZA',
            'x-rapidapi-host': 'v3.football.api-sports.io'
        }
        response = requests.get(
            url,
            headers=headers,
            data=payload
        )
        json_response = response.json()
        
        assert json_response['errors']['token'] != ''
