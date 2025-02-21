from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (JWTManager, create_access_token,
                                jwt_required, get_jwt_identity)

app = Flask(__name__)
auth = HTTPBasicAuth()
app.config["JWT_SECRET_KEY"] = "your_jwt_secret_key"
jwt = JWTManager(app)

users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


@auth.verify_password
def verify_password(username, password):
    """
    Verify the username and password for basic authentication.

    Args:
        username (str): The username to verify.
        password (str): The password to verify.

    Returns:
        dict or None: The user dictionary if credentials are valid,
        None otherwise.
    """
    if username in users and check_password_hash(
            users[username]["password"], password):
        return username
    return None


@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    """
    Endpoint protected by basic authentication.

    Returns:
        str: A message indicating successful access.
    """
    return "Basic Auth: Access Granted"


@app.route('/login', methods=['POST'])
def login():
    """
    Endpoint for user login and JWT token generation.

    Returns:
        flask.Response: JSON response with access token or error message.
    """
    data = request.get_json()

    if not data or 'username' not in data or 'password' not in data:
        return jsonify({"error": "Invalid username or password"}), 401

    username = data['username']
    password = data['password']

    if username in users and check_password_hash(
            users[username]["password"], password):
        access_token = create_access_token(
            identity={
                "username": username,
                "role": users[username]["role"]
            }
        )
        return jsonify({"access_token": access_token})

    return jsonify({"error": "Invalid credentials"}), 401


@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    """
    Endpoint protected by JWT authentication.

    Returns:
        str: A message indicating successful access.
    """
    return "JWT Auth: Access Granted"


@app.route('/admin-only')
@jwt_required()
def admin_only():
    """
    Endpoint accessible only to users with admin role.

    Returns:
        str or flask.Response: A success message or error response.
    """
    current_user = get_jwt_identity()
    if current_user['role'] != 'admin':
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """
    Handle unauthorized access attempts (missing token).

    Args:
        err: The error object.

    Returns:
        flask.Response: JSON response with error message.
    """
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """
    Handle invalid token errors.

    Args:
        err: The error object.

    Returns:
        flask.Response: JSON response with error message.
    """
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(header, payload):
    """
    Handle expired token errors.

    Args:
        err: The error object.

    Returns:
        flask.Response: JSON response with error message.
    """
    return jsonify({"error": "Token has expired"}), 401


if __name__ == "__main__":
    app.run(port=5000)
