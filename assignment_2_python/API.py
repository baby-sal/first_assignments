# Attempt 1
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


# Attempt 2
# import requests
#
# end_point = "https://ghibliapi.vercel.app/people"
#
# response = requests.get(end_point)
#
# print("response is:", response)
#
# ghibli_hair = input("What is your hair colour?  ")
#
# endpoint = "https://ghibliapi.vercel.app/people"
#
# data = requests.get(endpoint).json()
#
# cha_with_hair = [person for person in data if person["hair_color"] == ghibli_hair]
#
# if cha_with_hair:
#     for person in data:
#         print("You have the same hair colour as:", (cha_with_hair["name"]))
# else:
#     print("You are a rare beauty, can we try another colour?")
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

# Info from Hamed
#
# import requests
#
# endpoint = " https://ghibliapi.vercel.app/people"
# response = requests.get(endpoint)
# data = response.json()
#
# # print(type(data))
#
# characters_with_brown_hair = []
#
# for character in data:
#     if character["hair_color"] == "Brown":
#         characters_with_brown_hair.append(character["name"])
#
#
# print(characters_with_brown_hair)

# Attempt
# import requests
#
# ghibli_hair = input("What is your hair colour?  ").capitalize()
#
# endpoint = f"https://ghibliapi.vercel.app/people?hair_color={ghibli_hair}"
# response = requests.get(endpoint)
# data = response.json()
#
# brwn_hair_cha = []
# black_hair_cha = []
# white_hair_cha = []
# blonde_hair_cha = []
#
#
# for character in data:
#     if character["hair_color"] == "Brown":
#         brwn_hair_cha.append(character["name"])
#     elif character["hair_color"] == "Black":
#         black_hair_cha.append(character["name"])
#     elif character["hair_color"] == "White":
#         white_hair_cha.append(character["name"])
#     elif character["hair_color"] == "Blonde":
#         blonde_hair_cha.append(character["name"])

# print("You have the same hair colour as:" + str(brwn_hair_cha), str(black_hair_cha), str(white_hair_cha), str(blonde_hair_cha))


# Attempt 3

import requests

ghibli_hair = input("What is your hair colour?  ").capitalize()

endpoint = f"https://ghibliapi.vercel.app/people?hair_color={ghibli_hair}"
response = requests.get(endpoint)
data = response.json()

# print the names
ghibli_name = [person["name"] for person in data]
if ghibli_name:
    print(", ".join(ghibli_name) + " has the same hair colour as you!")
else:
    print("Sorry no match, try again?")

# Dictionary attempt:
# form a dictionary for hair colour

# cha_hair_color = {
#     "Brown":[],
#     "Black":[],
#     "Blonde":[],
#     "Dark Brown":[],
#     "None":[],
#     "Reddish brown":[],
#     "Yellow":[],
#     "Bald":[],
#     "White":[],
#     "Light orange":[],
#     "Grey":[],
#     "Red":[],
#     "Blue":[],
#     "Beige":[]
# }
#
# for character in data:
#     hair_color = character["hair_color"].capitalize()
#     if hair_color in cha_hair_color:
#         cha_hair_color[hair_color].append(character["name"])
#
# print("You have the same hair color as:")
# for hair_color in cha_hair_color.items():
#     if ghibli_hair == hair_color:
#         print(cha_hair_color["name"])
#     elif ghibli_hair != hair_color:
#         print("Would you like to try again?")