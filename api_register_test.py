import requests
import json
import os

user = {
    "username" : "Eziogreggio",
	"password": "gabibbo",
	"firstname": "Ezio",
	"lastname": "Greggio",
	"email": "ezio.greggio@example.com",
	"mfa_enabled": False,
	"is_internal": True,
	"role": "admin_system",
	"status": 1,
	"profile_img_base64": "string",
	"session_timeout_min": 0
	}

url = "http://localhost:5000/api/user"

def test_user_register(): 	
    response = requests.post(
        url,
        json=user
    )
    print(response.text)
    assert response.status_code == 200

    response_2 = requests.post(
        url,
        json=user
    )

    assert response_2.status_code == 400
    assert response_2.text == "invalid user"
