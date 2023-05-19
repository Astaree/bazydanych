import logging
from database import Database


class UniversityModel:
    def __init__(self):
        self.db = Database('baza.db')

    def create(self, name, location, dean_name):
        query = 'INSERT INTO university (name, location, dean_name, student_count) VALUES (?, ?, ?, 0)'
        self.db.execute(query, (name, location, dean_name))
        self.db.commit()

    def read_all(self):
        query = 'SELECT * FROM university'
        result = self.db.execute(query).fetchall()
        universities = []
        for row in result:
            university = {'id': row['id'], 'name': row['name'], 'location': row['location'],
                          'dean_name': row['dean_name'], 'student_count': row['student_count']}
            universities.append(university)
        return universities

    def read_one(self, id):
        query = 'SELECT * FROM university WHERE id = ?'
        result = self.db.execute(query, (id,)).fetchone()
        if result:
            university = {'id': result['id'], 'name': result['name'], 'location': result['location'],
                          'dean_name': result['dean_name'], 'student_count': result['student_count']}
            return university
        return None

    def read_by_query(self, id=None, name=None, location=None,
                      dean_name=None, student_count=None):
        query = 'SELECT * FROM university WHERE '
        if id:
            query += 'id = ? AND '
        if name:
            query += 'name = ? AND '
        if location:
            query += 'location = ? AND '
        if dean_name:
            query += 'dean_name = ? AND '
        if student_count:
            query += 'student_count = ? AND '
        query = query.rstrip('AND ')
        values = tuple(
            filter(None, [id, name, location, dean_name, student_count]))
        result = self.db.execute(query, values).fetchall()
        universities = []
        for row in result:
            university = {
                'id': row['id'],
                'name': row['name'],
                'location': row['location'],
                'dean_name': row['dean_name'],
                'student_count': row['student_count']
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
