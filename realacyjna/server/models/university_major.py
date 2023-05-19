from database import Database

class UniversityMajor:
    def __init__(self):
        self.db = Database('baza.db')
    
    def create(self, university_id, major_id):
        query = 'INSERT INTO university_major (university_id, major_id) VALUES (?, ?)'
        self.db.execute(query, (university_id, major_id))
        self.db.commit()
        
    def read_all(self):
        query = 'SELECT * FROM university_major'
        result = self.db.execute(query).fetchall()
        university_majors = []
        for row in result:
            university_major = {'id': row['id'], 'university_id': row['university_id'], 'major_id': row['major_id']}
            university_majors.append(university_major)
        return university_majors
    
    def read_one(self, id):
        query = 'SELECT * FROM university_major WHERE id = ?'
        result = self.db.execute(query, (id,)).fetchone()
        if result:
            university_major = {'id': result['id'], 'university_id': result['university_id'], 'major_id': result['major_id']}
            return university_major
        return None
    
    def read_by_query(self, id=None, university_id=None, major_id=None):
        query = 'SELECT * FROM university_major WHERE '
        if id:
            query += 'id = ? AND '
        if university_id:
            query += 'university_id = ? AND '
        if major_id:
            query += 'major_id = ? AND '
        query = query.rstrip('AND ')
        values = tuple(filter(None, [id, university_id, major_id]))
        result = self.db.execute(query, values).fetchall()
        university_majors = []
        for row in result:
            university_major = {'id': row['id'], 'university_id': row['university_id'], 'major_id': row['major_id']}
            university_majors.append(university_major)
        return university_majors
    
    def read_by_university_id(self, university_id):
        query = 'SELECT * FROM university_major WHERE university_id = ?'
        result = self.db.execute(query, (university_id,)).fetchall()
        university_majors = []
        for row in result:
            university_major = {'id': row['id'], 'university_id': row['university_id'], 'major_id': row['major_id']}
            university_majors.append(university_major)
        return university_majors
    
    def read_by_major_id(self, major_id):
        query = 'SELECT * FROM university_major WHERE major_id = ?'
        result = self.db.execute(query, (major_id,)).fetchall()
        university_majors = []
        for row in result:
            university_major = {'id': row['id'], 'university_id': row['university_id'], 'major_id': row['major_id']}
            university_majors.append(university_major)
        return university_majors
    
    def update(self, id, university_id, major_id):
        query = 'UPDATE university_major SET university_id = ?, major_id = ? WHERE id = ?'
        self.db.execute(query, (university_id, major_id, id))
        self.db.commit()
        
    def delete(self, id):
        query = 'DELETE FROM university_major WHERE id = ?'
        self.db.execute(query, (id,))
        self.db.commit()
        