#!/usr/bin/env python3
""" Session Expiration to timeout an user
"""
from api.v1.auth.session_auth import SessionAuth
from os import getenv
from datetime import datetime, timedelta


class SessionExpAuth(SessionAuth):
    """ initial to define attribute duration
    """

    def __init__(self):
        """ initial to define attribute duration
        """
        try:
            self.session_duration = int(getenv('SESSION_DURATION', 0))
        except ValueError:
            self.session_duration = 0

    def create_session(self, user_id=None):
        """ Overload session create
        """
        session_id = super().create_session(user_id)
        if session_id is None:
            return None
        session_dictionary = {
            'user_id': user_id,
            'created_at': datetime.now()
        }
        self.user_id_by_session_id[session_id] = session_dictionary
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """ assing new dict to dict into class father user_id_for_session_id
        """
        if session_id is None:
            return None
        session_dict = self.user_id_by_session_id.get(session_id)
        if session_dict is None:
            return None

        if self.session_duration <= 0:
            return session_dict.get('user_id')

        created_time = session_dict.get('created_at')
        Session = timedelta(seconds=self.session_duration)
        exp_time = created_time + Session

        if exp_time < datetime.now():
            return None
        return session_dict.get('user_id')
