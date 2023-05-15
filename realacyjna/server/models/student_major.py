import sqlite3


class StudentMajorModel:
    def __init__(self):
        self.connection = sqlite3.connect('baza.db')
        self.cursor = self.connection.cursor()

    def create(self, student_id, major_id):
        query = 'INSERT INTO student_major (student_id, major_id) VALUES (?, ?)'
        self.cursor.execute(query, (student_id, major_id))
        self.connection.commit()

    def read_one(self, id):
        query = 'SELECT * FROM student_major WHERE id = ?'
        self.cursor.execute(query, (id,))
        result = self.cursor.fetchone()
        if result:
            st_maj = {
                'id': result[0],
                'student_id': result[1],
                'major_id': result[2],
            }
            return st_maj

    def read_all(self):
        query = 'SELECT * FROM student_major'
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        st_maj = []
        for row in result:
            res = {
                'id': row[0],
                'student_id': row[1],
                'major_id': row[2],
            }
            st_maj.append(res)
        return st_maj

    def update(self, id, student_id=None, major_id=None):
        query = 'UPDATE student_major SET '
        if student_id:
            query += 'student_id = ?, '
        if major_id:
            query += 'major_id = ?, '
        query = query.rstrip(', ') + ' WHERE id = ?'
        values = tuple(filter(None, [student_id, major_id, id]))
        self.cursor.execute(query, values)
        self.connection.commit()

    def delete(self, id):
        query = 'DELETE FROM student_major WHERE id = ?'
        self.cursor.execute(query, (id,))
        self.connection.commit()

    def __del__(self):
        self.connection.close()