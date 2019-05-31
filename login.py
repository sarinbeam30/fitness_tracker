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

    def get_user_goal(self):
        res = requests.get(self.base_url + 'me/', headers=self.headers)

        return res.json()['goal']

    def get_user_name(self):
        res = requests.get(self.base_url + 'me/', headers=self.headers)

        return res.json()['name']

    def get_user_email(self):
        res = requests.get(self.base_url + 'me/', headers=self.headers)

        return res.json()['email']

    def get_user_weight(self):
        res = requests.get(self.base_url + 'me/', headers=self.headers)

        return res.json()['weight']

    def get_user_height(self):
        res = requests.get(self.base_url + 'me/', headers=self.headers)

        return res.json()['height']

    def get_user_birthdate(self):
        res = requests.get(self.base_url + 'me/', headers=self.headers)

        return res.json()['birth']

    def get_user_sex(self):
        res = requests.get(self.base_url + 'me/', headers=self.headers)

        return res.json()['sex']

    def user_change_profile(self, email, password, name, weight, height, gender):

        res = requests.patch(self.base_url + 'me/',headers=self.headers , data=
            {
            'email': email,
            'name': name, 
            'password': password,
            'weight': weight,
            'height': height
            }
        )
        print(res.status_code)
        return res

    def set_user_birthdate(self, name, birth):
        res = requests.patch(self.base_url + 'me/', headers=self.headers, data= {
            "email": self.email,
            "name": name,
            "birth": birth
            }
        )

    def set_user_gender(self, name, gender):
        res = requests.patch(self.base_url + 'me/', headers=self.headers, data= {
            "email": self.email,
            "name": name,
            "gender": gender
            }
        )

# a = Login('tarn@gmail.com', 'admin')
# a.user_login()
# a.set_user_birthdate('tarrz','2000-06-22')
# print(a.get_user_profile())