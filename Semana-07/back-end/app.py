# Import necessary packages/modules
from flask import Flask, send_from_directory
from flask_cors import CORS
from prisma import Prisma, register
from routes.coordinates import coordinate_blueprint
import os

# Instantiate Prisma ORM and connect to the database
db = Prisma()
db.connect()

# Register the database instance with Prisma
register(db)

# Instantiate Flask application with a static folder named 'build'
app = Flask(__name__, static_folder='build')

# Enable Cross-Origin Resource Sharing (CORS) for the application
cors = CORS(app)

# Specify the CORS headers to be sent with the responses from the application
app.config['CORS_HEADERS'] = 'Content-Type'

# Define the root route and other routes to serve static files from the 'build' folder
@app.route('/',defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    # If the requested path exists in the 'build' folder, send the file from that folder
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        return send_from_directory(app.static_folder, path)
    # Otherwise, send the 'index.html' file from the 'build' folder
    else:
        return send_from_directory(app.static_folder, 'index.html')

# Register the 'coordinate_blueprint' with the Flask application and set its URL prefix
app.register_blueprint(coordinate_blueprint, url_prefix='/coordinate')

# Run the Flask application on a development server if this module is being run directly
if __name__ == "__main__":
  app.run(debug=True, port=5000, host='0.0.0.0')
