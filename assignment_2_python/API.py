import requests
import json

# response = requests.get("https://ghibliapi.vercel.app/films")
# print(response.status_code)
# print(response.json())
#
response = requests.get("https://ghibliapi.vercel.app/people")
print(response.status_code)
print(response.json())
data = response.text
parse_jason = json.loads(data)
character = parse_jason("Ashitaka", "Male")
print(character)