from lib2to3.pytree import Base
from urllib import request
import requests

BASE = "http://127.0.0.1:5000/"

data = [{"likes": 100000, "name": "a7", "views": 100000},
        {"likes": 100, "name": "how to make rest api", "views": 100000},
        {"likes": 1000, "name": "flask", "views": 100000},
        {"likes": 100000, "name": "gsoc", "views": 100000000}]

for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), data[i])
    print(response.json())


input()
response = requests.delete(BASE + "video/0")
print(response)

input()
response = requests.get(BASE + "video/2")
print(response.json())
