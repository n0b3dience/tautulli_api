"""Tautulli base class"""


from payload import Payload
from tautulli_api_auth import TautulliApiAuth
import configparser


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
        # Kwarg values
        self.host = host or HOST
        self.port = port or PORT
        self.apikey = apikey or API_KEY
        self.schema = schema or SCHEMA
        self.path = path or PATH
        # Requests authorization
        self.auth = TautulliApiAuth(apikey=self.apikey)
