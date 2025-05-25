#!/usr/bin/env python3
"""
Write a function called filter_datum that returns the log message obfuscated
"""
import re


def filter_datum(fields, redaction, message, separator):
    pattern = r'(' + '|'.join(fields) + r')=[^' + re.escape(separator) + r']*'
    masked = re.sub(pattern, lambda m: f"{m.group(1)}={redaction}", message)
    return masked
