from flask_restful import Resource, reqparse
from models.student_major import StudentMajorModel

class StudentMajor(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('student_id', type=int, required=True, help='student_id required')
    parser.add_argument('major_id', type=int, required=True, help='major_id required')

    def __init__(self):
        self.model = StudentMajorModel()

    def get(self, id):
        student_major = self.model.read_one(id)
        if student_major:
            return student_major, 200
        return {'message': 'Student Major not found'}, 404
    
    
    
    def put(self,id):
        data = StudentMajorModel.parser.parse_args()
        student_id = data['student_id']
        major_id = data['major_id']

        student_major = self.model.read_one(id)
        if student_major:
            self.model.update(id, student_id, major_id)
            return {'message': 'Student Major updated successfully'}, 200
        
        self.model.create(student_id, major_id)
        return {'message': 'Student Major created successfully'}, 201
    
    def delete(self, id):
        student_major = self.model.read_one(id)
        if student_major:
            self.model.delete(id)
            return {'message': 'Student Major deleted successfully'}, 200
        return {'message': 'Student Major not found'}, 404
    
class StudentMajorList(Resource):
    def __init__(self):
        self.model = StudentMajorModel()
    
    def get(self):
        return {'student_faculties': self.model.read_all()}, 200 
    
    def post(self, id):
        if self.model.read_one(id):
            return {'message': 'Student Major with given ID already exists'}, 400
        data = StudentMajorModel.parser.parse_args()
        student_id = data['student_id']
        major_id = data['major_id']

        self.model.create(student_id, major_id)
        return {'message': 'Student Major created successfully'}, 201