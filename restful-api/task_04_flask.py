from flask import Flask
from flask import jsonify
from flask import request


app = Flask(__name__)


users = {}


@app.route('/')
def home():
    """
    Home Endpoint

    Returns:
        str: Welcome Message.
    """
    return "Welcome to the Flask API!"


@app.route('/data')
def get_usernames():
    """
    Endpoint to get all usernames.

    Returns:
        flask.Response: JSON containing a list of all usernames.
    """
    return jsonify(list(users.keys()))


@app.route('/status')
def get_status():
    """
    Endpoint to check API Status

    Returns:
        str: "OK" if the API is running.
    """
    return "OK"


@app.route('/users/<username>')
def get_user(username):
    """
    Endpoint to get user info

    Args:
        username (str): The user name to get info from
    Returns:
        flask.Response: JSON Response to get user info
        if not found = error 404
    """
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    """
    Endpoint to add a new user.

    Expects a JSON payload with user information, including a 'username' field.

    Returns:
        flask.Response: A JSON response confirming the addition of the user,
        or an error message if the username is missing.
    """
    data = request.get_json()
    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400
    users[username] = data
    return jsonify({"message": "User added", "user": data}), 201


if __name__ == "__main__":
    app.run()
