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
    
    def get(self, id):
        dormitory = self.model.read_one(id)
        if dormitory:
            return dormitory, 200
        return {'message': 'Dormitory not found'}, 404
    
    
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
    
    def delete(self, id):
        dormitory = self.model.read_one(id)
        if dormitory:
            self.model.delete(id)
            return {'message': 'Dormitory deleted successfully'}, 200
        return {'message': 'Faculty not found.'}, 404
    

class DormitoryList(Resource):
    def __init__(self):
        self.model = DormitoryModel()
    
    def get(self):
        dormitories = self.model.read_all()
        return dormitories, 200

def post(self):
        data = Dormitory.parser.parse_args()
        name = data['name']
        address = data['address']
        city = data['city']
        state = data['state']
        zip = data['zip']
        capacity = data['capacity']
        occupancy = data['occupancy']

        self.model.create(name, address, city, state, zip, capacity, occupancy)
        return {'message': 'Dormitory created successfully'}, 201