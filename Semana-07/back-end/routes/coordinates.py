from flask import Blueprint, request
from prisma.models import Coordinate

coordinate_blueprint = Blueprint('coordinate', __name__)


@coordinate_blueprint.route('/listAll', methods=['GET'])
def list_all_coordinate():
    if request.method == 'GET':
        coordinates = Coordinate.prisma().find_many()
        return {
            "data": [coordinate.dict() for coordinate in coordinates]
        }

@coordinate_blueprint.route('/listOne', methods=['GET'])
def list_one_coordinate():
    if request.method == 'GET':
        data = request.json
        if data is None:
            return
        id = data.get('id')
        if id is None:
            return {'error': 'Id is none'}
        coordinate = Coordinate.prisma().find_unique(where={'id': id})
        return {
            "data": [coordinate.dict()]
        }


@coordinate_blueprint.route('/create', methods=['POST'])
def create_coordinate():
    if request.method == 'POST':
        data = request.json
        if data is None:
            return

        coordinateX = data.get('coordinateX')
        coordinateY = data.get('coordinateY')
        coordinateZ = data.get('coordinateZ')
        coordinateR = data.get('coordinateR')
        if coordinateX is None or coordinateY is None or coordinateZ is None or coordinateR is None:
            return {"error": "You need all coordinates"}

        coordinate = Coordinate.prisma().create(
            data={'coordinateX': coordinateX, 'coordinateY': coordinateY, 'coordinateZ': coordinateZ, 'coordinateR': coordinateR})

        return dict(coordinate)

@coordinate_blueprint.route('/update', methods=['PUT'])
def update_coordinate():
    if request.method == 'PUT':
        data = request.json
        if data is None:
            return
        id = data.get('id')
        
        if id is None:
            return {'error': 'Id is none'}
        
        coordinateX = data.get('coordinateX')
        coordinateY = data.get('coordinateY')
        coordinateZ = data.get('coordinateZ')
        coordinateR = data.get('coordinateR')
        coordinate = Coordinate.prisma().update(where={'id': id}, data={'coordinateX': coordinateX, 'coordinateY': coordinateY, 'coordinateZ': coordinateZ, 'coordinateR': coordinateR})
        return "successfully deleted"

@coordinate_blueprint.route('/delete', methods=['DELETE'])
def delete_coordinate():
    if request.method == 'DELETE':
        data = request.json
        if data is None:
            return
        id = data.get('id')

        if id is None:
            return {'error': 'Id is none'}
        coordinate = Coordinate.prisma().delete(where={'id': id})
        return coordinate.dict(exclude={'author'})

