from flask import Flask
from flask_restful import Api

from ressources.api import User, Users, UserFormat

app = Flask(__name__)
api = Api(app)

api.add_resource(Users, "/users/")
api.add_resource(User, "/users/<string:name>")
api.add_resource(UserFormat, "/users/format")

app.run(debug=True, host='0.0.0.0')
