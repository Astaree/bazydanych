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

# Add routes for the university resource
api.add_resource(University, '/universities/<int:id>')
api.add_resource(UniversityList, '/universities')

# Add routes for the Major resource
api.add_resource(Major, '/major/<int:id>')
api.add_resource(MajorList, '/major')

# Add routes for the Student resource
api.add_resource(Student, '/students/<int:id>')
api.add_resource(StudentList, '/students')

# Add routes for the Student in dormitory resource
api.add_resource(StudentDorm, '/students_dormitory/<int:id>')
api.add_resource(StudentDormList, '/students_dormitory')

# Add routes for the Student in major resource
api.add_resource(StudentMajor, '/students_major/<int:id>')
api.add_resource(StudentMajorList, '/students_major')

# Add routes for the Dormitory resource
api.add_resource(Dormitory, '/dormitories/<int:id>')
api.add_resource(DormitoryList, '/dormitories')

if __name__ == '__main__':
    app.run(debug=True)

# TODO: add triggers to the database,
# api still might change, but works for now