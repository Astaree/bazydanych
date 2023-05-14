import sqlite3


class StudentModel:
    def __init__(self):
        self.connection = sqlite3.connect('baza.db')
        self.cursor = self.connection.cursor()

    def create(self, name, surname, email, date_of_birth, gender, enrollment_date, leave_date):
        query = 'INSERT INTO student (name, surname, email, date_of_birth, gender, enrollment_date, leave_date) VALUES (?, ?, ?, ?, ?, ?, ? )'
        self.cursor.execute(
            query, (name, surname, email, date_of_birth, gender, enrollment_date, leave_date))
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
                'enrollment_date': result[6],
                'leave_date': result[7],
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
                'enrollment_date': row[6],
                'leave_date': row[7],
            }
            students.append(student)
        return students

    def update(self, id, name, surname, email, date_of_birth, gender, enrollment_date, leave_date):
        query = 'UPDATE student SET name = ?, surname = ?, email = ?, date_of_birth = ?, gender = ?, , enrollment_date = ?, leave_date =? WHERE id = ?'
        self.cursor.execute(query, (name, surname, email,
                            date_of_birth, gender, enrollment_date, leave_date, id))
        self.connection.commit()

    def delete(self, id):
        query = 'DELETE FROM student WHERE id = ?'
        self.cursor.execute(query, (id,))
        self.connection.commit()

    def __del__(self):
        self.connection.close()
