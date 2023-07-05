from sqlite3 import Date
from flask import request
from flask_restful import Resource, reqparse
from models.major import MajorModel


class Major(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, required=True, help='Name is a required field.')
    parser.add_argument('department', type=str, required=True, help='Department is a required field.')
    parser.add_argument('email', type=str, required=True, help='Email is a required field.')
    parser.add_argument('phone', type=str)
    parser.add_argument('office', type=str)
    parser.add_argument('staff_id', type=int)
    parser.add_argument('university_id', type=int, required=True, help='uni_id is required')

    def __init__(self):
        self.model = MajorModel()

    def get(self, id):
        major = self.model.read_one(id)
        if major:
            return major, 200
        return {'message': 'Major not found.'}, 404
    def put(self, id):
        data = Major.parser.parse_args()
        name = data['name']
        department = data['department']
        email = data['email']
        phone = data['phone']
        office = data['office']
        staff_id = data['staff_id']
        university_id = data['university_id']

        major = self.model.read_one(id)
        if major:
            self.model.update(id, name, department, email, phone, office, staff_id, university_id)
            return {'message': 'Major updated successfully.'}, 200

        self.model.create(id, name, department, email, phone, office, staff_id, university_id)
        return {'message': 'Major created successfully.'}, 201

    def delete(self, id):
        major = self.model.read_one(id)
        if major:
            self.model.delete(id)
            return {'message': 'Major deleted successfully.'}, 200
        return {'message': 'Major not found.'}, 404
    
    

class MajorList(Resource):
    def __init__(self):
        self.model = MajorModel()

    def get(self):
        majors = self.model.read_all()
        if majors == []:
            return {'message': 'No data in table',
                    'keys':[
                        'id',
                        'name',
                        'department',
                        'email',
                        'phone',
                        'office',
                        'staff_id',
                        'university_id'
                    ]
                    }, 404
        return majors, 200

    def post(self):
            data = Major.parser.parse_args()
            name = data['name']
            department = data['department']
            email = data['email']
            phone = data['phone']
            office = data['office']
            staff_id = data['staff_id']
            university_id = data['university_id']
            
            self.model.create(name, department, email, phone, office, staff_id, university_id)
            return {'message': 'Major created successfully.'}, 201
    
    
class MajorQuery(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('id', type=int, help='Failed to parse the id.')
    parser.add_argument('name', type=str, help='Failed to parse the name.')
    parser.add_argument('department', type=str, help='Failed to parse the department.')
    parser.add_argument('email', type=str, help='Failed to parse the email.')
    parser.add_argument('phone', type=str, help='Failed to parse the phone.')
    parser.add_argument('office', type=str, help='Failed to parse the office.')
    parser.add_argument('staff_id', type=int, help='Failed to parse the staff_id')
    parser.add_argument('university_id', type=int, help='Failed to parse uni_id')

    def __init__(self):
        self.model = MajorModel()

    # GET /major_query
    def get(self):
        
        id = request.args.get('id')
        name = request.args.get('name')
        department = request.args.get('department')
        email = request.args.get('email')
        phone = request.args.get('phone')
        office = request.args.get('office')
        staff_id = request.args.get('staff_id')
        university_id = request.args.get('university_id')
        

        majors = self.model.read_by_query(id, name, department, email, phone, office, staff_id, university_id)
        if majors == []:
            return {'message': 'No data in table',
                    'keys': [
                        'id',
                        'name',
                        'department',
                        'email',
                        'phone',
                        'office',
                        'staff_id',
                        'university_id'
                    ]
                    }, 404
        return majors, 200