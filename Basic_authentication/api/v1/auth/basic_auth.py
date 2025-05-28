#!/usr/bin/env python3
"""
BasicAuth Module
"""
from api.v1.auth.auth import Auth
import base64
from typing import TypeVar


User = TypeVar('User')


class BasicAuth(Auth):
    """
    BasicAuth class
    """

    def extract_base64_authorization_header(
        self, authorization_header: str
    ) -> str:
        """
        extract_base64_authorization_header method
        """

        if authorization_header is None:
            return None
        elif not isinstance(authorization_header, str):
            return None
        elif not authorization_header.startswith('Basic '):
            return None
        else:
            return authorization_header.partition("Basic ")[2]

    def decode_base64_authorization_header(
        self, base64_authorization_header: str
    ) -> str:
        """
        decode_base64_authorization_header method
        """

        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            return decoded_bytes.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(
        self, decoded_base64_authorization_header: str
    ) -> tuple[str, str]:
        """
        extract_user_credentials method
        """

        if decoded_base64_authorization_header is None:
            return (None, None)
        elif not isinstance(decoded_base64_authorization_header, str):
            return (None, None)
        elif ':' not in decoded_base64_authorization_header:
            return (None, None)
        else:
            user = decoded_base64_authorization_header.partition(':')[0]
            password = decoded_base64_authorization_header.partition(':')[2]
            return (user, password)

    def user_object_from_credentials(
        self, user_email: str, user_pwd: str
    ) -> User:
        """
        user_object_from_credentials method
        """

        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None

        try:
            users = User.search({'email': user_email})
        except Exception:
            return None
        
        if not users or not isinstance(users, list):
            return None
        
        for user in users:
            if user.is_valid_password(user_pwd):
                return user

        return None
