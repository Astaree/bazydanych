from flask_restful import Resource, reqparse
from flask import current_app as app
from flask import request
from models.university import UniversityModel


class University(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('id', type=int, help='Failed to parse the id.')
    parser.add_argument('name', type=str, help='Failed to parse the name.')
    parser.add_argument('location', type=str,
                        help='Failed to parse the location.')
    parser.add_argument('dean_name', type=str,
                        help='Failed to parse the dean_name.')
    parser.add_argument('student_count', type=int,  
                        help='Failed to parse the student_count.')

    def __init__(self):
        self.model = UniversityModel()

    def get(self, id):
        university = self.model.read_one(id)
        if university:
            return university, 200
        return {'message': 'University not found'}, 404

    def put(self, id):
        data = University.parser.parse_args()
        name = data['name']
        location = data['location']
        dean_name = data['dean_name']

        if self.model.read_one(id):
            self.model.update(id, name, location, dean_name)
            return {'message': 'University updated successfully.'}, 200
        return {'message': 'University not found.'}, 404

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
        if universities == []:
            return {'message': 'No data in table',
                    'keys': [
                        'id',
                        'name',
                        'location',
                        'dean_name',
                        'student_count',
                        'max_students'
                    ]
                    }, 404
        return universities, 200

    # POST /university
    def post(self):
        data = University.parser.parse_args()
        id = data['id']
        name = data['name']
        location = data['location']
        dean_name = data['dean_name']
        student_count = data['student_count']

        self.model.create(name, location, dean_name)
        return {'message': 'University created successfully.'}, 201


class UniversityQuery(Resource):
    def __init__(self):
        self.model = UniversityModel()

    # GET /quniversity?id=1&name=University of Toronto&location=Toronto&dean_name=John&student_count=1000
    def get(self):
        id = request.args.get('id')
        name = request.args.get('name')
        location = request.args.get('location')
        dean_name = request.args.get('dean_name')
        student_count = request.args.get('student_count')
        

        universities = self.model.read_by_query(
            id, name, location, dean_name, student_count)
        if universities == []:
            return {'message': 'No data in table',
                    'keys': [
                        'id',
                        'name',
                        'location',
                        'dean_name',
                        'student_count'
                    ]
                    }, 404
        return universities, 200
