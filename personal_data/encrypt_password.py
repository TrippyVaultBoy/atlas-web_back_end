#!/usr/bin/env python3
"""
Implement a hash_password function that expects
one string argument name password and returns a
salted, hashed password, which is a byte string
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    turns a password into hashbrowns
    """

    password_to_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt(rounds=12)
    password_hashbrowns = bcrypt.hashpw(password_to_bytes, salt)

    return password_hashbrowns


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    is_valid function
    """

    password_to_bytes = password.encode('utf-8')
    return bcrypt.checkpw(password_to_bytes, hashed_password)
