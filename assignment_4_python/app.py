# Implement 2 API endpoints with appropriate functionality Implement one additional endpoint of your choice can be POST or GET (APP)


from flask import Flask, jsonify, request
from requests import delete

from db_utils import get_all_food, get_all_reviews, delete_review_by_id, add_review

app = Flask(__name__)


@app.route("/food/<int:food_id>", methods=["GET"])
def get_food(food_id):
    return jsonify(get_all_food())


@app.route("/reviews", methods=["GET"])
def get_reviews():
    return jsonify(get_all_reviews())


@app.route("/reviews/delete/<int:id>", methods=["DELETE"])
def delete_review_by_id(id):
    return jsonify(delete_review_by_id(id))


@app.route("/reviews/add", methods=["PUT"])
def add_review():
    review = request.get_json()
    add_review(
        food_id=review["food_id"],
        review_date=review["review_date"],
        review=review["review"],
    )
    return review



###This was from other file you created called 'app'

if __name__ == "__main__":
    app.run(debug=True, port=5000)