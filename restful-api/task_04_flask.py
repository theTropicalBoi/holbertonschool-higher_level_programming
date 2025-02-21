from flask import Flask, jsonify, request

app = Flask(__name__)
users = {
    "jane": {
        "name": "Jane",
        "age": 28,
        "city": "Los Angeles"
    }
}


@app.route("/")
def home():
    """ Home Endpoint
    Returns:
        str: Welcome Message.
    """
    return "<p>Hello World !</p>"


@app.route("/data")
def get_data():
    """ Endpoint to get all usernames.
    Returns:
        flask.Response: JSON containing a list of all usernames.
    """
    return jsonify(list(users.keys()))


@app.route("/status")
def get_status():
    """ Endpoint to check API Status
    Returns:
        str: "OK" if the API is running.
    """
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    """ Endpoint to get user info
    Args:
        username (str): The user name to get info from
    Returns:
        flask.Response: JSON Response to get user info
        if not found error 404
    """
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


app.route("/add_user", methods=['POST'])
def add_user():
    data = request.get_json()
    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400
    users[username] = data
    return jsonify({"message": "User added", "user": data}), 201


if __name__ == "__main__":
    app.run()
