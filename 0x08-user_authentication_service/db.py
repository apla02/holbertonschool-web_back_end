#!/usr/bin/env python3
""" DB module models and connection db
"""
# modules sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError

# import modules done by me
from user import Base
from user import User


class DB:
    """DB module models and connection db
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """ create and add new use inside db
        """
        new_user = User(email=email, hashed_password=hashed_password)
        self._session.add(new_user)
        self._session.commit()
        return new_user

    def find_user_by(self, **keyword) -> User:
        """ search user by argument argument
        """
        try:
            query = self._session.query(User).filter_by(**keyword)
            user = query.first()
        except InvalidRequestError:
            raise InvalidRequestError
        if user is None:
            raise NoResultFound
        else:
            return user

    def update_user(self, user_id: int, **keyword) -> None:
        """ update user by arbitrary argument
        """
        try:
            user = self.find_user_by(id=user_id)
            for k, v in keyword.items():
                if k in user.__dict__:
                    setattr(user, k, v)
                else:
                    raise ValueError
            self._session.commit()
        except Exception:
            raise ValueError
