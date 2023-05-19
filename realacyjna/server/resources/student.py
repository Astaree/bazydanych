from sqlite3 import Date
from flask import request
from flask_restful import Resource, reqparse
from models.studnet import StudentModel


class Student(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, required=True,
                        help='Name is a required field.')
    parser.add_argument('surname', type=str, required=True,
                        help='Surname is a required field.')
    parser.add_argument('email', type=str, required=True,
                        help='Email is a required field.')
    parser.add_argument('date_of_birth', type=str, required=True,
                        help='Date of birth is a required field.')
    parser.add_argument('gender', type=int, required=True,
                        help='Gender is a required field.')

    def __init__(self):
        self.model = StudentModel()

    def get(self, id):
        student = self.model.read_one(id)
        if student:
            return student, 200
        return {'message': 'Student not found'}, 404

    def put(self, id):
        data = Student.parser.parse_args()
        name = data['name']
        surname = data['surname']
        email = data['email']
        date_of_birth = data['date_of_birth']
        gender = data['gender']

        if self.model.read_one(id):
            self.model.update(id, name, surname, email, date_of_birth, gender)
            return {'message': 'Student updated successfully.'}, 200
        return {'message': 'Student not found'}, 404

    def delete(self, id):
        if self.model.read_one(id):
            self.model.delete(id)
            return {'message': 'Student deleted successfully.'}, 200
        return {'message': 'Student not found.'}, 404


class StudentList(Resource):
    def __init__(self):
        self.model = StudentModel()

    def get(self):
        students = self.model.read_all()
        if students == []:
            return {'message': 'No data in table',
                    'keys': [
                        'id',
                        'name',
                        'surname',
                        'email',
                        'date_of_birth',
                        'gender',
                        'join_date',
                        'semester',
                    ]
                    }, 404
        return students, 200

    def post(self):
        data = Student.parser.parse_args()
        name = data['name']
        surname = data['surname']
        email = data['email']
        date_of_birth = data['date_of_birth']
        gender = data['gender']

        self.model.create(name, surname, email, date_of_birth, gender)
        return {'message': 'Student created successfully.'}, 201


class StudentQuary(Resource):
    def __init__(self):
        self.model = StudentModel()

    def get(self):
        id = request.args.get('id')
        name = request.args.get('name')
        surname = request.args.get('surname')
        email = request.args.get('email')
        date_of_birth = request.args.get('date_of_birth')
        gender = request.args.get('gender')
        join_date = request.args.get('join_date')
        semester = request.args.get('semester')

        students = self.model.read_by_query(
            id, name, surname, email, date_of_birth, gender, join_date, semester)
        if students == []:
            return {'message': 'No data in table',
                    'keys': [
                        'id',
                        'name',
                        'surname',
                        'email',
                        'date_of_birth',
                        'gender',
                        'join_date',
                        'semester',
                    ]
                    }, 404
        return students, 200
    
