import sqlite3

class DormitoryModel:
    def __init__(self):
        self.db = sqlite3.connect('baza.db')
    
    def create(self, name, address, city, state, zip, capacity, occupancy):
            query = 'INSERT INTO dormitory (name, address, city, state, zip, capacity, occupancy) VALUES (?, ?, ?, ?, ?, ?)'
            self.db.execute(query, (name, address, city, state, zip, capacity, occupancy))
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
         
    def update(self, id, name, address, city, state, zip, capacity, occupancy):
         query = 'UPDATE dormitory SET name = ?, address = ?, city = ?, state = ?, zip = ?, capacity = ?, occupancy = ?'
         self.db.execute(query, (name, address, city, state, zip, capacity, occupancy))
         self.db.commit()
    
    def delete(self, id):
         query = 'DELETE FROM dormitory WHERE id = ?'
         self.db.execute(query, (id,))
         self.db.commit()
