import json

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import DeclarativeMeta

class AlchemyEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            # an SQLAlchemy class
            fields = {}
            for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                data = obj.__getattribute__(field)
                try:
                    json.dumps(data) # this will fail on non-encodable values, like other classes
                    fields[field] = data
                except TypeError:
                    fields[field] = None
            # a json-encodable dict
            return fields

        return json.JSONEncoder.default(self, obj)

class Database(object):
    class _Database:
        def __init__(self):
            self.val = None

        def connect(self, app):
            print("connect "+str(self))
            self.db = SQLAlchemy(app)

        def init(self):
            print("init "+str(self))
            self.db.create_all()

        def getDB(self):
            print("getDB "+str(self))
            return self.db
    instance = None

    def __new__(cls):
        if not Database.instance:
            Database.instance = Database._Database()
        return Database.instance

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def __setattr__(self, name):
        return setattr(self.instance, name)

db = Database()
