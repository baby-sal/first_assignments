# **Studio Ghibli Character Generator and Movie Recommendation**

# Welcome. This app asks the user questions about their hair and eye color
# and finds a character in the Ghibli universe who looks like them.
# After the doppelganger is (or isn't...) revealed, the user can input a character
# name that they want to know about, with respect to the film they are in.
#
# I used the Ghibli API to access information about the characters and the films.
# The app sends a request to the API to form responses in the form of lists with the characters who match the user's hair colour and eye colour.
# Secondly, the app will respond the URL relating to the character and loop through the list of films on the film endpoint
# If there is a match found, then the app will print the film's details.
# There is no set up required for the API

# I imported the time function to make the user have to wait for the result, increasing their suspense.

# Enjoy!

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
print(f"{user["name"]}, it's nice to meet you! \n\nIf you can kindly share some details with me, I'd like to find your Ghibli doppelganger and recommend you a movie. \n\nIf that sounds ok, let's get spirited away!")

# Ask for the user's inputs
# Creating a themed nickname:
user_gender = input("\nWhat is your gender?")

def nickname(suffix):
    if user_gender == "Male" or user_gender == "male":
        suffix = "-kun"
    elif user_gender == "Female" or user_gender == "female":
        suffix = "-chan"
    else:
        suffix = "-san"

    full_name = (user["name"] + suffix)

    print(f"\nOK! We shall call you " + full_name+"!")
    return full_name

# Define user name outside of function so it can be used again:
user_name = nickname("")

# Collecting hair colour and eye colour
ghibli_hair = input("\nWhat is your hair colour? ").capitalize()

endpoint_hair = f"https://ghibliapi.vercel.app/people?hair_color={ghibli_hair}"
response_hair = requests.get(endpoint_hair)
data_hair = response_hair.json()

# Print the names of matching hair colour characters by requesting to API hair endpoint
hair_name = [person["name"] for person in data_hair]
if hair_name:
    print(", ".join(hair_name) + " has the same hair colour as you!")
else:
    print("\nSorry no match, try again?")

print(f"\nI'm finding so much out about you! One more thing...")

ghibli_eyes = input("\nI can't help getting lost in your eyes, " + user_name +", but what is their colour?").capitalize()

endpoint_eyes = f"https://ghibliapi.vercel.app/people"
response_eyes = requests.get(endpoint_eyes)
data_eyes = response_eyes.json()

# Print the names of matching eye colour characters by accessing the person endpoint on eye colour
eyes_name = [person["name"] for person in data_eyes if person["eye_color"].capitalize() == ghibli_eyes]
if eyes_name:
    print(", ".join(eyes_name) + " has the same eye colour as you!")
else:
    print("\nSorry no match, try again?")

print("\nNow let's see if you have a doppelganger or not...")

# time module
time.sleep(3.0)

# Doppelganger finder iterates the names in hair_name and eyes_name lists and if matching
# prints the doppelganger. Results stored in doppelgangers file.
doppelganger_name = [name for name in hair_name if name in eyes_name]

if doppelganger_name:
    print("\nYour Ghibli doppelganger is: " + ", ".join(doppelganger_name))
    file = open("/Users/sallydavies/Desktop/CFG Degree/CFG-Assignments/assignment_2_python/doppelgangers", "a+")
    file.write(f"\n {user_name} looks like {doppelganger_name}")
    file.close()
else:
    print("\nSorry no match...")

# Connecting doppelganger with films and producing a recommendation

interest_cha = input("\nWhich character would you search in movies?").capitalize()

endpoint_films = f"https://ghibliapi.vercel.app/films"
response_films = requests.get(endpoint_films)
data_films = response_films.json()

url_name = [person["films"] for person in data_eyes if person["name"].capitalize() == interest_cha]

# Make the list of lists into one list so that all urls can be searched in for loop
urls_all = [url for sublist in url_name for url in sublist]

# If the person and film URLs match, the films information will be requested from the films endpoint
if url_name:
    print(interest_cha + f" is in the following film:\n")
for film in data_films:
        if film["url"] in urls_all:
            print(f"{film["title"]}, \n Which was produced by the world-famous {film["director"]}.")
            release_year = str(film["release_date"])
            print(f"It was released in '" + release_year[2:4])
            print(f"Here is a quick description: \n {film["description"]}")
            print(f"This film garnered a Rotten Tomatoes score of {film["rt_score"]} /100, why don't you check it out?!")
            file = open("/film_recommendations.txt", "a+")
            file.write(f"{film["title"]}")
            file.close()
else:
    print("\nSorry no match, try again?")

print("I hope you enjoyed the Ghibli quiz! ありがとうございました")
print("	♡＼(￣▽￣)／♡")


# How I'd like to improve:
# Recursion - if there is no match then being able to repeat that input again
# Be able to connect related colours of hair and eyes, so that there are more matches (some of the colour names are too specific)
# Make a response that is relevant to the Rotten Tomatoes score, e.g if bad, ask to suggest another.