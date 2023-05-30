from flask import request
from flask_restful import Resource, reqparse
from models.staff import StaffModel


class Staff(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, required=True, help='Name is a required field.')
    parser.add_argument('surname', type=str, required=True, help='Surname is a required field.')

    def __init__(self):
        self.model = StaffModel()

    def get(self, id):
        staff = self.model.read_one(id)
        if staff:
            return staff, 200
        return {'message': 'Staff not found.'}, 404

    def put(self, id):
        data = Staff.parser.parse_args()
        name = data['name']
        surname = data['surname']

        staff = self.model.read_one(id)
        if staff:
            self.model.update(id, name, surname)
            return {'message': 'Staff updated successfully.'}, 200

        self.model.create(id, name, surname)
        return {'message': 'Staff created successfully.'}, 201

    def delete(self, id):
        staff = self.model.read_one(id)
        if staff:
            self.model.delete(id)
            return {'message': 'Staff deleted successfully.'}, 200
        return {'message': 'Staff not found.'}, 404


class StaffList(Resource):
    def __init__(self):
        self.model = StaffModel()

    def get(self):
        staff_list = self.model.read_all()
        if staff_list == []:
            return {'message': 'No data in table',
                    'keys': ['id', 'name', 'surname']
                    }, 404
        return staff_list, 200

    def post(self):
        data = Staff.parser.parse_args()
        name = data['name']
        surname = data['surname']

        self.model.create(name, surname)
        return {'message': 'Staff created successfully.'}, 201


class StaffQuery(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('id', type=int, help='Failed to parse the id.')
    parser.add_argument('name', type=str, help='Failed to parse the name.')
    parser.add_argument('surname', type=str, help='Failed to parse the surname.')

    def __init__(self):
        self.model = StaffModel()

    def get(self):
        id = request.args.get('id')
        name = request.args.get('name')
        surname = request.args.get('surname')

        staff_list = self.model.read_by_query(id, name, surname)
        if staff_list == []:
            return {'message': 'No data in table',
                    'keys': ['id', 'name', 'surname']
                    }, 404
        return staff_list, 200