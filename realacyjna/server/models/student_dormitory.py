import sqlite3
from database import Database


class StudentDormModel:
    def __init__(self):
        self.connection = sqlite3.connect('baza.db', isolation_level=None)
        self.cursor = self.connection.cursor()

    def create(self, student_id, dormitory_id, check_in_date, check_out_date):
        query = 'INSERT INTO student_dormitory (student_id, dormitory_id, check_in_date, check_out_date) VALUES (?, ?, ?, ?)'
        self.cursor.execute(
            query, (student_id, dormitory_id, check_in_date, check_out_date))
        self.connection.commit()

    def read_one(self, id):
        query = 'SELECT * FROM student_dormitory WHERE id = ?'
        self.cursor.execute(query, (id,))
        result = self.cursor.fetchone()
        if result:
            st_dor = {
                'id': result[0],
                'student_id': result[1],
                'dormitory_id': result[2],
                'check_in_date': result[3],
                'check_out_date': result[4],
            }
            return st_dor

    def read_all(self):
        query = 'SELECT * FROM student_dormitory'
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        st_dor = []
        for row in result:
            res = {
                'id': row[0],
                'student_id': row[1],
                'dormitory_id': row[2],
                'check_in_date': row[3],
                'check_out_date': row[4],
            }
            st_dor.append(res)
        return st_dor

    def read_by_query(self, student_id=None, dormitory_id=None, check_in_date=None, check_out_date=None):
        query = 'SELECT * FROM student_dormitory'
        conditions = []
        values = []
        if student_id:
            conditions.append('student_id = ?')
            values.append(student_id)
        if dormitory_id:
            conditions.append('dormitory_id = ?')
            values.append(dormitory_id)
        if check_in_date:
            conditions.append('check_in_date = ?')
            values.append(check_in_date)
        if check_out_date:
            conditions.append('check_out_date = ?')
            values.append(check_out_date)
        if conditions:
            query += ' WHERE ' + ' AND '.join(conditions)
        result = self.db.execute(query, values).fetchone()
        if result:
            student_dormitory = {'id': result['id'], 'student_id': result['student_id'],
                                 'dormitory_id': result['dormitory_id'], 'check_in_date': result['check_in_date'],
                                 'check_out_date': result['check_out_date']}
            return student_dormitory
        return None




    def update(self, id, student_id=None, dormitory_id=None, check_in_date=None, check_out_date=None):
        query = 'UPDATE student_dormitory SET '
        if student_id is not None:
            query += 'student_id = ?, '
        if dormitory_id is not None:
            query += 'dormitory_id = ?, '
        if check_in_date is not None:
            query += 'check_in_date = ?, '
        if check_out_date is not None:
            query += 'check_out_date = ?, '
        query = query.rstrip(', ') + ' WHERE id = ?'
        values = [value for value in [student_id, dormitory_id, check_in_date, check_out_date, id] if value is not None]
        self.cursor.execute(query, tuple(values))
        self.connection.commit()

    def delete(self, id):
        query = 'DELETE FROM student_dormitory WHERE id = ?'
        self.cursor.execute(query, (id,))
        self.connection.commit()

    def __del__(self):
        self.connection.close()
