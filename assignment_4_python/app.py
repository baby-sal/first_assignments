from flask import Flask, jsonify, request
from requests import delete
from db_utils import get_all_food, get_all_reviews, delete_review_by_id_db

app = Flask(__name__)

@app.route("/food", methods=["GET"])
def get_food():
    return jsonify(get_all_food())


@app.route("/reviews", methods=["GET"])
def get_reviews():
    return jsonify(get_all_reviews())


@app.route("/reviews/delete/<int:id>", methods=["DELETE"])
def delete_review_by_id(id):
    return jsonify(delete_review_by_id_db(id))

if __name__ == "__main__":
    app.run(debug=True)