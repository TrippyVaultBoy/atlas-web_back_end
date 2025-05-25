#!/usr/bin/env python3
"""
Write a function called filter_datum that returns the log message obfuscated
"""
from typing import List
import re


def filter_datum(fields: List[str],
                 redaction: str,
                 message: str,
                 separator: str) -> str:
    """
    filter_datum function
    """
    pattern = r'(' + '|'.join(fields) + r')=[^' + re.escape(separator) + r']*'
    masked = re.sub(pattern, lambda m: f"{m.group(1)}={redaction}", message)
    return masked
