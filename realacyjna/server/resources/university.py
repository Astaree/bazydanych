from flask_restful import Resource, reqparse
from models.university import UniversityModel

class University(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, required=True, help='Name is a required field.')
    parser.add_argument('location', type=str, required=True, help='Location is a required field.')
    parser.add_argument('dean_name', type=str, required=True, help='Dean name is a required field.')

    def __init__(self):
        self.model = UniversityModel()

    def get(self, id):
        university = self.model.read_one(id)
        if university:
            return university, 200
        return {'message': 'University not found'}, 404

    def post(self, id):
        if self.model.read_one(id):
            return {'message': 'University with given ID already exists.'}, 400

        data = University.parser.parse_args()
        name = data['name']
        location = data['location']
        dean_name = data['dean_name']

        self.model.create(name, location, dean_name)
        return {'message': 'University created successfully.'}, 201

    def put(self, id):
        data = University.parser.parse_args()
        name = data['name']
        location = data['location']
        dean_name = data['dean_name']

        if self.model.read_one(id):
            self.model.update(id, name, location, dean_name)
            return {'message': 'University updated successfully.'}, 200
        self.model.create(name, location, dean_name)
        return {'message': 'University created successfully.'}, 201

    def delete(self, id):
        if self.model.read_one(id):
            self.model.delete(id)
            return {'message': 'University deleted successfully.'}, 200
        return {'message': 'University not found.'}, 404

class UniversityList(Resource):
    def __init__(self):
        self.model = UniversityModel()

    def get(self):
        universities = self.model.read_all()
        return {'universities': universities}, 200
