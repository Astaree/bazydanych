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

    def create_entry(self, table: str = None, columns=[], query=[]):
        query_data = {}
        sql_query = ""

        for i, q in enumerate(query):
            if q != '':
                query_data[columns[i]] = q

        if len(query_data) > 0:
            sql_query = "INSERT INTO {} (".format(table)
            sql_query += ", ".join(query_data.keys())
            sql_query += ") VALUES ("
            sql_query += ", ".join("'" + value + "'" for value in query_data.values())
            sql_query += ");"
        print(sql_query)
        try:
            self.cursor.execute(sql_query)
            self.connection.commit()
            print("Insertion successful.")
        except sqlite3.OperationalError as e:
            print("Insertion failed: {}".format(e))

    def delete_entry(self, table: str = None, selected_entry=None):
        try:
            entry_id = selected_entry[:selected_entry.find("|") - 1]
            sql_query = "DELETE FROM {} WHERE id = ?".format(table)

            self.cursor.execute(sql_query, (entry_id,))
            self.connection.commit()
            print("Delete successful.")
        except sqlite3.Error as e:
            print("Delete failed: {}".format(e))

    def update_entry(self, table=None, selected_entry=None, columns=[], query=[]):
        print(table)
        print(selected_entry)
        print(columns)
        print(query)
        try:
            entry_id = selected_entry.split(" | ")[0]  # Extract the entry ID from the selected_entry string
            query_data = {}
            sql_query = "UPDATE {} SET".format(table)

            for i, q in enumerate(query):
                if q != '':
                    query_data[columns[i]] = q

            if len(query_data) > 0:
                for column in query_data:
                    sql_query += " {} = '{}',".format(column, query_data[column])

                sql_query = sql_query[:-1]
                sql_query += " WHERE id = ?"

                print(sql_query)
                self.cursor.execute(sql_query, entry_id)
                self.connection.commit()
                print("Update successful.")
        except sqlite3.Error as e:
            print("Update failed: {}".format(e))
