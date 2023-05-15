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
            print(row.keys())
            university = {'id': row['id'], 'name': row['name'], 'location': row['location'], 'dean_name': row['dean_name'], 'student_count': row['student_count']}
            universities.append(university)
        return universities

    def read_one(self, id):
        query = 'SELECT * FROM university WHERE id = ?'
        result = self.db.execute(query, (id,)).fetchone()
        if result:
            university = {'id': result['id'], 'name': result['name'], 'location': result['location'], 'dean_name': result['dean_name'], 'student_count': result['student_count']}
            return university
        return None

    def update(self, id, name, location, dean_name):
        query = 'UPDATE university SET name = ?, location = ?, dean_name = ? WHERE id = ?'
        self.db.execute(query, (name, location, dean_name, id))
        self.db.commit()

    def delete(self, id):
        query = 'DELETE FROM university WHERE id = ?'
        self.db.execute(query, (id,))
        self.db.commit()
