#working with apis and dictionaries

import requests
import json
response = requests.get("https://randomuser.me/api")

#print(response.json())

title = response.json()['results'][0]['name']['first']
print(title)
gender = response.json()['results'][0]['gender']
print(gender)
last_name = response.json()['results'][0]['name']['last']
print(last_name)
st_name = response.json()['results'][0]['location']['street']['name']
print(st_name)
city = response.json()['results'][0]['city']['state']['postcode']
state = response.json()['results'][0]['country']
print(city)
print(state)
email = response.json()['results'][0]['email']
login = response.json()['results'][0]['login']['username']
print(email)
print(login)