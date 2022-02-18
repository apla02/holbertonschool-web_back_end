#!/usr/bin/env python3
""" Implement a class for basic authentication
"""
from api.v1.auth.auth import Auth
from base64 import b64decode
from typing import TypeVar
from models.user import User


class BasicAuth(Auth):
    """ Implement a class for basic authentication
    """

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """ It returns the Base64 part of the Authorization
        """
        if authorization_header is None:
            return None
        elif not isinstance(authorization_header, str):
            return None
        elif not authorization_header.startswith("Basic "):
            return None
        else:
            return authorization_header.split()[1]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header:
                                           str) -> str:
        """ it returns the decoded value of a Base64 string
        """
        if base64_authorization_header is None:
            return None
        elif not isinstance(base64_authorization_header, str):
            return None
        try:
            b64decode(base64_authorization_header)
        except Exception:
            return None
        return str(b64decode(base64_authorization_header), 'utf-8')

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header:
                                 str) -> (str, str):
        """ returns the user email and password from the Base64 decoded value.
        """
        if decoded_base64_authorization_header is None:
            return (None, None)
        elif not isinstance(decoded_base64_authorization_header, str):
            return (None, None)
        try:
            decoded_base64_authorization_header.split(":")[1]
            decode_base64 = decoded_base64_authorization_header.split(":")
            return (decode_base64[0], decode_base64[1])
        except Exception:
            return (None, None)

    def user_object_from_credentials(self, user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """returns the User instance based on his email and password.
        """
        if user_email is None or type(user_email) is not str:
            return None
        if user_pwd is None or type(user_pwd) is not str:
            return None
        try:
            search_user = User.search({'email': user_email})
        except Exception:
            return None
        for user in search_user:
            if user.is_valid_password(user_pwd):
                return user
            else:
                return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        """
        header_request = self.authorization_header(request)
        if header_request is None:
            return None
        ext_base64 = self.extract_base64_authorization_header(header_request)
        if ext_base64 is None:
            return None
        dec_base64 = self.decode_base64_authorization_header(ext_base64)
        if dec_base64 is None:
            return None
        email, password = self.extract_user_credentials(dec_base64)
        if email is None or password is None:
            return None
        user_credentials = self.user_object_from_credentials(email, password)
        if user_credentials is None:
            return None
        else:
            return user_credentials
