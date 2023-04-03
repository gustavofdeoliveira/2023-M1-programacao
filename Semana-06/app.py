# Importing Flask module
from flask import Flask

# Importing Prisma and register modules from prisma package
from prisma import Prisma, register

# Importing coordinate_blueprint from routes.coordinates package
from routes.coordinates import coordinate_blueprint

# Creating an instance of Prisma
db = Prisma()

# Connecting to the database
db.connect()

# Registering the database instance
register(db)

# Creating an instance of the Flask application
app = Flask(__name__)

# Defining a route for the root endpoint
@app.route('/', methods=['GET'])
def index():
    # Returning a JSON response
    return {
        "ping": "coordinates"
    }

# Registering the coordinate_blueprint with the Flask application
app.register_blueprint(coordinate_blueprint, url_prefix='/coordinate')

# Running the Flask application if the script is run directly
if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')
