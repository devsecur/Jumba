from flask import Flask
from flask_restful import Api
from ressources.api import API, APIs

app = Flask(__name__)
api = Api(app)

api.add_resource(APIs, '/apis', '/apis/')
api.add_resource(API, '/apis/<string:name>')

app.run(debug=True, host='0.0.0.0')
