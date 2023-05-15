import sqlite3


class StudentDormModel:
    def __init__(self):
        self.connection = sqlite3.connect('baza.db')
        self.cursor = self.connection.cursor()

    def create(self, student_id, dormitory_id, check_in_date, check_out_date):
            query = 'INSERT INTO student_dormitory (student_id, dormitory_id, check_in_date, check_out_date) VALUES (?, ?, ?, ?)'
            self.cursor.execute(query, (student_id, dormitory_id, check_in_date, check_out_date))
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
        
    def update(self, id, student_id, dormitory_id, check_in_date, check_out_date):
            query = 'UPDATE student_dormitory SET student_id = ?, dormitory_id = ?, check_in_date = ?, check_out_date = ? WHERE id = ?'
            self.cursor.execute(query, (student_id, dormitory_id, check_in_date, check_out_date, id))
            self.connection.commit()

    def delete(self, id):
            query = 'DELETE FROM student_dormitory WHERE id = ?'
            self.cursor.execute(query, (id,))
            self.connection.commit()

    def __del__(self):
            self.connection.close()