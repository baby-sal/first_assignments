# Implement 2 API endpoints with appropriate functionality Implement one additional endpoint of your choice can be POST or GET (APP)


from flask import Flask, jsonify, request
from db_utils import get_all_food

app = Flask(__name__)

import requests

@app.route("/food/<int:food_id>", methods=["GET"])
def get_food(food_id):
    return jsonify(get_all_food())


@app.route("/review/add", methods=["POST"])
def add_review():



###This was from other file you created called 'app'

if __name__ == "__main__":
    app.run(debug=True)