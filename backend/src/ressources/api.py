from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse

class UserFormat(Resource):
    def get(self):
        return jsonify(
            [{"key":"name"}, {"key":"age"}, {"key":"occupation"}]
        )

class Users(Resource):
    def get(self):
        return "bla"

    def post(self):
        pass

class User(Resource):
    def get(self, name):
        return "bla"

    def post(self, name):
        pass

    def put(self, name):
        pass

    def delete(self, name):
        pass
