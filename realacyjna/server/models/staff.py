import sqlite3


class StaffModel:
    def __init__(self):
        self.connection = sqlite3.connect('baza.db', isolation_level=None)
        self.cursor = self.connection.cursor()

    def create(self, name, surname):
        query = 'INSERT INTO staff (name, surname) VALUES (?, ?)'
        self.cursor.execute(query, (name, surname))
        self.connection.commit()

    def read_one(self, id):
        query = 'SELECT * FROM staff WHERE id = ?'
        self.cursor.execute(query, (id,))
        result = self.cursor.fetchone()
        if result:
            staff = {
                'id': result[0],
                'name': result[1],
                'surname': result[2]
            }
            return staff

    def read_all(self):
        query = 'SELECT * FROM staff'
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        staff_list = []
        for row in result:
            staff = {
                'id': row[0],
                'name': row[1],
                'surname': row[2]
            }
            staff_list.append(staff)
        return staff_list

    def update(self, id, name=None, surname=None):
        query = 'UPDATE staff SET '
        if name is not None:
            query += 'name = ?, '
        if surname is not None:
            query += 'surname = ?, '
        query = query.rstrip(', ') + ' WHERE id = ?'
        values = [value for value in [name, surname, id] if value is not None]
        self.cursor.execute(query, tuple(values))
        self.connection.commit()

    def delete(self, id):
        query = 'DELETE FROM staff WHERE id = ?'
        self.cursor.execute(query, (id,))
        self.connection.commit()

    def __del__(self):
        self.connection.close()

    def read_by_query(self, id=None, name=None, surname=None):
        query = 'SELECT * FROM staff'
        conditions = []
        values = []

        if id:
            conditions.append('id = ?')
            values.append(id)
        if name:
            conditions.append('name = ?')
            values.append(name)
        if surname:
            conditions.append('surname = ?')
            values.append(surname)

        if conditions:
            query += ' WHERE ' + ' AND '.join(conditions)

        self.cursor.execute(query, values)
        result = self.cursor.fetchall()
        staff_list = []
        for row in result:
            staff = {
                'id': row[0],
                'name': row[1],
                'surname': row[2]
            }
            staff_list.append(staff)
        return staff_list
