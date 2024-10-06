from flask import Flask, jsonify

app = Flask(__name__)

import requests

def get_food():
    endpoint = "http://127.0.0.1:5000/food/"
    data = requests.get(endpoint).json()
    return data
