from flask import Flask
from prisma import Prisma, register
from routes.coordinates import coordinate_blueprint


db = Prisma()
db.connect()
register(db)
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():

  
  return {
    "ping": "coordinates"
  }

app.register_blueprint(coordinate_blueprint, url_prefix='/coordinate')



if __name__ == "__main__":
  app.run(debug=True, port=5000, host='0.0.0.0')