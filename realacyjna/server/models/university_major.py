from database import Database

class UniversityMajorModel:
    def __init__(self):
        self.db = Database('baza.db')
        self.table_name = 'major_university'
        
    def create(self, university_id, major_id):
        query = f'INSERT INTO {self.table_name} (university_id, major_id) VALUES (%s, %s)'
        self.db.execute(query, (university_id, major_id))
        
    def read_all(self):
        query = f'SELECT * FROM {self.table_name}'
        result = self.db.execute(query).fetchall()
        university_majors = []
        for row in result:
            university_major = {'id': row['id'], 'university_id': row['university_id'], 'major_id': row['major_id']}
            university_majors.append(university_major)
        return university_majors
    
    def read_one(self, id):
        query = f'SELECT * FROM {self.table_name} WHERE id = %s'
        result = self.db.execute(query, (id,)).fetchone()
        if result:
            university_major = {'id': result['id'], 'university_id': result['university_id'], 'major_id': result['major_id']}
            return university_major
        return None
    
    def read_by_query(self, id=None, university_id=None, major_id=None):
        query = f'SELECT * FROM {self.table_name} WHERE '
        conditions = []
        values = []

        if id:
            conditions.append('id = %s')
            values.append(id)
        if university_id:
            conditions.append('university_id = %s')
            values.append(university_id)
        if major_id:
            conditions.append('major_id = %s')
            values.append(major_id)

        query += ' AND '.join(conditions)
        result = self.db.execute(query, values).fetchall()

        university_majors = []
        for row in result:
            university_major = {'id': row['id'], 'university_id': row['university_id'], 'major_id': row['major_id']}
            university_majors.append(university_major)

        return university_majors
    
    
    def update(self, id, university_id, major_id):
        query = f'UPDATE {self.table_name} SET university_id = %s, major_id = %s WHERE id = %s'
        self.db.execute(query, (university_id, major_id, id))
        
    def delete(self, id):
        query = f'DELETE FROM {self.table_name} WHERE id = %s'
        self.db.execute(query, (id,))
        
    