import sqlite3
from database import Database


class StudentModel:
    def __init__(self):
        self.connection = sqlite3.connect('baza.db')
        self.cursor = self.connection.cursor()

    def create(self, name, surname, email, date_of_birth, gender):
        query = 'INSERT INTO student (name, surname, email, date_of_birth, gender) VALUES (?, ?, ?, ?, ?)'
        self.cursor.execute(
            query, (name, surname, email, date_of_birth, gender))
        self.connection.commit()

    def read_one(self, id):
        query = 'SELECT * FROM student WHERE id = ?'
        self.cursor.execute(query, (id,))
        result = self.cursor.fetchone()
        if result:
            student = {
                'id': result[0],
                'name': result[1],
                'surname': result[2],
                'email': result[3],
                'date_of_birth': result[4],
                'gender': result[5],
                'join_date': result[6],
                'semester': result[7],
            }
            return student
        return None

    def read_all(self):
        query = 'SELECT * FROM student'
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        students = []
        for row in result:
            student = {
                'id': row[0],
                'name': row[1],
                'surname': row[2],
                'email': row[3],
                'date_of_birth': row[4],
                'gender': row[5],
                'join_date': row[6],
                'semester': row[7],
            }
            students.append(student)
        return students

    def read_by_query(self, id=None, name=None,
                      surname=None, email=None, date_of_birth=None,
                      gender=None, join_date=None, semester=None):
        query = 'SELECT * FROM student WHERE '
        if id:
            query += 'id = ? AND '
        if name:
            query += 'name = ? AND '
        if surname:
            query += 'surname = ? AND '
        if email:
            query += 'email = ? AND '
        if date_of_birth:
            query += 'date_of_birth = ? AND '
        if gender:
            query += 'gender = ? AND '
        if join_date:
            query += 'join_date = ? AND '
        if semester:
            query += 'semester = ? AND '
        query = query.rstrip('AND ')
        values = tuple(filter(
            None, [id, name, surname, email, date_of_birth,
                   gender, join_date, semester]))
        result = self.cursor.execute(query, values).fetchall()
        students = []
        for row in result:
            student = {
                'id': row[0],
                'name': row[1],
                'surname': row[2],
                'email': row[3],
                'date_of_birth': row[4],
                'gender': row[5],
                'join_date': row[6],
                'semester': row[7],
            }
            students.append(student)
        return students

    def update(self, id, name=None, surname=None, email=None, date_of_birth=None, gender=None):
        query = 'UPDATE student SET '
        if name:
            query += 'name = ?, '
        if surname:
            query += 'surname = ?, '
        if email:
            query += 'email = ?, '
        if date_of_birth:
            query += 'date_of_birth = ?, '
        if gender:
            query += 'gender = ?, '
        query = query.rstrip(', ') + ' WHERE id = ?'
        values = tuple(
            filter(None, [name, surname, email, date_of_birth, gender, id]))
        self.cursor.execute(query, values)
        self.connection.commit()

    def delete(self, id):
        query = 'DELETE FROM student WHERE id = ?'
        self.cursor.execute(query, (id,))
        self.connection.commit()

    def __del__(self):
        self.connection.close()
