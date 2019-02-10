"""Tautulli base class"""


from payload import Payload
from validator import Validator
from requester import Requester
from tautulli_api_auth import TautulliApiAuth
import configparser
from jsonschema import validate, ValidationError, SchemaError, RefResolver


# ConfigParser Variables
config = configparser.ConfigParser()
config.read('settings_private.ini')
# Settings File Variables
HOST = config['USER_SETTINGS']['host']
PORT = config['USER_SETTINGS']['port']
API_KEY = config['USER_SETTINGS']['api_key']
SCHEMA = config['USER_SETTINGS']['schema']
PATH = config['USER_SETTINGS']['path']


class Tautulli:
    """Tautulli base class"""
    def __init__(self, host=None, port=None, apikey=None,
                 schema=None, path=None):
        # Endpoint values
        self.host = host or HOST
        self.port = port or PORT
        self.apikey = apikey or API_KEY
        self.schema = schema or SCHEMA
        self.path = path or PATH
        self.url = '{0}://{1}:{2}{3}/api/v2'.format(
            self.schema, self.host, self.port, self.path
        )
        # Requests authorization
        self.auth = TautulliApiAuth(apikey=self.apikey)

    def _command(self, name='', params=None, pprint=False):
        """Sends and receives API command"""
        payload = Payload(name, params=params)
        validator = Validator(params)
        validator.validate()
        requester = Requester(self.url, payload, self.auth)
        r = requester.get(pprint=pprint)
        return r
