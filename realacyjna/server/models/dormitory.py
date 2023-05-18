import sqlite3
from database import Database


class DormitoryModel:
    def __init__(self):
        self.db = sqlite3.connect('baza.db')

    def create(self, name, address, city, state, zip, capacity, occupancy):
        query = 'INSERT INTO dormitory (name, address, city, state, zip, capacity, occupancy) VALUES (?, ?, ?, ?, ?, ?)'
        self.db.execute(query, (name, address, city,
                        state, zip, capacity, occupancy))
        self.db.commit()

    def read_all(self):
        query = 'SELECT * FROM dormitory'
        cursor = self.db.execute(query)
        result = cursor.fetchall()
        return [{'id': row[0], 'name': row[1], 'address': row[2], 'city': row[3], 'state': row[4], 'zip': row[5],
                 'capacity': row[6], 'occupancy': row[7]} for row in result]

    def read_one(self, id):
        query = 'SELECT * FROM dormitory WHERE id = ?'
        cursor = self.db.execute(query, (id,))
        result = cursor.fetchone()
        if result:
            return {'id': result[0], 'name': result[1], 'address': result[2], 'city': result[3], 'state': result[4], 'zip': result[5],
                    'capacity': result[6], 'occupancy': result[7]}

    def read_by_query(self, name=None, adress=None, city=None, state=None, zip=None, capacity=None,
                      occupancy=None):
        query = 'SELECT * FROM dormitory'
        conditions = []
        values = []
        if name:
            conditions.append('name = ?')
            values.append(name)
        if adress:
            conditions.append('adress = ?')
            values.append(adress)
        if city:
            conditions.append('city = ?')
            values.append(city)
        if state:
            conditions.append('state = ?')
            values.append(state)
        if zip:
            conditions.append('zip = ?')
            values.append(zip)
        if capacity:
            conditions.append('capacity = ?')
            values.append(capacity)
        if occupancy:
            conditions.append(occupancy)
            values.append(occupancy)
        if conditions:
            query += ' WHERE ' + ' AND '.join(conditions)
        result = self.db.execute(query, values).fetchone()
        if result:
            dormitory = {'id': result[0], 'name': result[1], 'address': result[2], 'city': result[3], 'state': result[4], 'zip': result[5],
                         'capacity': result[6], 'occupancy': result[7]}
            return dormitory
        return None


    def update(self, id, name=None, address=None, city=None, state=None, zip=None, capacity=None, occupancy=None):
        query = 'UPDATE dormitory SET '
        if name:
            query += 'name = ?, '
        if address:
            query += 'address = ?, '
        if city:
            query += 'city = ?, '
        if state:
            query += 'state = ?, '
        if zip:
            query += 'zip = ?, '
        if capacity:
            query += 'capacity = ?, '
        if occupancy:
            query += 'occupancy = ?, '
        query = query.rstrip(', ') + ' WHERE id = ?'
        values = tuple(
            filter(None, [name, address, city, state, zip, capacity, occupancy, id]))
        self.db.execute(query, values)
        self.db.commit()

    def delete(self, id):
        query = 'DELETE FROM dormitory WHERE id = ?'
        self.db.execute(query, (id,))
        self.db.commit()
