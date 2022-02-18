#!/usr/bin/env python3
""" class to manage the API authentication.
"""
from flask import request
from typing import List, TypeVar
from os import getenv


class Auth:
    """ class to manage the API authentication.
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ path required auth
        """
        if path is None:
            return True

        if excluded_paths is None or excluded_paths == []:
            return True

        if path[-1] != "/":
            path = f"{path}/"

        slash_tolerant = [path+"/" if path[-1] != "/" else path
                          for path in excluded_paths]
        if path in excluded_paths or path in slash_tolerant:
            return False
        else:
            return True

    def authorization_header(self, request=None) -> str:
        """ authorization header
        """
        if request is None:
            return None

        response = request.headers.get('Authorization')
        if response:
            return response
        else:
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ current user
        """
        return None

    def session_cookie(self, request=None):
        """ return a cookie value from a request:
        """
        if request is None:
            return None
        session_name = getenv("SESSION_NAME", None)
        return request.cookies.get(session_name)
