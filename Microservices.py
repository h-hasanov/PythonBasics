from flask import Flask, jsonify, request, make_response

app = Flask(__name__)

users = {
    "MyName": "123456",
    "MyFriendsName": "78910"
}

addresses = [
    {
        "Name": "MyName MySurname",
        "Address": "MyAddress",
        "City": "MyCity",
        "State": "MyState",
        "Postcode": "UK1"
    }
]

def extractAddress(jsonData):
    result = {
        "Name": jsonData["Name"],
        "Address": jsonData["Address"],
        "City": jsonData["City"],
        "State": jsonData["State"],
        "Postcode": jsonData["Postcode"],
    }
    return result

@app.route("/api/v1/addresses", methods = ["GET"])
def get_addresses():
    return jsonify(addresses)

@app.route("/api/v1/addresses", methods = ["POST"])
def save_Address():
    if request.json is None:
        return make_response(jsonify({'Error': "No Content"}), 400)
    if not "Name" in request.json:
        return make_response(jsonify({'Error': "Missing Key Name"}), 400)
    addresses.append(extractAddress(request.json))
    return jsonify({"Status": "OK", "ID": str(len(addresses))})

@app.route("/api/v1/addresses/<int:addressID>", methods = ["PUT"])
def update_Address(addressID):
    addresses[addressID-1] = extractAddress(request.json)
    return make_response(jsonify({"status": "OK"}), 200)

@app.route("/api/v1/addresses/<int:addressID>", methods = ["DELETE"])
def delete_address(addressID):
    del addresses[addressID-1]
    return make_response(jsonify({"status": "OK"}), 200)

if __name__ == "__main__":
    app.run(debug = True)

