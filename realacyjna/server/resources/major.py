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

    def __init__(self):
        self.model = MajorModel()

    def get(self, id):
        Major = self.model.read_one(id)
        if Major:
            return Major, 200
        return {'message': 'Major not found.'}, 404


    def put(self, id):
        data = Major.parser.parse_args()
        name = data['name']
        department = data['department']
        email = data['email']
        phone = data['phone']
        office = data['office']

        Major = self.model.read_one(id)
        if Major:
            self.model.update(id, name, department, email, phone, office)
            return {'message': 'Major updated successfully.'}, 200

        self.model.create(name, department, email, phone, office)
        return {'message': 'Major created successfully.'}, 201

    def delete(self, id):
        Major = self.model.read_one(id)
        if Major:
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
                        'office'
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

        # Check if the Major already exists
        Major = self.model.read_one_by_name(name)
        if Major:
            return {'message': 'Major already exists.'}, 400
        self.model.create(name, department, email, phone, office)
        return {'message': 'Major created successfully.'}, 201
    
class MajorQuery(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('id', type=int, help='Failed to parse the id.')
    parser.add_argument('name', type=str, help='Failed to parse the name.')
    parser.add_argument('department', type=str, help='Failed to parse the department.')
    parser.add_argument('email', type=str, help='Failed to parse the email.')
    parser.add_argument('phone', type=str, help='Failed to parse the phone.')
    parser.add_argument('office', type=str, help='Failed to parse the office.')

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
        

        majors = self.model.read_by_query(id, name, department, email, phone, office)
        if majors == []:
            return {'message': 'No data in table',
                    'keys': [
                        'id',
                        'name',
                        'department',
                        'email',
                        'phone',
                        'office'
                    ]
                    }, 404
        return majors, 200