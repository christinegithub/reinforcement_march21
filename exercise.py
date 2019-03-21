import requests
import json

# Exercise 1

ottawa_wards_response = requests.get('https://represent.opennorth.ca/boundaries/?sets=ottawa-wards')
ottawa_wards_response.json()

body = json.loads(ottawa_wards_response.content)

for object in body["objects"]:
    print(object["name"])


print("-------------------------------")

# Exercise 2

candidates_response = requests.get('https://represent.opennorth.ca/candidates')
candidates_response.json()

candidates = json.loads(candidates_response.content)

for candidate in candidates["objects"]:
    print(candidate["last_name"])
