import requests

class Login:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.base_url = 'http://localhost:8000/api/user/'
        self.status_code = 404
        self.headers = {'Authorization': 'Token ' + self.user_login()}
    
    def get_email(self):
        return self.email
    
    def get_password(self):
        return self.password

    def get_status_code(self):
        return self.status_code

    def get_token(self):
        return self.user_login()

    def user_login(self):
        """user login return token"""
        res = requests.post(self.base_url + 'token/', data= {
            'email': self.email, 
            'password': self.password
            }
        )
        self.status_code = res.status_code
        if self.status_code == 200:
            token = res.json()['token']
            return token
        else:
            raise Exception('Wrong Input')
        

    def get_user_profile(self):
        """retrieve user profile"""
        res = requests.get(self.base_url + 'me/', headers=self.headers)

        return res.json()

    def get_user_name(self):
        res = requests.get(self.base_url + 'me/', headers=self.headers)

        return res.json()['name']

    def user_change_name(self, name):

        res = requests.put(self.base_url + 'me/',headers=self.headers , data=
            {
            'email': self.email, 
            'password': self.password,
            'name': name,
            }
        )
        print(res.status_code)
        return res

a = Login('khem@khem.com', 'khemkhem')
print(a.user_login())
print(a.get_user_profile())