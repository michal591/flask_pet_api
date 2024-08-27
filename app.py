from flask import Flask, jsonify, request

# Create an instance of the Flask class
app = Flask(__name__)

pet1 = {
    "id": 1,
    "name": "Dixie",
    "age": 5,
    "image": "https://t4.ftcdn.net/jpg/01/99/00/79/360_F_199007925_NolyRdRrdYqUAGdVZV38P4WX8pYfBaRP.jpg",
}
pet2 = {
    "id": 2,
    "name": "Charlie",
    "age": 2,
    "image": "https://images.pexels.com/photos/1108099/pexels-photo-1108099.jpeg",
}

# "id": 3,"name": "Charlie","age": 2,"image": "https://images.pexels.com/photos/1108099/pexels-photo-1108099.jpeg",

pets = [pet1, pet2]


# Define a route for the root URL
@app.route("/")
def pets_list():
    return pets


@app.route("/", methods=["POST"])
def add_pet():
    new_pet = request.get_json()
    pets.append(new_pet)
    return jsonify({"result": "added succseful"})


@app.route("/pet/<id>/")
def single_pets(id):
    try:
        for pet in pets:
            if pet["id"] == int(id):
                return pet
    except:
        print("error in id")
    return jsonify({"result": "pet not found"})


@app.route("/pet/<id>/", methods=["DELETE"])
def delete_pets(id):
    try:
        for pet in pets:
            if pet["id"] == int(id):
                pets.remove(pet)
                return jsonify({"result": "pet delete"})
    except:
        print("error in id")
    return jsonify({"result": "pet not found"})


@app.route("/pet/<id>/", methods=["PUT"])
def update_pets(id):
    try:
        for pet in pets:
            if pet["id"] == int(id):
                new_update_pet = request.get_json()
                pets.remove(pet)
                pets.append(new_update_pet)
                return jsonify({"result": "update succseful"})
    except:
        print("error in id")
    return jsonify({"result": "pet not found"})


# Run the app only if this script is executed (not imported)
if __name__ == "__main__":
    app.run(debug=True)
