import requests
import os
import json

def get_apis(name="", method="GET"):
    url = 'https://apimgmt/api-umbrella/v1/apis/{}'.format(name)
    payload = {'some': 'data'}
    headers = {
        'X-Api-Key': os.path.expandvars('$API_KEY'),
        'X-Admin-Auth-Token': os.path.expandvars('$API_ADMIN_KEY')
        }

    r = requests.request(method, url, headers=headers, verify=False)
    return json.loads(r.text)
