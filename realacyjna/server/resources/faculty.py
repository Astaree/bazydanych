from flask_restful import Resource, reqparse
from models.faculty import FacultyModel

class Faculty(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, required=True, help='Name is a required field.')
    parser.add_argument('department', type=str, required=True, help='Department is a required field.')
    parser.add_argument('email', type=str, required=True, help='Email is a required field.')
    parser.add_argument('phone', type=str)
    parser.add_argument('office', type=str)
    parser.add_argument('hire_date', type=str, required=True, help='Hire date is a required field.')

    def __init__(self):
        self.model = FacultyModel()

    def get(self, id):
        faculty = self.model.read_one(id)
        if faculty:
            return faculty, 200
        return {'message': 'Faculty not found.'}, 404

    def post(self, id):
        if self.model.read_one(id):
            return {'message': 'Faculty with given ID already exists.'}, 400

        data = Faculty.parser.parse_args()
        name = data['name']
        department = data['department']
        email = data['email']
        phone = data['phone']
        office = data['office']
        hire_date = data['hire_date']

        self.model.create(name, department, email, phone, office, hire_date)
        return {'message': 'Faculty created successfully.'}, 201

    def put(self, id):
        data = Faculty.parser.parse_args()
        name = data['name']
        department = data['department']
        email = data['email']
        phone = data['phone']
        office = data['office']
        hire_date = data['hire_date']

        faculty = self.model.read_one(id)
        if faculty:
            self.model.update(id, name, department, email, phone, office, hire_date)
            return {'message': 'Faculty updated successfully.'}, 200

        self.model.create(name, department, email, phone, office, hire_date)
        return {'message': 'Faculty created successfully.'}, 201

    def delete(self, id):
        faculty = self.model.read_one(id)
        if faculty:
            self.model.delete(id)
            return {'message': 'Faculty deleted successfully.'}, 200
        return {'message': 'Faculty not found.'}, 404


class FacultyList(Resource):
    def __init__(self):
        self.model = FacultyModel()

    def get(self):
        return {'faculties': self.model.read_all()}, 200
