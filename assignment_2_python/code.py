# **Studio Ghibli Character Generator and Movie Recommendation**
# Which studio Ghibli character do you look like?
# Which studio Ghibli movie do they appear in?
#
# Create a welcome message to explain what the purpose of the program is
# Ask the user to input their gender, hair colour and eye colour
# Send the inputs to the API to return the characters that you have similar features
# If there are more than 3 characters give the option to choose a species you feel relates to you from the options
# Display the characters details and what films they appear in (title, original title, release year, description, rotten tomato score(put highest ranking on top?))

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

    full_name = (user["name"] + suffix)

    print(f"OK! We shall call you " + full_name+"!")
    return full_name
# Collecting hair colour and eye colour

user_name = nickname("")

user_hair_colour = input(user_name+", what is your hair colour?")

print(f"I'm finding so much out about you! One more thing...")

user_eye_colour = input("I can't help getting lost in your eyes, " + user_name +", but what is their colour?")

print(f"What a magical aura you have, " + user_name + ",thank you for sharing!\n Let's find your doppelganger!")

