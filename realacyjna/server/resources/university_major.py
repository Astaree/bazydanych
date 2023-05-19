from flask import request
from flask_restful import Resource
from models.university_major import UniversityMajorModel

class UniversityMajor(Resource):
    def __init__(self):
        self.model = UniversityMajorModel()
        
    #GET /university_major/<int:id>
    def get(self, id):
        university_major = self.model.read_one(id)
        if university_major:
            return university_major, 200
        return {'message': 'University Major not found'}, 404
    
    #PUT /university_major/<int:id>
    def put(self,id):
        university_major = self.model.read_one(id)
        if university_major:
            data = UniversityMajor.parser.parse_args()
            university_id = data['university_id']
            major_id = data['major_id']
            self.model.update(id, university_id, major_id)
            return {'message': 'University Major updated successfully'}, 200
        return {'message': 'University Major not found'}, 404
    
    #DELETE /university_major/<int:id>
    def delete(self, id):
        university_major = self.model.read_one(id)
        if university_major:
            self.model.delete(id)
            return {'message': 'University Major deleted successfully'}, 200
        return {'message': 'University Major not found'}, 404
    
class UniversityMajorList(Resource):
    def __init__(self):
        self.model = UniversityMajorModel()
    
    #GET /university_major
    def get(self):
        university_majors = self.model.read_all()
        if university_majors:
            return university_majors, 200
        return {'message': 'No data in table',
                'keys':[
                    'id',
                    'university_id',
                    'major_id'
                ]
                }, 404
    
    #POST /university_major/<int:id>
    def post(self, id):
        university_major = self.model.read_one(id)
        if university_major:
            return {'message': 'University Major already exists'}, 400
        data = UniversityMajor.parser.parse_args()
        university_id = data['university_id']
        major_id = data['major_id']
        self.model.create(university_id, major_id)
        return {'message': 'University Major created successfully'}, 201
        
class UniversityMajorListQuarry(Resource):
    def __init__(self):
        self.model = UniversityMajorModel()
    
    #GET /quniversity_major/
    def get(self):
        
        university_id = request.args.get('university_id')
        major_id = request.args.get('major_id')
        id = request.args.get('id')
        
        university_majors = self.model.read_by_query(id, university_id, major_id)
        if university_majors == []:
            return {'message': 'No data in table',
                    'keys':[
                        'id',
                        'university_id',
                        'major_id'
                    ]
                    }, 404
        return university_majors, 200