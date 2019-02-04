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
        self._base_payload = {
            'apikey': API_KEY,
            'cmd': self.cmd,
            'out_type': self.out_type,
            'callback': self.callback,
            'debug': self.debug
        }
        self.params = self._strip_params()
        self.payload = self.update()

    def update(self):
        payload = self._base_payload
        # Combine params with _base_payload into payload
        for key in self.params:
            payload[key] = self.params[key]
        # Remove all None values from payload
        for key in payload:
            if payload[key] is None:
                del payload[key]
        self.validate()
        return payload

    def _strip_params(self):
        stripped_params = {}
        for key in self.params:
            if self.params[key] is not None:
                stripped_params[key] = self.params[key]
        return stripped_params

    def clear(self):
        """Clear everything from payload"""
        self.payload.clear()

    def remove_keys(self, *keys):
        """Removes given keys from payload"""
        for key in keys:
            del self.payload[key]

    def get(self, pprint=False):
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

    def validate(self):
        """Validate payload"""
        if len(self.params) > 0:
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