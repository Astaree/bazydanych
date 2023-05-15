from flask import Flask
from flask_restful import Api

from resources.university import University, UniversityList
from resources.major import Major, MajorList
from resources.student import Student, StudentList
from resources.student_dormitory import StudentDorm, StudentDormList
from resources.student_major import StudentMajor, StudentMajorList
from resources.dormitory import Dormitory, DormitoryList



app = Flask(__name__)
api = Api(app)

# Db routes
# Add routes for the university resource
api.add_resource(University, '/api/universities/<int:id>')
api.add_resource(UniversityList, '/api/universities')

# Add routes for the Major resource
api.add_resource(Major, '/api/major/<int:id>')
api.add_resource(MajorList, '/api/major')

# Add routes for the Student resource
api.add_resource(Student, '/api/students/<int:id>')
api.add_resource(StudentList, '/api/students')

# Add routes for the Student in dormitory resource
api.add_resource(StudentDorm, '/api/students_dormitory/<int:id>')
api.add_resource(StudentDormList, '/api/students_dormitory')

# Add routes for the Student in major resource
api.add_resource(StudentMajor, '/api/students_major/<int:id>')
api.add_resource(StudentMajorList, '/api/students_major')

# Add routes for the Dormitory resource
api.add_resource(Dormitory, '/api/dormitories/<int:id>')
api.add_resource(DormitoryList, '/api/dormitories')


# client routes



if __name__ == '__main__':
    app.run(debug=True)

# TODO: add triggers to the database,
# api still might change, but works for now