import sqlite3

class MajorModel:
    def __init__(self):
        self.db = sqlite3.connect('baza.db')

    def create(self, name, department, email, phone, office):
        query = 'INSERT INTO Major (name, department, email, phone, office) VALUES (?, ?, ?, ?, ?, ?)'
        self.db.execute(query, (name, department, email, phone, office))
        self.db.commit()

    def read_all(self):
        query = 'SELECT * FROM Major'
        cursor = self.db.execute(query)
        result = cursor.fetchall()
        return [{'id': row[0], 'name': row[1], 'department': row[2], 'email': row[3], 'phone': row[4], 'office': row[5]} for row in result]

    def read_one(self, id):
        query = 'SELECT * FROM Major WHERE id = ?'
        cursor = self.db.execute(query, (id,))
        result = cursor.fetchone()
        if result:
            return {'id': result[0], 'name': result[1], 'department': result[2], 'email': result[3], 'phone': result[4], 'office': result[5]}

    def update(self, id, name, department, email, phone, office, hire_date):
        query = 'UPDATE Major SET name = ?, department = ?, email = ?, phone = ?, office = ? WHERE id = ?'
        self.db.execute(query, (name, department, email, phone, office, id))
        self.db.commit()

    def delete(self, id):
        query = 'DELETE FROM Major WHERE id = ?'
        self.db.execute(query, (id,))
        self.db.commit()
