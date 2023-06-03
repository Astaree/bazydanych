from flask import request
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
        data = StudentDorm.parser.parse_args()
        student_id = data['student_id']
        dormitory_id = data['dormitory_id']

        student_dormitory = self.model.read_one(id)
        if student_dormitory:
            self.model.update(id, student_id, dormitory_id)
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
        stud_dorm = self.model.read_all()
        if stud_dorm == []:
            return {'message': 'No data in table',
                    'keys':[
                        'id',
                        'student_id',
                        'dormitory_id',
                    ]
                    }, 404
        return stud_dorm, 200
    
    def post(self):
        data = StudentDorm.parser.parse_args()
        student_id = data['student_id']
        dormitory_id = data['dormitory_id']

    
        if self.model.create(student_id, dormitory_id) == False:
            return {'message': 'Failed creating student'}, 400
        
        return {'message': 'Student in Dormitory created successfully'}, 201

class StudentDormListQuarry(Resource):
    def __init__(self):
        self.model = StudentDormModel()
    
    def get(self):
        
        id = request.args.get('id')
        student_id = request.args.get('student_id')
        dormitory_id = request.args.get('dormitory_id')
        
        stud_dorm = self.model.read_by_query(id, student_id, dormitory_id)
        if stud_dorm == []:
            return {'message': 'No data in table',
                    'keys':[
                        'id',
                        'student_id',
                        'dormitory_id',
                    ]
                    }, 404
        return stud_dorm, 200