from flask import Flask, jsonify

app = Flask(__name__)

import requests

@app.route("/food/<int:food_id>", methods=["GET"])
def get_food(food_id):
    endpoint = "http://127.0.0.1:5000/food/"
    data = requests.get(endpoint).json()
    return data

@app.route("/review/add", methods=["POST"])
def add_review():
    endpoint_2 = "http://127.0.0.1:5000/review/"
    data = requests.get(endpoint_2).json()
    return data