import os
import configparser
import json
from jsonschema import validate, ValidationError, SchemaError, RefResolver
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

    def __init__(self, name, host=HOST, port=PORT, apikey=API_KEY,
                 schema=SCHEMA, path=PATH, out_type=None, callback=None,
                 debug=None, **params):
        self.name = name
        self.host = host
        self.port = port
        self._apikey = apikey
        self.schema = schema
        self.path = path
        self.out_type = out_type
        self.callback = callback
        self.debug = debug
        self.cmd = name
        self._base_url = '{0}://{1}:{2}{3}/api/v2'.format(
            self.schema, self.host, self.port, self.path)
        self._base_payload = {
            'apikey': API_KEY,
            'cmd': self.cmd,
            'out_type': self.out_type,
            'callback': self.callback,
            'debug': self.debug
        }
        self._params = params
        self._schema_dir = os.path.abspath('schemas')
        self._resolver = RefResolver(
            'file:///{}/'.format(self._schema_dir), None)
        self.params = self._strip_params()
        self.payload = self.update()

    def update(self):
        """Form payload"""
        payload = {}
        # Add non-None _base_payload keys/vals into payload
        for key in self._base_payload:
            if self._base_payload[key] is not None:
                payload[key] = self._base_payload[key]
            else:
                pass
        # Add non-None _params keys/vals into payload
        for key in self.params:
            payload[key] = self._params[key]
        # Validate payload against JSON Schema
        try:
            self._validate(payload)
            return payload
        except SchemaError as e:
            raise e.message
        except ValidationError as e:
            raise e.message

    def _strip_params(self):
        stripped_params = {}
        for key in self._params:
            if self._params[key] is not None:
                stripped_params[key] = self._params[key]
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

    def _validate(self, updated_payload):
        """Validate payload"""
        if len(self.params) > 0:
            try:
                schema = './schemas/{}.json'.format(self.name)
                with open(schema, 'r') as schema_file:
                    schema = json.load(schema_file)
                    validate(instance=updated_payload, schema=schema,
                             resolver=self._resolver)
            except ValidationError as e:
                print(e.message)
            except SchemaError as e:
                print(e.message)
        else:
            try:
                schema = '/schemas/payload.json'
                with open(schema, 'r') as schema_file:
                    schema = json.load(schema_file)
                    validate(instance=updated_payload, schema=schema,
                             resolver=self._resolver)
            except ValidationError as e:
                print(e.message)
            except SchemaError as e:
                print(e.message)
