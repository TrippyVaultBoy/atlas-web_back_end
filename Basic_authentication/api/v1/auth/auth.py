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
        if path is None:
            return True
        if not excluded_paths or excluded_paths is None:
            return True
        if not path.endswith('/'):
            path += '/'
        for excluded in excluded_paths:
            if excluded.endswith('/') and path == excluded:
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """
        authorization_header method
        """

        if request is None:
            return None
        if 'Authorization' not in request.headers:
            return None

        return request.headers.get('Authorization')

    def current_user(self, request=None) -> User:
        """
        current_user method
        """
        return None
