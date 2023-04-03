# Import necessary modules and packages
from flask import Blueprint, request
from prisma.models import Coordinate

# Create a new Blueprint for coordinates
coordinate_blueprint = Blueprint('coordinate', __name__)

# Define a route to list all coordinates
@coordinate_blueprint.route('/listAll', methods=['GET'])
def list_all_coordinate():
    # Check if the HTTP request method is GET
    if request.method == 'GET':
        # Retrieve all coordinates from the database
        coordinates = Coordinate.prisma().find_many()
        
        # Return the data in JSON format
        return {
            "data": [coordinate.dict() for coordinate in coordinates]
        }

# Define a route to list the most recent coordinate added
@coordinate_blueprint.route('/listOne', methods=['GET'])
def list_one_coordinate():
    # Check if the HTTP request method is GET
    if request.method == 'GET':
        # Retrieve the most recent coordinate from the database
        coordinates = Coordinate.prisma().find_first(order={
        'id': 'desc',
    })
        # Return the data in JSON format
        return coordinates.json()

# Define a route to create a new coordinate
@coordinate_blueprint.route('/create', methods=['POST'])
def create_coordinate():
    # Check if the HTTP request method is POST
    if request.method == 'POST':
        # Retrieve the coordinate data from the request
        data = request.json
        if data is None:
            return

        # Extract the coordinate values from the data
        coordinateX = data.get('coordinateX')
        coordinateY = data.get('coordinateY')
        coordinateZ = data.get('coordinateZ')
        coordinateR = data.get('coordinateR')

        # Check if all the required coordinates are present
        if coordinateX is None or coordinateY is None or coordinateZ is None or coordinateR is None:
            return {"error": "You need all coordinates"}

        # Create a new coordinate object and save it to the database
        coordinate = Coordinate.prisma().create(
            data={'coordinateX': coordinateX, 'coordinateY': coordinateY, 'coordinateZ': coordinateZ, 'coordinateR': coordinateR})

        # Return the newly created coordinate in JSON format
        return dict(coordinate)

# Define a route to update a coordinate
@coordinate_blueprint.route('/update', methods=['PUT'])
def update_coordinate():
    if request.method == 'PUT': # check if request method is PUT
        data = request.json # retrieve the JSON data from the request
        if data is None: # if no data was provided
            return
        id = data.get('id') # retrieve the id of the coordinate to update
        
        if id is None: # if id is not provided
            return {'error': 'Id is none'}
        
        coordinateX = data.get('coordinateX') # retrieve the new X coordinate value
        coordinateY = data.get('coordinateY') # retrieve the new Y coordinate value
        coordinateZ = data.get('coordinateZ') # retrieve the new Z coordinate value
        coordinateR = data.get('coordinateR') # retrieve the new R coordinate value
        
        # update the coordinate with the given id using the new coordinate values
        coordinate = Coordinate.prisma().update(where={'id': id}, data={'coordinateX': coordinateX, 'coordinateY': coordinateY, 'coordinateZ': coordinateZ, 'coordinateR': coordinateR})
        return "successfully deleted" # return a success message
    
# Define a route to delete a coordinate
@coordinate_blueprint.route('/delete', methods=['DELETE'])
def delete_coordinate():
    if request.method == 'DELETE': # check if request method is DELETE
        data = request.json # retrieve the JSON data from the request
        if data is None: # if no data was provided
            return
        id = data.get('id') # retrieve the id of the coordinate to delete

        if id is None: # if id is not provided
            return {'error': 'Id is none'}
        
        # delete the coordinate with the given id
        coordinate = Coordinate.prisma().delete(where={'id': id})
        return coordinate.dict(exclude={'author'}) # return the deleted coordinate (excluding the author field)


