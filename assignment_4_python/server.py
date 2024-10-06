from flask import Flask, jsonify
app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=True)

@app.route ("/food/<int:food_id>", methods=["GET"])
def get_food(food_id):
    print("ID in server is:" + str(food_id))
    foods = [foods for foods in food if foods["id"] == food_id]
    return jsonify(foods)

@app.route ("/region/<int:region_id>", methods=["GET"])
def get_region(region_id):
    print("ID in server is:" + str(region_id))
    regions = [regions for regions in region if regions["id"] == region_id]
    return jsonify(regions)


## check the flights api example
##Make a POST for people to add reviews to the review table.