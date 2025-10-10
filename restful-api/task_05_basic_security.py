#!/usr/bin/env python3
"""
Create an API with basic security tests
"""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager,create_access_token, jwt_required, get_jwt_identity)

app = Flask(__name__)
auth = HTTPBasicAuth
app.config["JWT_SECRET_KEY"] = "secret-key"
jwt = JWTManager(app)

users = {
    "user1": {"username": "user1", 
              "password": generate_password_hash("Columbo"), "role": "user"},
    "admin1": {"username": "admin1", 
               "password": generate_password_hash("Pokemon"), "role": "admin"}
}
@app.route("/")
def home():
    """
    Home Page
    """
    return "Bonjour"

@auth.verify_password
def verify_password(username, password):
    """
    Verify Password
    """
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        return username

@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    """
    Login accepted
    """
    return "Basic Auth: Access Granted"

@app.route('/login', methods=['POST'])
def login():
    """
    User has to login
    """
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    user = users.get(username)

    if not user or not check_password_hash(user['password'], password):
        return jsonify({"error": "Invalid credentials"}), 401

    access_token = create_access_token(
        identity={"username": username, "role": user["role"]})
    return {"access token": jsonify(access_token=access_token)}

@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    """
    Message if JWT is accepted
    """
    return "JWT Auth: Access Granted"

@app.route('/admin-only')
@jwt_required()
def admin_only():
    """
    Admin only access
    """
    identity = get_jwt_identity()
    if identity["role"] != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"

@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """
    Return error message
    """
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """
    Return error message
    """
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(err):
    """
    Return error message
    """
    return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    """
    Return error message
    """
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    """
    Return error message
    """
    return jsonify({"error": "Fresh token required"}), 401
