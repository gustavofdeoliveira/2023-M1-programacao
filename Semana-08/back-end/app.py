from flask import Flask, send_from_directory
from flask_cors import CORS
from prisma import Prisma, register
from routes.coordinates import coordinate_blueprint
import os

db = Prisma()
db.connect()
register(db)
app = Flask(__name__, static_folder='build')
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/',defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')

app.register_blueprint(coordinate_blueprint, url_prefix='/coordinate')



if __name__ == "__main__":
  app.run(debug=True, port=5000, host='0.0.0.0')