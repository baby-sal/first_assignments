import requests
import json
from time import sleep


def get_all_food_fe():
    endpoint = "http://127.0.0.1:5000/food"
    get_result = requests.get(endpoint).json()
    return get_result

def get_all_reviews_fe():
    endpoint = "http://127.0.0.1:5000/reviews"
    get_result = requests.get(endpoint).json()
    return get_result

def delete_review_using_id_fe(id):
    endpoint = f"http://127.0.0.1:5000/reviews/delete/{id}"
    delete_result = requests.delete(endpoint).json()
    return delete_result

def run():
    print("Did someone say FOOD?!")
    print( )
    sleep(2)
    print("Would you like to:")
    print("1. Browse Japanese regional delicacies")
    print("2. Read the reviews of various delicacies")
    print("3. Delete a review from the database")
    print( )
    choice = input("Please select 1, 2 or 3?: ").strip()

    if choice == "1":
        if get_all_food_fe() is None:
            print("No food here...")
        print(get_all_food_fe())

    elif choice == "2":
        if get_all_reviews_fe() is None:
            print("No reviews here...")
        print(get_all_reviews_fe())

    elif choice == "3":
        reviews = get_all_reviews_fe()
        print("Here are the current reviews:")
        print(reviews)
        if reviews is not None:
            delete_review_id = input("Which review should we delete?").strip()
            print("Review removed from the database. Thank you")
            print("Please see the updated database:")
            print(delete_review_using_id_fe(delete_review_id))

        else:
            print("Unable to load reviews. 申し訳ございませんでした")

    else:
        print("Incorrect entry, please choose again")



if __name__ == "__main__":
    run()
