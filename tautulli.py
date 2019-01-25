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


class Tautulli:

    def __init__(self):
        self._base_url = '{0}://{1}:{2}{3}/api/v2'.format(
            SCHEMA, HOST, PORT, PATH
        )
        # TODO: Figure out how the below ApiAuth works
        self.auth = TautulliApiAuth(api_key=API_KEY)

    def get_history(self, **kwargs):
        """
        Get the Tautulli history.

        Required parameters:
            None

        Optional parameters:
            grouping (int):                 0 or 1
            user (str):                     "Jon Snow"
            user_id (int):                  133788
            rating_key (int):               4348
            parent_rating_key (int):        544
            grandparent_rating_key (int):   351
            start_date (str):               "YYYY-MM-DD"
            section_id (int):               2
            media_type (str):               "movie", "episode", "track"
            transcode_decision (str):       "direct play", "copy", "transcode",
            order_column (str):             "date", "friendly_name",
                                            "ip_address", "platform", "player",
                                            "full_title", "started",
                                            "paused_counter", "stopped",
                                            "duration"
            order_dir (str):                "desc" or "asc",
                                            default: "desc"
            start (int):                    Row to start from,
                                            default: 0
            length (int):                   Number of items to return,
                                            default: 25
            search (str):                   A string to search for, "Thrones"

        Example usage:
            get_history(user="Jon Snow", order_dir="asc", length=20)
        """

        payload = {
            'apikey': API_KEY,
            'cmd': 'get_history',
            'grouping': None,                   # (int) 0 or 1
            'user': None,                       # (str)
            'user_id': None,                    # (int)
            'rating_key': None,                 # (int)
            'parent_rating_key': None,          # (int)
            'grandparent_rating_key': None,     # (int)
            'start_date': None,                 # (str) "YYYY-MM-DD"
            'section_id': None,                 # (int)
            'media_type': None,                 # (str)
            'transcode_decision': None,         # (str)
            'order_column': None,               # (str)
            'order_dir': None,                  # (str)
            'start': None,                      # (int)
            'length': None,                     # (str)
            'search': None                      # (str)
        }

        pos_int_params = [
            'user_id',
            'rating_key',
            'parent_rating_key',
            'grandparent_rating_key',
            'section_id',
            'start'
        ]

        str_params = [
            'user',
            'start_date',
            'media_type',
            'transcode_decision',
            'order_column',
            'order_dir',
            'length',
            'search'
        ]

        bin_params = [
            'grouping'
        ]

        # Parameter-check lists
        param_check_dict = {
            'media_type': ["movie", "episode", "track"],
            'transcode_decision': ["direct play", "copy", "transcode"],
            'order_column': [
                "date", "friendly_name", "ip_address", "platform", "player",
                "full_title", "started", "paused_counter", "stopped", "duration"
            ],
            'order_dir': ["desc", "asc"]
        }

        # Check parameters
        utils.check_kwargs(kwargs, payload)
        utils.check_param_types(
            kwargs, pos_int_params, str_params, bin_params, param_check_dict
        )

        # Send request
        response = utils.send_receive_request(
            self._base_url, params_dict=payload
        )
        # Return request
        return response
