import logging
from database import Database
import re

class UniversityModel:
    def __init__(self):
        self.db = Database('baza.db')

    def create(self, name, location, dean_name,  max_students):
        query = 'INSERT INTO university (name, location, dean_name,  max_students) VALUES (?, ?, ?, ?)'
        self.db.execute(query, (name, location, dean_name,  max_students))
        self.db.commit()

    def read_all(self):
        query = 'SELECT * FROM university'
        result = self.db.execute(query).fetchall()
        universities = []
        for row in result:
            university = {'id': row['id'], 'name': row['name'], 'location': row['location'],
                          'dean_name': row['dean_name'], 'student_count': row['student_count'], 'max_students': row['max_students']}
            universities.append(university)
        return universities

    def read_one(self, id):
        query = 'SELECT * FROM university WHERE id = ?'
        result = self.db.execute(query, (id,)).fetchone()
        if result:
            university = {'id': result['id'], 'name': result['name'], 'location': result['location'],
                          'dean_name': result['dean_name'], 'student_count': result['student_count'], 'max_students': result['max_students']}
            return university
        return None



    def read_by_query(self, id=None, name=None, location=None,
                    dean_name=None, student_count=None, max_students=None):
        query = 'SELECT * FROM university WHERE '
        conditions = []
        values = []

        if id:
            conditions.append('id = ?')
            values.append(id)
        if name:
            conditions.append('name LIKE ?')
            values.append(f'%{name}%')
        if location:
            conditions.append('location LIKE ?')
            values.append(f'%{location}%')
        if dean_name:
            conditions.append('dean_name LIKE ?')
            values.append(f'%{dean_name}%')
        if student_count:
            conditions.append('student_count = ?')
            values.append(student_count)
        if max_students:
            conditions.append('max_students = ?')
            values.append(max_students)

        query += ' AND '.join(conditions)
        result = self.db.execute(query, values).fetchall()
        
        universities = []
        for row in result:
            university = {
                'id': row['id'],
                'name': row['name'],
                'location': row['location'],
                'dean_name': row['dean_name'],
                'student_count': row['student_count'],
                'max_students': row['max_students']
            }
            universities.append(university)
        
        return universities


    def update(self, id, name=None, location=None, dean_name=None):
        query = 'UPDATE university SET '
        if name:
            query += 'name = ?, '
        if location:
            query += 'location = ?, '
        if dean_name:
            query += 'dean_name = ?, '
        query = query.rstrip(', ') + ' WHERE id = ?'
        values = tuple(filter(None, [name, location, dean_name, id]))
        self.db.execute(query, values)
        self.db.commit()

    def delete(self, id):
        query = 'DELETE FROM university WHERE id = ?'
        self.db.execute(query, (id,))
        self.db.commit()
