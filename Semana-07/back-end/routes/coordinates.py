# Import the Blueprint and request classes from Flask library and the Coordinate model from prisma.models
from flask import Blueprint, request
from prisma.models import Coordinate

# Create a Blueprint object named coordinate_blueprint
coordinate_blueprint = Blueprint('coordinate', __name__)

# Define a route to handle GET requests on '/listAll' endpoint
@coordinate_blueprint.route('/listAll', methods=['GET'])
def list_all_coordinate():
    # Check if the request is a GET request
    if request.method == 'GET':
        # Find all coordinates using the prisma ORM and return the result in a dictionary format
        coordinates = Coordinate.prisma().find_many()
        return {
            "data": [coordinate.dict() for coordinate in coordinates]
        }

# Define a route to handle GET requests on '/listOne' endpoint
@coordinate_blueprint.route('/listOne', methods=['GET'])
def list_one_coordinate():
    # Check if the request is a GET request
    if request.method == 'GET':
        # Get the JSON data from the request object
        data = request.json
        # If the JSON data is None, return None
        if data is None:
            return
        # Get the id of the coordinate from the JSON data
        id = data.get('id')
        # If the id is None, return an error dictionary
        if id is None:
            return {'error': 'Id is none'}
        # Find the unique coordinate using the prisma ORM and return the result in a dictionary format
        coordinate = Coordinate.prisma().find_unique(where={'id': id})
        return {
            "data": [coordinate.dict()]
        }

# Define a route to handle POST requests on '/create' endpoint
@coordinate_blueprint.route('/create', methods=['POST'])
def create_coordinate():
    # Check if the request is a POST request
    if request.method == 'POST':
        # Get the JSON data from the request object
        data = request.json
        # If the JSON data is None, return None
        if data is None:
            return
        # Get the coordinate values from the JSON data
        coordinateX = data.get('coordinateX')
        coordinateY = data.get('coordinateY')
        coordinateZ = data.get('coordinateZ')
        coordinateR = data.get('coordinateR')
        # If any of the coordinate values are None, return an error dictionary
        if coordinateX is None or coordinateY is None or coordinateZ is None or coordinateR is None:
            return {"error": "You need all coordinates"}
        # Create a new coordinate using the prisma ORM and return the result in a dictionary format
        coordinate = Coordinate.prisma().create(
            data={'coordinateX': coordinateX, 'coordinateY': coordinateY, 'coordinateZ': coordinateZ, 'coordinateR': coordinateR})
        return dict(coordinate)

@coordinate_blueprint.route('/update', methods=['PUT'])  # Decorator for the Flask route to update coordinate data
def update_coordinate():
    if request.method == 'PUT':  # Check if the HTTP request method is PUT
        data = request.json  # Retrieve the JSON data from the request body
        if data is None:  # If no data is found in the request, exit the function
            return
        id = data.get('id')  # Retrieve the 'id' field from the JSON data
        
        if id is None:  # If the 'id' field is missing, return an error message
            return {'error': 'Id is none'}
        
        coordinateX = data.get('coordinateX')  # Retrieve the 'coordinateX' field from the JSON data
        coordinateY = data.get('coordinateY')  # Retrieve the 'coordinateY' field from the JSON data
        coordinateZ = data.get('coordinateZ')  # Retrieve the 'coordinateZ' field from the JSON data
        coordinateR = data.get('coordinateR')  # Retrieve the 'coordinateR' field from the JSON data
        
        # Update the coordinate data in the database using the Prisma ORM
        coordinate = Coordinate.prisma().update(where={'id': id}, data={'coordinateX': coordinateX, 'coordinateY': coordinateY, 'coordinateZ': coordinateZ, 'coordinateR': coordinateR})
        
        return "successfully deleted"  # Return a success message to the client

@coordinate_blueprint.route('/delete', methods=['DELETE'])  # Decorator for the Flask route to delete coordinate data
def delete_coordinate():
    if request.method == 'DELETE':  # Check if the HTTP request method is DELETE
        data = request.json  # Retrieve the JSON data from the request body
        if data is None:  # If no data is found in the request, exit the function
            return
        id = data.get('id')  # Retrieve the 'id' field from the JSON data

        if id is None:  # If the 'id' field is missing, return an error message
            return {'error': 'Id is none'}
        
        # Delete the coordinate data from the database using the Prisma ORM
        coordinate = Coordinate.prisma().delete(where={'id': id})
        
        # Return the deleted coordinate data to the client, excluding the 'author' field
        return coordinate.dict(exclude={'author'})
