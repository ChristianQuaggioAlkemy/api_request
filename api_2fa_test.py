import requests
import json
import os
import pytest
import pyotp

user = {
    "username" : "enzinoiacc",
	"password": "veline",
	"firstname": "Enzo",
	"lastname": "Iacchetti",
	"email": "enzo.iacchetti@example.com",
	"mfa_enabled": False,
	"is_internal": True,
	"role": "admin_system",
	"status": 1,
	"profile_img_base64": "string",
	"session_timeout_min": 0
	}

user_data = {"username": user['username'], "password": user['password']}

url_user = "http://localhost:5000/api/user"
url_login = "http://localhost:5000/api/auth/login"
url_2fa = "http://localhost:5000/api/auth/2fa"

reg = requests.post(
        url_user,
        json=user
        )
log = requests.post(url_login, json=user_data)
secret = ''

class TestApi_2fa:
    def test_login_wo_2fa(self):

        r = log.json()
        assert log.status_code == 200
        assert r['info'][0]['sessionId']

    def test_enable_and_login_2fa(self):
        print(user_data)
        user['mfa_enabled'] = True
        sid = log.json()['info'][0]['sessionId']
        headers = {'Authorization': sid}
        url = "http://localhost:5000/api/user" + "/" + user['username']
        response = requests.put(url, headers=headers, json=user)
        
        user_data['mfa_token'] = pyotp.TOTP(response.json()['mfa_secret']).now()
        print(user_data)
        assert response.status_code == 200
        
        resp_random = requests.get(url, headers=headers)
        assert resp_random.status_code == 401

        log_2fa = requests.post(url_2fa, json=user_data)
        assert log_2fa.status_code == 200

    
    def test_login_wo_2fa_after_enabling_2fa(self):

        log_after = requests.post(url_login, json=user_data)

        assert log_after.status_code == 202
        assert log_after.json()['error_code'] == 'err_2fa'
        








