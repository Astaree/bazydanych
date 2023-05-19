from flask import request
from flask_restful import Resource, reqparse
from models.dormitory import DormitoryModel

class Dormitory(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, required=True, help='Name is a required field')
    parser.add_argument('address', type=str, required=True, help='Address is a required field')
    parser.add_argument('city', type=str, required=True, help='City is a required field')
    parser.add_argument('state', type=str, required=True, help='State is a required field')
    parser.add_argument('zip', type=str, required=True, help='Zip is a required field')
    parser.add_argument('capacity', type=int)
    parser.add_argument('occupancy', type=int)


    def __init__(self):
        self.model = DormitoryModel()
    
    # GET /dormitory/<id>
    def get(self, id):
        dormitory = self.model.read_one(id)
        if dormitory:
            return dormitory, 200
        return {'message': 'Dormitory not found'}, 404
    
    # PUT /dormitory/<id>
    def put(self, id):
        data = Dormitory.parser.parse_args()
        name = data['name']
        address = data['address']
        city = data['city']
        state = data['state']
        zip = data['zip']
        capacity = data['capacity']
        occupancy = data['occupancy']

        dormitory = self.model.read_one(id)
        if dormitory:
            self.model.update(id, name, address, city, state, zip, capacity, occupancy)
            return {'message': 'Dormitory updated successfully'}, 200
        
        self.model.create(name, address, city, state, zip, capacity, occupancy)
        return {'message': 'Dormitory created successfully'}, 201
    
    # DELETE /dormitory/<id>
    def delete(self, id):
        dormitory = self.model.read_one(id)
        if dormitory:
            self.model.delete(id)
            return {'message': 'Dormitory deleted successfully'}, 200
        return {'message': 'Faculty not found.'}, 404
    

class DormitoryList(Resource):
    def __init__(self):
        self.model = DormitoryModel()
    
    # GET /dormitory
    def get(self):
        dormitories = self.model.read_all()
        if dormitories == []:
            return {'message': 'No data in table',
                    'keys':[
                        'id',
                        'name',
                        'address',
                        'city',
                        'state',
                        'zip',
                        'capacity',
                        'occupancy'
                    ]
                    }, 404
        return dormitories, 200


class DormitoryListQuarry(Resource):
    def __init__(self):
        self.model = DormitoryModel()
        
    # GET /dormitory
    def get(self):
            
        name = request.args.get('name')
        address = request.args.get('address')
        city = request.args.get('city')
        state = request.args.get('state')
        zip = request.args.get('zip')
        capacity = request.args.get('capacity')
        occupancy = request.args.get('occupancy')
        
        dormitory = self.model.read_by_query(name, address, city, state, zip, capacity, occupancy)
        if dormitory == []:
            return {'message': 'No data in table'}, 404
        return dormitory, 200
        