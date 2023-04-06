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
new_user = {
        "username" : "eziogreggio",
        "password": "gabibbo",
        "firstname": "ezio",
        "lastname": "greggio",
        "email": "ezio.greggio@example.com",
        "mfa_enabled": False,
        "is_internal": True,
        "role": "admin_system",
        "status": 1,
        "profile_img_base64": "string",
        "session_timeout_min": 0
    }
new_pw = "gabibb0"
url_login = "http://localhost:5000/api/auth/login"
user_data = {"username": user['username'], "password": user['password'] }
new_user_data = {"username": new_user['username'], "password": new_user['password'] }
user_mario = {"username": "mario.pippo", "password": "tortellino" }


def login(url, data):
    response = requests.post(url, json=data)
    return response.json()['info'][0]['sessionId']

class TestApiUser:
    def test_auth_login(self):

        response = requests.post(url_login, json=user_data)
        
        r = response.json()
        if not user['mfa_enabled']:
            assert response.status_code == 200
            assert r['info'][0]['sessionId'] 
        else:
            assert response.status_code == 202
            assert r['error_code'] == "err_2fa"
    def test_get_user(self):

        sid = login(url_login, user_data)
        headers = {'Authorization': sid}
        url = "http://localhost:5000/api/user" + "/" + user['username']

        response = requests.get(
                url,
                headers=headers
                )
        r = response.json()

        assert response.status_code == 200
        assert r['username']

    def test_put_user(self):
        
        sid = login(url_login, user_data)
        headers = {'Authorization': sid}
        url = "http://localhost:5000/api/user" + "/" + user['username']
        response = requests.put(url, headers=headers, json=new_user)

        assert response.status_code == 200
        assert response.text == "successful operation"       
        response_3 = requests.put("http://localhost:5000/api/user/giovannimuciaccia", headers=headers, json=new_user)
        assert response_3.status_code == 404
        assert response_3.text == "user not found"

    def test_get_modified_user(self):
        sid = login(url_login, new_user_data)
        headers = {'Authorization': sid}
        url = "http://localhost:5000/api/user" + "/" + new_user['username']

        response = requests.get(
                url,
                headers=headers
                )
        r = response.json()

        assert response.status_code == 200
        assert r['firstname'] == new_user['firstname']

    def test_put_password_user(self):

        sid = login(url_login, new_user_data)
        headers = {'Authorization': sid}
        url = "http://localhost:5000/api/user" + "/" + new_user['username'] + "/password" 

        new_pass = {"old_password": user['password'], "new_password": new_pw}
        response = requests.put(
                url,
                headers=headers,
                json=new_pass
                )
        assert response.status_code == 200
        
        fake_pw = {"old_password": "belando", "new_password": "besugo"}
        response = requests.put(
                url,
                headers=headers,
                json=fake_pw
                )
        assert response.status_code == 401

    def test_login_new_password(self):
        response = requests.post(
                url_login,
                json=new_user_data
                )
        assert response.status_code == 401

        new_user_data['password'] = new_pw
        sid = login(url_login, new_user_data)
        assert sid 

    def test_delete_user(self):
        new_user_data['password'] = new_pw
        sid = login(url_login, new_user_data)
        headers = {'Authorization': sid}
        url = "http://localhost:5000/api/user" + "/randomuser"

        response = requests.delete(
                url,
                headers=headers
                )
        assert response.status_code == 404
        
        url = "http://localhost:5000/api/user" + "/" + new_user['username']

        response = requests.delete(
                url,
                headers=headers
                )
        assert response.status_code == 200

    def login_deleted_user(self):

        new_user_data['password'] = new_pw
        response = requests.post(url_login, json=new_user_data)
        assert response.status_code == 401
