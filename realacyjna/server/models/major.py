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

    def read_by_query(self, name=None, department=None, email=None, phone=None, office=None):
        query = 'SELECT * FROM major'
        conditions = []
        values = []
        if name:
            conditions.append('name = ?')
            values.append(name)
        if department:
            conditions.append('department = ?')
            values.append(department)
        if email:
            conditions.append('email = ?')
            values.append(email)
        if phone:
            conditions.append('phone = ?')
            values.append(phone)
        if office:
            conditions.append('office = ?')
            values.append(office)
        if conditions:
            query += ' WHERE ' + ' AND '.join(conditions)
        result = self.db.execute(query, values).fetchone()
        if result:
            major = {'id': result[0], 'name': result[1], 'department': result[2], 'email': result[3], 'phone': result[4],
                     'office': result[5]}
            return major
        return None

    def update(self, id, name=None, department=None, email=None, phone=None, office=None, hire_date=None):
        query = 'UPDATE Major SET '
        if name:
            query += 'name = ?, '
        if department:
            query += 'department = ?, '
        if email:
            query += 'email = ?, '
        if phone:
            query += 'phone = ?, '
        if office:
            query += 'office = ?, '
        if hire_date:
            query += 'hire_date = ?, '
        query = query.rstrip(', ') + ' WHERE id = ?'
        values = tuple(filter(None, [name, department, email, phone, office, hire_date, id]))
        self.db.execute(query, values)
        self.db.commit()

    def delete(self, id):
        query = 'DELETE FROM Major WHERE id = ?'
        self.db.execute(query, (id,))
        self.db.commit()
