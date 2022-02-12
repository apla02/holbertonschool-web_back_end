#!/usr/bin/env python3
""" log message obfuscated
"""
import re
from typing import List
import logging
import mysql.connector
from mysql.connector import connection, cursor
from os import getenv


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """return string obfuscated
    """
    for field in fields:
        message = re.sub(f"{field}=.*?{separator}",
                         f"{field}={redaction}{separator}", message)
    return message


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """ Redacting Formatter class
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Log formatter
        """
        return filter_datum(self.fields,
                            self.REDACTION,
                            super(RedactingFormatter,
                                  self).format(record),
                            self.SEPARATOR)


def get_logger() -> logging.Logger:
    """Create logger
    Returns:
        logging.Logger: a Logger object.
    """
    logger = logging.getLogger("user_data")
    logger.propagate = False
    s_handler = logging.StreamHandler()
    s_handler.setLevel(logging.INFO)
    formatter = RedactingFormatter(PII_FIELDS)
    s_handler.setFormatter(formatter)
    logger.addHandler(s_handler)
    return logger


def get_db() -> connection.MySQLConnection:
    """ Connect python to a DB
    """
    config = {
        'user': getenv('PERSONAL_DATA_DB_USERNAME', "root"),
        'password': getenv('PERSONAL_DATA_DB_PASSWORD', ""),
        'host': getenv('PERSONAL_DATA_DB_HOST', "localhost"),
        'database': getenv('PERSONAL_DATA_DB_NAME'),
    }

    cnx = connection.MySQLConnection(**config)
    return cnx


def main():
    """ run when the module is executed.
    """
    database = get_db()
    cursor = database.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users;")
    for row in cursor:
        message = ''
        for k in row:
            message += f'{k}={row[k]}; '
        log_record = logging.LogRecord("user_data", logging.INFO,
                                       None, None, message, None, None)
        formatter = RedactingFormatter(fields=("email", "ssn",
                                       "password", 'name'))
        print(formatter.format(log_record))
    cursor.close()
    database.close()


if __name__ == '__main__':
    main()
