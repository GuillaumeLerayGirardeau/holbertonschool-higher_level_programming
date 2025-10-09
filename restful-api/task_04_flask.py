#!/usr/bin/env python3
"""Create an API with Flask."""
from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}
user_keys = ["username", "name", "age", "city"]


@app.route("/", methods=["GET"])
def home():
    """Home page."""
    return "Welcome to the Flask API!", 200


@app.route("/data", methods=["GET"])
def json_data():
    """Display user names."""
    users_names = []
    for i in users:
        users_names.append(i)
    return jsonify(users_names), 200


@app.route("/status", methods=["GET"])
def show_status():
    """Display status."""
    return "OK", 200


@app.route("/users/<username>", methods=["GET"])
def user_info(username):
    """Display user information based on username."""
    if users.get(username) is not None:
        return jsonify(users.get(username)), 200
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """Add a user."""
    new_user = request.get_json()
    for i in new_user:
        if i not in user_keys:
            return jsonify({"error": "Username is required"}), 400
    users[new_user["username"]] = new_user
    return jsonify({"message": "User added", "user": new_user}), 201


if __name__ == "__main__":
    app.run()
