#!/usr/bin/env python3
"""
create a class to manage the API authentication
"""
from flask import request
from typing import List, TypeVar


User = TypeVar('User')


class Auth():
    """
    Auth class
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        require_auth method
        """
        return False

    def authorization_header(self, request=None) -> User:
        """
        authorization_header method
        """
        return None

    def current_user(self, request=None) -> User:
        """
        current_user method
        """
        return None
