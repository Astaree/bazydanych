from flask_restful import Resource, reqparse
from models.student_faculty import StudentFacultyModel

class StudentFaculty(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('student_id', type=int, required=True, help='student_id required')
    parser.add_argument('faculty_id', type=int, required=True, help='faculty_id required')

    def __init__(self):
        self.model = StudentFacultyModel()

    def get(self, id):
        student_faculty = self.model.read_one(id)
        if student_faculty:
            return student_faculty, 200
        return {'message': 'Student Faculty not found'}, 404
    
    def post(self, id):
        if self.model.read_one(id):
            return {'message': 'Student Faculty with given ID already exists'}, 400
        data = StudentFacultyModel.parser.parse_args()
        student_id = data['student_id']
        faculty_id = data['faculty_id']

        self.model.create(student_id, faculty_id)
        return {'message': 'Student Faculty created successfully'}, 201
    
    def put(self,id):
        data = StudentFacultyModel.parser.parse_args()
        student_id = data['student_id']
        faculty_id = data['faculty_id']

        student_faculty = self.model.read_one(id)
        if student_faculty:
            self.model.update(id, student_id, faculty_id)
            return {'message': 'Student Faculty updated successfully'}, 200
        
        self.model.create(student_id, faculty_id)
        return {'message': 'Student Faculty created successfully'}, 201
    
    def delete(self, id):
        student_faculty = self.model.read_one(id)
        if student_faculty:
            self.model.delete(id)
            return {'message': 'Student Faculty deleted successfully'}, 200
        return {'message': 'Student Faculty not found'}, 404
    
class StudentFacultyList(Resource):
    def __init__(self):
        self.model = StudentFacultyModel()
    
    def get(self):
        return {'student_faculties': self.model.read_all()}, 200 
    