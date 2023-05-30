from flask import Flask
from flask_restful import Api

from resources.university import University, UniversityList, UniversityQuery
from resources.major import Major, MajorList, MajorQuery
from resources.student_major import StudentMajor, StudentMajorList, StudentMajorListQuarry
from resources.university_major import UniversityMajor, UniversityMajorList, UniversityMajorListQuarry
from resources.student import Student, StudentList, StudentQuary
from resources.student_dormitory import StudentDorm, StudentDormList, StudentDormListQuarry
from resources.dormitory import Dormitory, DormitoryList, DormitoryListQuarry
from resources.staff import Staff, StaffList, StaffQuery
from resources.index import Index



app = Flask(__name__)
api = Api(app)

# Db routes
# Add routes for the university resource
api.add_resource(University, '/api/university/<int:id>')
api.add_resource(UniversityList, '/api/university')
api.add_resource(UniversityQuery, '/api/quniversity')

# Add routes for the Major resource
api.add_resource(Major, '/api/majors/<int:id>')
api.add_resource(MajorList, '/api/majors')
api.add_resource(MajorQuery, '/api/qmajors')


# Add routes for the Student resource
api.add_resource(Student, '/api/students/<int:id>')
api.add_resource(StudentList, '/api/students')
api.add_resource(StudentQuary, '/api/qstudents')

# Add routes for the Student in dormitory resource
api.add_resource(StudentDorm, '/api/students_dormitory/<int:id>')
api.add_resource(StudentDormList, '/api/students_dormitory')
api.add_resource(StudentDormListQuarry, '/api/qstudents_dormitory')


# Add routes for the Student in major resource
api.add_resource(StudentMajor, '/api/students_major/<int:id>')
api.add_resource(StudentMajorList, '/api/students_major')
api.add_resource(StudentMajorListQuarry, '/api/qstudents_major')

# Add routes for the Dormitory resource
api.add_resource(Dormitory, '/api/dormitories/<int:id>')
api.add_resource(DormitoryList, '/api/dormitories')
api.add_resource(DormitoryListQuarry, '/api/qdormitories')

# Add routes for the staff resource
api.add_resource(Staff, '/api/staff/<int:id>')
api.add_resource(StaffList, '/api/staff')
api.add_resource(StaffQuery, '/api/qstaff')

# client routes
api.add_resource(Index, '/')


if __name__ == '__main__':
    app.run(debug=True )
    
    
# TODO: add triggers to the database,
# api still might change, but works for now