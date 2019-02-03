import configparser
import json
from jsonschema import validate, ValidationError, SchemaError
import requests


# ConfigParser Variables
config = configparser.ConfigParser()
config.read('settings_private.ini')
# Settings File Variables
HOST = config['USER_SETTINGS']['host']
PORT = config['USER_SETTINGS']['port']
API_KEY = config['USER_SETTINGS']['api_key']
SCHEMA = config['USER_SETTINGS']['schema']
PATH = config['USER_SETTINGS']['path']


class Payload:
    """Base class for API command payload"""

    def __init__(self, name, out_type=None, callback=None,
                 debug=None, **params):
        self._base_url = '{0}://{1}:{2}{3}/api/v2'.format(
            SCHEMA, HOST, PORT, PATH
        )
        self.name = name
        self.apikey = API_KEY
        self.cmd = name
        self.out_type = out_type
        self.callback = callback
        self.debug = debug
        self.payload = {
            'apikey': API_KEY,
            'cmd': self.cmd,
            'out_type': self.out_type,
            'callback': self.callback,
            'debug': self.debug
        }
        self.params = params

        if len(params) > 0:
            self.update(params)

    def update(self, param_dict):
        self.payload.update(param_dict)

    def clear(self):
        self.payload.clear()

    def remove_keys(self, *keys):
        if keys is not None:
            for key in keys:
                del self.payload[key]
        else:
            pass

    def get_results(self, pprint=False):
        """Send/receive API request"""
        r = requests.get(self._base_url, params=self.payload)
        if r.status_code == 200:
            if pprint:
                r = json.loads(r.content.decode('utf-8'))
                r = json.dumps(r, sort_keys=True, indent=4)
                return r
            else:
                r = json.loads(r.content.decode('utf-8'))
                return r
        else:
            r.raise_for_status()

    def validate(self, unique_schema=True):
        """Validate payload"""
        if unique_schema:
            try:
                schema = './schemas/{}.json'.format(self.name)
                with open(schema, 'r') as schema_file:
                    schema = json.load(schema_file)
                    validate(instance=self.payload, schema=schema)
            except ValidationError as e:
                print(e.message)
            except SchemaError as e:
                print(e.message)
        else:
            try:
                schema = '/schemas/payload.json'
                with open(schema, 'r') as schema_file:
                    schema = json.load(schema_file)
                    validate(instance=self.payload, schema=schema)
            except ValidationError as e:
                print(e.message)
            except SchemaError as e:
                print(e.message)
