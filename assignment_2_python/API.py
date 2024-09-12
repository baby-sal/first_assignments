# import requests
# print(requests)
import json

# response = requests.get("https://ghibliapi.vercel.app/films")
# print(response.status_code)
# print(response.json())

# data = response.json()

# print(data)

# print the names
# for name in data:
#     print(name["name"])

import requests

end_point = "https://ghibliapi.vercel.app/people"

response = requests.get(end_point)

print("response is:", response)

ghibli_hair = input("What is your hair colour?  ")

endpoint = "https://ghibliapi.vercel.app/people"

data = requests.get(endpoint).json()

cha_with_hair = [person for person in data if person["hair_color"] == ghibli_hair]

if cha_with_hair:
    for person in data:
        print("You have the same hair colour as:", (cha_with_hair["name"]))
else:
    print("You are a rare beauty, can we try another colour?")
#
# ghibli_eye = input("What is your eye colour?  ")
#
# endpoint = "https://ghibliapi.vercel.app/people"
#
# data = requests.get(endpoint).json()

# cha_match = [person for person in data if person["eye_color"] == ghibli_eye and person["hair_color"] == ghibli_hair]
#
# if cha_match:
#     values = cha_match[0]["name"]
#     print("You look like:", values)
# else:
#     print("You are a rare beauty, want to retry")