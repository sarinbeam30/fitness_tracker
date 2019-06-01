import requests
from login import Login
from datetime import datetime
import json

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
        return res.json()['id']

    def tags_get_all(self):
        """retrieve all tags created by this user"""
        res = requests.get(self.base_url + 'recipe/tags/',headers=self.headers)

        return res.json()

    def tags_get_name(self):
        """retrieve all tags created by this user"""
        res = requests.get(self.base_url + 'recipe/tags/',headers=self.headers)
        gather = []

        for i in res.json():
            gather.append(i['id'])
        return gather
    
    def nutrition_create(self, name, cal):
        """create nutrition by add tags and date"""
        d = json.dumps
        result = self.tags_create(name, cal)
        res = requests.post(self.base_url + 'recipe/recipes/', headers=self.headers, data =
        {
            "date": "2019-10-10",
            "tags": [result]
        })

    def nutrition_today_list(self):
        gather = []
        want_unique = []
        res = requests.get(self.base_url + 'recipe/recipes/',headers=self.headers)
        
        for i in res.json():
            if i['date'] == datetime.today().strftime('%Y-%m-%d'):
                # print(i['date'])
                gather.append(i['tags'])
        for i in gather:
            for j in i:
                want_unique.append(j)
        gather = self.unique(want_unique)
        return gather

    def unique(self, list1): 
        unique_list = [] 
        for x in list1: 
            if x not in unique_list: 
                unique_list.append(x) 
        return unique_list

    def get_tags_name_by_id(self, tag):

        gather = []
        res = requests.get(self.base_url + 'recipe/tags/',headers=self.headers)
       
        for i in res.json():
            if(tag == i['id']):
                gather.append(i)

        return gather

    def get_tags_name_by_multiple_id(self, tags):

        gather = []
        res = requests.get(self.base_url + 'recipe/tags/',headers=self.headers)
        
        for i in tags:
            for j in res.json():
                if(i == j['id']):
                    gather.append(j)

        return gather


# a = Login('admin@admin.com', 'admin')
# a.user_login()
# b = Nutrition(a.get_token())
# print(datetime.today().strftime('%Y-%m-%d'))
# b.nutrition_create("rainbow", 300)
# b.tags_create('pizza', 1000)
# print(b.tags_get_all())
# print(b.tags_get_name())
# print(b.nutrition_today_list())
# print(b.get_tags_name_by_id(30))
# print(b.get_tags_name_by_multiple_id([1, 2, 3]))