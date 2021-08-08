# Topic: Customized library file to connect to databases using mysql library
# Ask user questions for information and connect to database
# Author: Xuhua Huang
#
# Last updated: Aug 8, 2021
# Created on: Aug 8, 2021

import mysql.connector

# ----------------------------------------------------------------------------------------------------------------------
# custom dictionary to contains all the sensitive information
# to connect to database as if we are doing it manually
sql_connection: dict = {
    'host_database': '',
    'username': '',
    'password': ''
}
# ----------------------------------------------------------------------------------------------------------------------


class SQLConnection:
    def __init__(self,
                 schemas_name: str = None) -> None:
        self._host: str = sql_connection['host_database']
        self._data_base: str = schemas_name
        self._username: str = sql_connection['username']
        self._password: str = sql_connection['password']

    def get_sql_connection(self):
        return mysql.connector.connect(host=self._host,
                                       user=self._username,
                                       password=self._password,
                                       database=self._data_base,
                                       charset='utf8mb4')


def main():
    my_sql: SQLConnection = SQLConnection(schemas_name='DEFAULT')
    _aws_conn = my_sql.get_sql_connection()
    _aws_cursor = _aws_conn.cursor()
    _aws_cursor.execute('SELECT * FROM `DEFAULT`.TL_measures ORDER BY creation_date_utc desc limit 100;')
    print(_aws_cursor.fetchall())


if __name__ == '__main__':
    main()
