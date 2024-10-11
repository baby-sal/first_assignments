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

def get_all_food_():
    endpoint = "http://127.0.0.1:5000/food"
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




if __name__ == "__main__":
    main()
