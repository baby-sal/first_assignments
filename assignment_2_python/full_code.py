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
        # inbuilt print function (#1)
        print(letter)

user["name"] = input("Hello friend, how do I spell your name?")

read_out_my_name(user["name"])

# Explain the program to the user:
print(f"{user["name"]}, it's nice to meet you! \n\nIf you can kindly share some details with me, I'd like to find your Ghibli doppelganger and recommend you a movie. \n\nIf that sounds ok, let's get spirited away!")

# Ask for the user's inputs
# Creating a themed nickname:
user_gender = input("\nWhat is your gender?")

# if else usage
def nickname(suffix):
    if user_gender == "Male" or user_gender == "male":
        suffix = "-kun"
    elif user_gender == "Female" or user_gender == "female":
        suffix = "-chan"
    else:
        suffix = "-san"

    full_name = (user["name"] + suffix)
    # usage of return
    print(f"\nOK! We shall call you " + full_name+"!")
    return full_name

# Define user name outside of function so it can be used again:
user_name = nickname("")

# Collecting hair colour and eye colour
ghibli_hair = input("\nWhat is your hair colour? ").capitalize()

#Usage of API
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
    # writing results to a separate file (doppelgangers.txt)
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
# for loop usage
if url_name:
    print(interest_cha + f" is in the following film:\n")
for film in data_films:
        if film["url"] in urls_all:
            print(f"{film["title"]}, \n Which was produced by the world-famous {film["director"]}.")
            #str inbuilt function (#2)
            release_year = str(film["release_date"])
            # string slicing
            print(f"It was released in '" + release_year[2:4])
            print(f"Here is a quick description: \n {film["description"]}")
            print(f"This film garnered a Rotten Tomatoes score of {film["rt_score"]} /100, why don't you check it out?!")
            file = open("/film_recommendations.txt", "a+")
            #writing results to a separate file (film_recommendations.txt)
            file.write(f"{film["title"]}")
            file.close()
else:
    print("\nSorry no match, try again?")

print("I hope you enjoyed the Ghibli quiz! ありがとうございました")
print("	♡＼(￣▽￣)／♡")