# Import necessary modules and packages
from flask import Flask, send_from_directory
from flask_cors import CORS
from prisma import Prisma, register
from routes.coordinates import coordinate_blueprint
import os

# Create a new instance of the Prisma ORM and connect to the database
db = Prisma()
db.connect()

# Register the Prisma instance to be used with other modules
register(db)

# Create a new Flask app instance with the name of the current module
app = Flask(__name__, static_folder='build')

# Enable Cross-Origin Resource Sharing (CORS) for the Flask app
cors = CORS(app)

# Specify the headers to be used for CORS
app.config['CORS_HEADERS'] = 'Content-Type'

# Create a route for the Flask app to serve static files
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        # If the requested path exists, serve the file from the static folder
        return send_from_directory(app.static_folder, path)
    else:
        # Otherwise, serve the index.html file from the static folder
        return send_from_directory(app.static_folder, 'index.html')

# Register the 'coordinate_blueprint' Blueprint with the Flask app
app.register_blueprint(coordinate_blueprint, url_prefix='/coordinate')

# Start the Flask app with debug mode enabled, listening on port 5000, and accessible from any IP address
if __name__ == "__main__":
  app.run(debug=True, port=5000, host='0.0.0.0')
