#!/usr/bin/env python3
"""
Write a function called filter_datum that returns the log message obfuscated
"""
from typing import List
import re
import logging
import sys


PII_FIELDS = ("name", "email", "password", "ssn", "ip")


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.__fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        format method
        """
        message = super().format(record)
        return filter_datum(self.__fields,
                            self.REDACTION,
                            message,
                            self.SEPARATOR)


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


def get_logger() -> logging.Logger:
    """
    get_logger function
    """
    logger = logging.getLogger('user_data')
    logging.basicConfig(level=logging.INFO)
    logger.propagate = False

    logger.handlers = []

    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setLevel(logging.INFO)
    stream_handler.setFormatter(RedactingFormatter(list(PII_FIELDS)))

    logger.addHandler(stream_handler)

    return logger
