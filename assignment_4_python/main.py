#requests go here (client side) where the main program starts from

##check hp main example
## check the flights api example

##Make a POST for people to add reviews to the review table.

# Implement client-side for each of the 3 API endpoints you have created. (MAIN)
#+ In main.py have a run() function/call the functions to simulate the planned interaction
# with the API, this could include welcome statements, displaying etc., (hairdressers
# booking example from lesson) (MAIN)
import requests

def get_all_food_fe():

    endpoint = "http://127.0.0.1:5000/food"
    result = requests.get(endpoint).json()
    return result

if __name__ == "__main__":
    main()
# def delete_character_by_id(id):
#     endpoint = f"http://127.0.0.1:5000/characters/remove/{id}"
#     result = requests.delete(endpoint).json()
#     return result