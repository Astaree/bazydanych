from flask import Flask
from flask_restful import Api
from resources.university import University, UniversityList
from resources.faculty import Faculty, FacultyList

app = Flask(__name__)
api = Api(app)

# Add routes for the university resource
api.add_resource(University, '/universities/<int:id>')
api.add_resource(UniversityList, '/universities')

# Add routes for the faculty resource
api.add_resource(Faculty, '/faculties/<int:id>')
api.add_resource(FacultyList, '/faculties')


if __name__ == '__main__':
    app.run(debug=True)
