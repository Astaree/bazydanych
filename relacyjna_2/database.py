import sqlite3


class Database:
    def __init__(self):
        self.connection = sqlite3.connect("./baza.db")
        self.connection.row_factory = sqlite3.Row
        self.cursor = self.connection.cursor()

    def get_keys(self):
        keys = self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
        table_names = [key[0] for key in keys]
        table_names = table_names[1:]
        return table_names

    def get_column(self, table):
        query = "SELECT * FROM {}".format(table)
        ret = self.cursor.execute(query).description
        columns = list(map(lambda x: x[0], ret))
        return columns

    def get(self, table=None):
        if table is None:
            return "Table parameter is missing"
        sql_query = "SELECT * FROM {}".format(table)
        self.cursor.execute(sql_query)
        result = self.cursor.fetchall()
        return result
