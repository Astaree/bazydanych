from flask_restful import Resource, reqparse
from models.student_dormitory import StudentDormModel

class StudentDorm(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('student_id', type=int, required=True, help='student_id required')
    parser.add_argument('dormitory_id', type=int, required=True, help='dormitory_id required')
    parser.add_argument('check_in_date', type=str, required=True, help='check_in_date required')
    parser.add_argument('check_out_date', type=str, required=True, help='check_out_date required')

    def __init__(self):
        self.model = StudentDormModel()

    def get(self, id):
        student_dormitory = self.model.read_one(id)
        if student_dormitory:
            return student_dormitory, 200
        return {'message': 'Student in Dormitory not found'}, 404
    
    def put(self,id):
        data = StudentDormModel.parser.parse_args()
        student_id = data['student_id']
        dormitory_id = data['dormitory_id']
        check_in_date = data['check_in_date']
        check_out_date = data['check_out_date']

        student_dormitory = self.model.read_one(id)
        if student_dormitory:
            self.model.update(id, student_id, dormitory_id, check_in_date, check_out_date)
            return {'message': 'Student in Dormitory updated successfully'}, 200
        return {'message': 'Student in Dormitory not found'}, 404
    
    def delete(self, id):
        student_major = self.model.read_one(id)
        if student_major:
            self.model.delete(id)
            return {'message': 'Student Major deleted successfully'}, 200
        return {'message': 'Student Major not found'}, 404
    
class StudentDormList(Resource):
    def __init__(self):
        self.model = StudentDormModel()
    
    def get(self):
        return {'student_dormitories': self.model.read_all()}, 200
    
    def post(self):
        data = StudentDormModel.parser.parse_args()
        student_id = data['student_id']
        dormitory_id = data['dormitory_id']
        check_in_date = data['check_in_date']
        check_out_date = data['check_out_date']

        
        
        self.model.create(student_id, dormitory_id, check_in_date, check_out_date)
        return {'message': 'Student in Dormitory created successfully'}, 201
