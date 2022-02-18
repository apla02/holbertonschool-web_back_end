#!/usr/bin/env python3
"""
Handle all Routes module for the Session authentication
"""
from api.v1.views import app_views
from flask import jsonify, request
from os import getenv


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def handle_all_routes():
    """POST: api/v1/auth_session/login/
    """
    email = request.form.get('email')
    if email is None or email == "":
        return jsonify({"error": "email missing"}), 400
    pwd = request.form.get('password')
    if pwd is None or pwd == "":
        return jsonify({"error": "password missing"}), 400

    from models.user import User
    try:
        search_user = User.search({'email': email})
        if search_user == []:
            return jsonify({"error": "no user found for this email"}), 404
    except Exception:
        return None

    for user in search_user:
        if not user.is_valid_password(pwd):
            return jsonify({"error": "wrong password"}), 401

    from api.v1.app import auth

    session_id = auth.create_session(search_user[0].id)
    Name = getenv('SESSION_NAME')
    result = jsonify(search_user[0].to_json())
    result.set_cookie(Name, session_id)
    return result


@app_views.route('/auth_session/logout', methods=['DELETE'],
                 strict_slashes=False)
def delete_session():
    """ DELETE: /api/v1//auth_session/logout/
    Delete a session ID
    """
    from api.v1.app import auth

    if auth.destroy_session(request) is None:
        abort(404)
    else:
        return jsonify({}), 200
