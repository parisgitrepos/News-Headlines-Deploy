import requests
import os

class Auth:
    def __init__(self, env_key = 'AUTH_API'):
        self.web_api_key = os.getenv(env_key)
    
    def signup(self, email, password):
        web_api_key = self.web_api_key
        signup_endpoint = 'https://identitytoolkit.googleapis.com/v1/accounts:signUp?key=' + web_api_key

        json = {'email':email, 'password':password}
        r = requests.post(signup_endpoint, json=json)
        
        if r.status_code == 400:
            return [r.status_code, r.json()['error']['message']]
        elif r.status_code == 200:
            return [r.status_code]

    def login(self, email, password):
        web_api_key = self.web_api_key
        login_endpoint = 'https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key=' + web_api_key

        json = {'email':email, 'password':password}

        r = requests.post(login_endpoint, json = json)

        if r.status_code == 400:
            return [400, r.json()['error']['message']]
        elif r.status_code == 200:
            print(r.json()) # Temporary
            return [200, r.json()['refreshToken']]
        else:
            return ['UNKNOWN']
            
    def refresh_token(self, token):
        endpoint = 'https://securetoken.googleapis.com/v1/token?key=' + self.web_api_key
        json = {'refresh_token':token}
        r = requests.post(endpoint, json = json)
        if r.status_code == 200:
            return [200, refresh_token]
        elif r.status_code == 400:
            return [400, 'ERROR']