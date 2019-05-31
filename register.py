import requests
import login

class Register():
    def __init__(self, name, email, password, weight, height, sex, birthdate):
        self.name = name
        self.email = email
        self.password = password
        self.weight = weight
        self.height = height
        self.sex = sex
        self.birthdate = birthdate
        self.status = 404
        self.base_url = 'http://localhost:8000/api/user/'

    def get_statuscode(self):
        return self.status

    def user_register(self):
        """user register w/ email, password and name"""
        res = requests.post(self.base_url + 'create/', data= {
            'email': self.email, 
            'password': self.password,
            'name': self.name,
            'weight': self.weight,
            'height': self.height,
            'sex': self.sex,
            'birthdate': self.birthdate,
            'goal':"0"
            }
        )

        self.status = res.status_code
        return res


    

        