#!/usr/bin/env python3
"""
Write a function called filter_datum that returns the log message obfuscated
"""
from typing import List
import re
import logging
import os
import mysql.connector
from mysql.connector import Error


PII_FIELDS = ("name", "email", "password", "phone", "ssn")


def main() -> None:
    """
    main function
    """

    fields = PII_FIELDS
    redaction = '***'
    separator = ';'

    connection = get_db()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users;")

    column_names = []
    for column_description in cursor.description:
        column_name = column_description[0]
        column_names.append(column_name)

    for row in cursor:

        key_value_pairs = []

        for index in range(len(column_names)):
            key = column_names[index]
            value = row[index]
            pair = f"{key}={value}"
            key_value_pairs.append(pair)

        formated_message = separator.join(key_value_pairs)

        print(filter_datum(fields, redaction, formated_message, separator))

    cursor.close()
    connection.close()


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
    logger.propagate = False

    logger.handlers = []

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    stream_handler.setFormatter(RedactingFormatter(list(PII_FIELDS)))

    logger.addHandler(stream_handler)

    return logger


"""
PERSONAL_DATA_DB_USERNAME=app_user
PERSONAL_DATA_DB_PASSWORD=app_password
PERSONAL_DATA_DB_HOST=localhost
PERSONAL_DATA_DB_NAME=my_db
./main.py
"""


def get_db() -> mysql.connector.connection.MySQLConnection:
    """
    get_db method
    """
    username = os.getenv('PERSONAL_DATA_DB_USERNAME', 'app_user')
    password = os.getenv('PERSONAL_DATA_DB_PASSWORD', '')
    host = os.getenv('PERSONAL_DATA_DB_HOST', 'localhost')
    database = os.getenv('PERSONAL_DATA_DB_NAME')

    try:
        connection = mysql.connector.connect(
            user=username,
            password=password,
            host=host,
            database=database
        )
        if connection.is_connected():
            return connection
    except Error as error:
        print(f"Connection failed: {error}")
        return None


if __name__ == "__main__":
    main()
