from sqlite3 import Date
from flask_restful import Resource, reqparse
from models.studnet import StudentModel

class Student(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, required=True, help='Name is a required field.')
    parser.add_argument('surname', type=str, required=True, help='Surname is a required field.')
    parser.add_argument('email', type=str, required=True, help='Email is a required field.')
    parser.add_argument('date_of_birth', type=Date, required=True, help='Date of birth is a required field.')
    parser.add_argument('gender', type=str, required=True, help='Gender is a required field.')
    parser.add_argument('major', type=str, required=True, help='Major is a required field.')
    parser.add_argument('join_date', type=Date, required=True, help='Major is a required field.')
    parser.add_argument('leave_date', type=Date, required=True, help='Major is a required field.')


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
        major = data['major']

        if self.model.read_one(id):
            self.model.update(id, name, surname, email, date_of_birth, gender, major)
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
        return {'students': students}, 200

    def post(self):
        data = Student.parser.parse_args()
        name = data['name']
        surname = data['surname']
        email = data['email']
        date_of_birth = data['date_of_birth']
        gender = data['gender']
        major = data['major']

        self.model.create(name, surname, email, date_of_birth, gender, major)
        return {'message': 'Student created successfully.'}, 201
