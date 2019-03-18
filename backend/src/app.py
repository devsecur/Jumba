import os

from flask import Flask
from flask_restful import Api

from common import db

app = Flask(__name__)
app.config.from_object(os.environ['APP_CONFIG'])
app.json_encoder = db.AlchemyEncoder
db = db.Database()
db.connect(app)
api = Api(app)

from views import views
db.init()


views(api)

app.run(debug=True, host='0.0.0.0')
