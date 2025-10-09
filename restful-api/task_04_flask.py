#!/usr/bin/python3
"""
Created an API with Flask
"""


from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}
user_keys = ["username", "name", "age", "city"]


@app.route("/", methods=["GET"])
def home():
    """
    Home page
    """
    return "Welcome to the Flask API!"


@app.route("/data", methods=["GET"])
def json_data():
    """
    Display user names
    """
    users_names = []
    for i in users:
        users_names.append(i)
    return jsonify(users_names)


@app.route("/status", methods=["GET"])
def show_status():
    """
    Display status
    """
    return "OK"


@app.route("/users/<username>", methods=["GET"])
def user_info(username):
    """
    Display user information based on username
    """
    if users.get(username) is not None:
        return jsonify(users.get(username))
    else:
        return {"error": "User not found"}


@app.route("/add_user", methods=["POST"])
def add_user():
    """
    Add a user 
    """
    new_user = request.get_json()
    for i in new_user:
        if i not in user_keys:
            return {"error": "Username is required"}
    users[new_user["username"]] = new_user
    return {"message": "User added", "user": new_user}


if __name__ == "__main__":
    app.run()
