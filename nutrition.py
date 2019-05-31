import requests
from login import Login

class Nutrition:
    def __init__(self, token):
        self.base_url = 'http://localhost:8000/api/'
        self.token = token
        self.headers = {'Authorization': 'Token ' + self.token}
    
    def tags_create(self, name, calories):
        """create tags use for nutrition"""
        res = requests.post(self.base_url + 'recipe/tags/',headers=self.headers, 
        data={
            'name': name,
            'calories': calories
            }
        )


    def tags_get_all(self):
        """retrieve all tags created by this user"""
        res = requests.get(self.base_url + 'recipe/tags/',headers=self.headers)

        return res.json()

    
    # def nutrition_create(self):
    #     """create nutrition by add tags and date"""
    #     res = requests.post()

a = Login('admin@admin.com', 'admin')
a.user_login()
b = Nutrition(a.get_token())
# b.tags_create('pizza', 1000)
print(b.tags_get_all())