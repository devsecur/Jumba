import requests
import os
import json
from flask_restful import reqparse

def pagination(f):
    def decorated_function(*args, **kws):
        # Do something with your request here
        parser = reqparse.RequestParser()
        parser.add_argument('sort', type=str)
        parser.add_argument('page', type=int, default=0)
        parser.add_argument('order', type=str)
        parser.add_argument('filter', type=str)
        parser.add_argument('limit', type=int, default=10)

        arguments = parser.parse_args()
        results = f(*args, **kws)
        if arguments["filter"]:
            datas = []
            for data in results["data"]:
                add = False
                for key, value in data.items():
                    if isinstance(value, str ) and arguments["filter"] in value:
                        add = True
                        break
                if add:
                    datas.append(data)
            results["data"] = datas
        results["data"] = sorted(
            results["data"],
            key=lambda k: k.get(arguments["sort"], 0),
            reverse=True if arguments["order"] == 'asc' else False)
        results["recordsTotal"] = len(results["data"])
        results["data"] = results["data"][arguments["page"]*arguments["limit"]:arguments["page"]+1*arguments["limit"]]
        return results
    return decorated_function

def get_apis(name="", method="GET"):
    url = 'https://apimgmt/api-umbrella/v1/apis/{}'.format(name)
    payload = {'some': 'data'}
    headers = {
        'X-Api-Key': os.path.expandvars('$API_KEY'),
        'X-Admin-Auth-Token': os.path.expandvars('$API_ADMIN_KEY')
        }

    r = requests.request(method, url, headers=headers, verify=False)
    return json.loads(r.text)
