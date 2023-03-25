
from email import header
import requests
import json

URL = "http://127.0.0.1:8000/student_api/"

def get_data(id=None):
    data = {}
    headers = {'content-Type':'application/json'}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    res = requests.get(url=URL,headers=headers, data=json_data)
    data = res.json()
    print(data)
# get_data(2)

def post_data():
    data ={
        'name': 'Adeel',
        'age':15,
        'city':'layyah'
    }
    headers = {'content-Type':'application/json'}
    res = json.dumps(data)
    json_data = requests.post(url=URL,headers=headers, data=res)
    result = json_data.json()
    print(result)
# post_data()

def update():
    data = {
        'id':3,
        'name':'Masha',
        'age':55
    }
    headers = {'content-Type':'application/json'}
    res = json.dumps(data)
    json_data = requests.put(url=URL,headers=headers, data=res)
    result = json_data.json()
    print(result)
# update()

def delete_data():
    data={'id':3}
    headers = {'content-Type':'application/json'}
    res = json.dumps(data)
    json_data = requests.delete(url=URL,headers=headers, data=res)
    result = json_data.json()
    print(result)
# delete_data()

