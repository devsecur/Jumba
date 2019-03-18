from ast import literal_eval
import json

from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse

from common import db
from models.User import User

class UserView(Resource):
    def get(self, name):
        return jsonify(User.query.all())
        #return jsonify([i.serialize for i in User.query.all()])

    def post(self, name):
        user = User(username=name, email='admin3@example.com')
        db.db.getDB().session.add(user)
        db.db.getDB().session.commit()
        return jsonify(user)

    def put(self, name):
        pass

    def delete(self, name):
        pass
