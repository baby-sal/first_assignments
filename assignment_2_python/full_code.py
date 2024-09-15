# **Studio Ghibli Character Generator and Movie Recommendation**
# Which studio Ghibli character do you look like?
# Which studio Ghibli movie do they appear in?
#
# Create a welcome message to explain what the purpose of the program is
# Ask the user to input their gender, hair colour and eye colour
# Send the inputs to the API to return the characters that you have similar features
# Give the option of which character the user would like to learn about.
# Display the characters details and what films they appear in (title, original title, release year, description, rotten tomato score(put highest ranking on top?))
import requests
import json
import time

# User dictionary:
user = {
    "name":"",
    "gender":"",
    "hair_colour":"",
    "eye_colour":"",
}

# Ask for the user to input their name:

def read_out_my_name(name):
    for letter in name:
        print(letter)

user["name"] = input("Hello friend, how do I spell your name?")

read_out_my_name(user["name"])

# Explain the program to the user:
print(f'''\n{user["name"]}, it's nice to meet you! \nIf you can kindly share some details with me, I'd like to find your Ghibli doppelganger and recommend you a movie. \nIf that sounds ok, let's get spirited away!''')

# Ask for the user's inputs
# Name, creating a themed nickname
user_gender = input("What is your gender?")

def nickname(suffix):
    if user_gender == "Male" or user_gender == "male":
        suffix = "-kun"
    elif user_gender == "Female" or user_gender == "female":
        suffix = "-chan"
    else:
        suffix = "-san"

    full_name = (user["name"] + suffix)

    print(f"OK! We shall call you " + full_name+"!")
    return full_name
# Collecting hair colour and eye colour

user_name = nickname("")

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

print(f"I'm finding so much out about you! One more thing...")

ghibli_eyes = input("I can't help getting lost in your eyes, " + user_name +", but what is their colour?").capitalize()

endpoint_2 = f"https://ghibliapi.vercel.app/people"
response_2 = requests.get(endpoint_2)
data_2 = response_2.json()

# print the names
ghibli_name_2 = [person["name"] for person in data_2 if person["eye_color"].capitalize() == ghibli_eyes]
if ghibli_name_2:
    print(", ".join(ghibli_name_2) + " has the same eye colour as you!")
else:
    print("Sorry no match, try again?")

print("Now let's see if you have a doppelganger or not...")
time.sleep(3.0)

# Testing the doppelganger finder
doppelganger_name = [name for name in ghibli_name if name in ghibli_name_2]

if doppelganger_name:
    print("Your Ghibli doppelganger is: " + ", ".join(doppelganger_name))
else:
    print("Sorry no match...")

# Connecting doppelganger with films

interest_cha = input("Which character would you search in movies?").capitalize()

interest_films = []
for person in data:
    if person["name"].capitalize() == interest_cha:
        interest_films = person["films"]

if interest_films:
    print (f"{interest_cha} is in the following films:")
    for film_url in interest_films:
        film_response = requests.get(film_url)
        film_data = film_response.json()
        print(f"{film_data["title"]} which was produced by {film_data["director"]}")
        release_year = str(film_data["release_date"])
        print(f"It was released in '" + release_year[2:4])
        print(f"Here is a quick description: \n {film_data["description"]}")
        print(f"This film garnered a Rotten Tomatoes score of {film_data["rt_score"]} /100, why don't you check it out?!")
        file = open("/Users/sallydavies/Desktop/CFG Degree/CFG-Assignments/assignment_2_python/results.txt", "a+")
        file.write(f"\n {film_data["title"]}")
        file.close()