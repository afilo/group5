import json

with open('config.json', 'r') as f:
    config = json.load(f)

host = config['host'] # host connection url
name = config['name'] # name of the database to access
authMechanism = config['authMechanism'] # authentication mechanism