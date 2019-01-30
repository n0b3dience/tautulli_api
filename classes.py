import configparser
from tautulli_api_auth import TautulliApiAuth
import utils


# ConfigParser Variables
config = configparser.ConfigParser()
config.read('settings_private.ini')
# Settings File Variables
HOST = config['USER_SETTINGS']['host']
PORT = config['USER_SETTINGS']['port']
API_KEY = config['USER_SETTINGS']['api_key']
SCHEMA = 'http'
PATH = ''


class ApiCommand:
    """
    API Command base class
    """
    def __init__(self, name, out_type=None, callback=None, debug=None,
                 **kwargs):
        self._base_url = '{0}://{1}:{2}{3}/api/v2'.format(
            SCHEMA, HOST, PORT, PATH
        )
        self.name = name
        self.cmd = name
        self.payload = {
            'apikey': API_KEY,
            'cmd': self.cmd,
            'out_type': out_type,
            'callback': callback,
            'debug': debug
        }

        # Don't know if this will work in a base class or not.
        for key in kwargs:
            self.payload[key] = kwargs[key]
