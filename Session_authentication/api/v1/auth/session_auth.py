#!/usr/bin/env python3
"""
session_auth module
"""
from api.v1.auth.auth import Auth
from models.user import User
from uuid import uuid4


class SessionAuth(Auth):
    """
    SessionAuth class
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        create_session method
        """

        if user_id is None or not isinstance(user_id, str):
            return None
        else:
            session_id = str(uuid4())
            SessionAuth.user_id_by_session_id[session_id] = user_id
            return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        user_id_for_session_id method
        """

        if session_id is None or not isinstance(session_id, str):
            return None
        else:
            return SessionAuth.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """
        current_user method
        """

        session_id = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_id)
        if user_id is None:
            return None
        return User.get(user_id)
