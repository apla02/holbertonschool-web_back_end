#!/usr/bin/env python3
"""
Main file
"""
import requests


def register_user(email: str, password: str) -> None:
    """ Create a new user
    """
    data = {
        'email': email,
        'password': password
    }
    response = requests.post('http://localhost:5000/users', data)
    assert response.status_code == 200


def log_in_wrong_password(email: str, password: str) -> None:
    """ Valid login with a wrong password
    """
    url = 'http://localhost:5000/sessions'
    data = {
        'email': email,
        'password': password
    }
    response = requests.post(url, data)
    assert response.status_code == 401


def log_in(email: str, password: str) -> str:
    """ Valid loging with right data
    """
    url = 'http://localhost:5000/sessions'
    data = {
        'email': email,
        'password': password
    }
    response = requests.post(url, data)
    assert response.status_code == 200
    return response.cookies['session_id']


def profile_unlogged() -> None:
    """ cancel login without session
    """
    response = requests.get('http://localhost:5000/profile')
    assert response.status_code == 403


def profile_logged(session_id: str) -> None:
    """ cancel login from someone logged
    """
    url = 'http://localhost:5000/profile'
    data = {
        'session_id': session_id
    }
    response = requests.get(url, cookies=data)
    assert response.status_code == 200


def log_out(session_id: str) -> None:
    """ log out from the application
    """
    url = 'http://localhost:5000/sessions'
    data = {
        'session_id': session_id
    }
    response = requests.delete(url, cookies=data)
    assert response.status_code == 200


def reset_password_token(email: str) -> str:
    """ Reset password token
    """
    url = 'http://localhost:5000/reset_password'
    data = {
        'email': email
    }
    response = requests.post(url, data)
    assert response.status_code == 200
    return response.json()['reset_token']


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """ Update password and reset toke
    """
    url = 'http://localhost:5000/reset_password'
    data = {
        'email': email,
        'new_password': new_password,
        'reset_token': reset_token
    }
    response = requests.put(url, data)
    assert response.status_code == 200


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


if __name__ == "__main__":
    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
