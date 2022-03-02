#!/usr/bin/env python3
""" create password encrypted
"""
# import concrete
from db import DB
from user import User

# Universal importation
import bcrypt
import uuid

# from slqalchemy
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """create password encrypted
    """
    psw = password.encode('utf-8')
    hashed = bcrypt.hashpw(psw, bcrypt.gensalt())
    return hashed


def _generate_uuid() -> str:
    """ generate a uniq identifier
    """
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ register a new user
        """
        try:
            user = self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists.")
        except NoResultFound:
            psw = _hash_password(password)
            new_user = self._db.add_user(email, psw)
            return new_user

    def valid_login(self, email: str, password: str) -> bool:
        """ Valid login user authentication
        """
        try:
            user = self._db.find_user_by(email=email)
        except Exception:
            return False

        if bcrypt.checkpw(password.encode('utf-8'),
                          user.hashed_password) and user:
            return True
        else:
            return False

    def create_session(self, email: str) -> str:
        """ create a session and update it
        """
        try:
            user = self._db.find_user_by(email=email)
        except Exception:
            return None
        session = _generate_uuid()
        self._db.update_user(user.id, session_id=session)
        user_up = self._db.find_user_by(email=email)
        return session

    def get_user_from_session_id(self, session_id: str) -> User:
        """ search an user per session id
        """
        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """ destroy session
        """
        try:
            user = self._db.find_user_by(id=user_id)
        except Exception:
            return None

        self._db.update_user(user.id, session_id=None)
        return None

    def get_reset_password_token(self, email: str) -> str:
        """ update reset token
        """
        try:
            user = self._db.find_user_by(email=email)
        except Exception:
            raise ValueError
        identifier = _generate_uuid()
        self._db.update_user(user.id, reset_token=identifier)
        return identifier

    def update_password(self, reset_token: str, password: str) -> None:
        """ update password and reset token
        """
        try:
            user = self._db.find_user_by(reset_token=reset_token)
            new_password = _hash_password(password)
            self._db.update_user(user.id, hashed_password=new_password,
                                 reset_token=None)
            return None
        except Exception:
            raise ValueError
