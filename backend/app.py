import os

from flask import Flask
from flask_restful import Api

from common import db
from ressources.api import User, Users, UserFormat
from ressources.question import Question

app = Flask(__name__)


def create_app(app):

    app.config.from_object(os.environ['APP_CONFIG'])

    db.init_app(app)
    return app

app = create_app(app)
api = Api(app)

api.add_resource(Users, "/users/")
api.add_resource(Question, "/questions/<string:dataset>")
api.add_resource(User, "/users/<string:name>")
api.add_resource(UserFormat, "/users/format")
app.run(debug=True, host='0.0.0.0')
