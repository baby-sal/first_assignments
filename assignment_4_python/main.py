#requests go here (client side) where the main program starts from

##check hp main example
## check the flights api example

##Make a POST for people to add reviews to the review table.

# Implement client-side for each of the 3 API endpoints you have created. (MAIN)
#+ In main.py have a run() function/call the functions to simulate the planned interaction
# with the API, this could include welcome statements, displaying etc., (hairdressers
# booking example from lesson) (MAIN)
import requests
import json
import time


def get_all_food_fe():
    endpoint = "http://127.0.0.1:5000/food"
    get_result = requests.get(endpoint).json()
    return get_result.json()

def get_all_reviews_fe():
    endpoint = "http://127.0.0.1:5000/reviews"
    get_result = requests.get(endpoint).json()
    return get_result.json()

def delete_review_using_id(id):
    endpoint = f"http://127.0.0.1:5000/reviews/delete/{id}"
    delete_result = requests.delete(endpoint).json()
    return delete_result.json()

def add_review(food_id,review_date,review)

    review = {
        "food_id" : food_id,
        "review_date" : review_date,
        "review" : review,
    }

    put_result = requests.put("http://127.0.0.1:5000/reviews/add",
                              headers={'content-type': 'application/json'},
                              data=json.dumps(review)

    )

    return put_result.json()


def run():
    print("Did someone say FOOD?!")
    print(...)
    time.sleep(3.0)
    print("Would you like to:")
    print("1. Browse Japanese regional delicacies")
    print("2. Add a review for a delicacy")
    print("3. Delete a review from the database")
    choice = input("1, 2 or 3?: ").strip()

    if choice == "1":
        if get_all_food_fe() is None:
            print("No food here...")
        print(get_all_food_fe())

    elif choice == "2":
        food_id = input("Which delicacy did you try? (Between 1 - 47, please revert to question 1 for full information): ")
        review_date = input("What was the date? (YYYY-MM-DD): ")
        review = input("Please share your thoughts in 255 characters or less: ")
        add_review(food_id,review_date,review)
        print("Thank you for your review!")

    elif choice == "3":
        reviews = get_all_reviews_fe()
        print("Here are the current reviews:")
        print(reviews)
        if reviews is not None:
            delete_review_id = input("Which review should we delete?").strip()
            print("Review removed from the database. Thank you")
            print("Please see the updated database:")
            print(delete_review_using_id(delete_review_id))
        else:
            print("Unable to load reviews. 申し訳ございませんでした")

    else:
        print("Incorrect entry, please choose again")



if __name__ == "__main__":
    run()
