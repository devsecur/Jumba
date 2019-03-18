from flask_restful import Resource
from common.utils import get_apis, pagination

class APIs(Resource):
    @pagination
    def get(self):
        return get_apis()

    def post(self):
        return get_apis()

class API(Resource):
    def get(self, name):
        return get_apis(name)

    def post(self, name):
        return get_apis(name)

    def put(self, name):
        return get_apis(name)

    def delete(self, name):
        return get_apis(name)
