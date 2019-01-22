import configparser
from .tautulli_api_auth import TautulliApiAuth
import json
import requests


# ConfigParser Variables
config = configparser.ConfigParser()
config.read('settings.ini')
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
            order_column (str):             "date",
            "friendly_name",
                                            "ip_address", "platform", "player",
                                            "full_title", "started",
                                            "paused_counter", "stopped",
                                            "duration"
            order_dir (str):                "desc" or "asc"
            start (int):                    Row to start from, 0
            length (int):                   Number of items to return, 25
            search (str):                   A string to search for, "Thrones"

        Example usage:
            Tautulli.get_history(
                user="Jon Snow",
                start_date="2018-01-01",
                order_dir="asc",
                length=200
            )
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

        # Parameter-check lists
        media_type_list = ["movie", "episode", "track"]
        transcode_decision_list = ["direct play", "copy", "transcode"]
        order_column_list = [
            "date", "friendly_name", "ip_address", "platform", "player",
            "full_title", "started", "paused_counter", "stopped", "duration"
        ]
        order_dir_list = ["desc", "asc"]

        # Put **kwargs into payload
        for k, v in kwargs.items():
            if k in payload:
                payload[k] = v
            else:
                raise ValueError(
                    '{0} is not an accepted parameter\n'.format(k)
                )

        # **kwarg checks

        if payload['grouping'] is not None:
            if payload['grouping'] == 0 | 1:
                pass
            else:
                raise TypeError(
                    '"grouping=<val>" <val> MUST be 0 or 1'
                )
        else:
            pass

        if payload['user'] is not None:
            if type(payload['user']) == str:
                pass
            else:
                raise TypeError(
                    '"user=<user_name>" <user_name> MUST be a STRING'
                )
        else:
            pass

        if payload['user_id'] is not None:
            if type(payload['user_id']) == int:
                pass
            else:
                raise TypeError(
                    '"user_id=<val>" <val> MUST be an INTEGER'
                )
        else:
            pass

        if payload['rating_key'] is not None:
            if type(payload['rating_key']) == int:
                pass
            else:
                raise TypeError(
                    '"rating_key=<val>" <val> MUST be an INTEGER'
                )
        else:
            pass

        if payload['parent_rating_key'] is not None:
            if type(payload['parent_rating_key']) == int:
                pass
            else:
                raise TypeError(
                    '"parent_rating_key=<val>" <val> MUST be an INTEGER'
                )
        else:
            pass

        if payload['grandparent_rating_key'] is not None:
            if type(payload['grandparent_rating_key']) == int:
                pass
            else:
                raise TypeError(
                    '"grandparent_rating_key=<val>" <val> MUST be an INTEGER'
                )
        else:
            pass

        if payload['start_date'] is not None:
            if type(payload['start_date']) == str:
                pass
            else:
                raise TypeError(
                    '"start_date=<YYYY-MM-DD>" <YYYY-MM-DD> MUST be a STRING'
                )
        else:
            pass

        if payload['section_id'] is not None:
            if type(payload['section_id']) == int:
                pass
            else:
                raise TypeError(
                    '"section_id=<val>" <val> MUST be an INTEGER'
                )
        else:
            pass

        if payload['media_type'] is not None:
            if type(payload['media_type']) == str:
                if payload['media_type'] in media_type_list:
                    pass
                else:
                    raise ValueError(
                        '"media_type=<val>" <val> MUST be one of the '
                        'following:\n'
                        '    "movie", "episode", "track"'
                    )
            else:
                raise TypeError(
                    '"media_type=<val>" <val> MUST be a STRING\n'
                    'ACCEPTED VALUES:\n'
                    '    "movie", "episode", "track"'
                )
        else:
            pass

        if payload['transcode_decision'] is not None:
            if type(payload['transcode_decision']) == str:
                if payload['transcode_decision'] in transcode_decision_list:
                    pass
                else:
                    raise ValueError(
                        '"transcode_decision=<val>" <val> MUST be one of the '
                        'following:\n'
                        '    "direct play", "copy", "transcode"'
                    )
            else:
                raise TypeError(
                    '"transcode_decision=<val>" <val> MUST be a STRING\n'
                    'ACCEPTED VALUES:\n'
                    '    "direct play", "copy", "transcode"'
                )
        else:
            pass

        if payload['order_column'] is not None:
            if type(payload['order_column']) == str:
                if payload['order_column'] in order_column_list:
                    pass
                else:
                    raise ValueError(
                        '"order_column=<val>" <val> MUST be one of the '
                        'following:\n'
                        '    "date", "friendly_name", "ip_address",\n'
                        '    "platform", "player", "full_title",\n'
                        '    "started", "paused_counter", "stopped",\n'
                        '    "duration"'
                    )
            else:
                raise TypeError(
                    '"order_column=<val>" <val> MUST be a STRING\n'
                    'ACCEPTED VALUES:\n'
                    '    "date", "friendly_name", "ip_address",\n'
                    '    "platform", "player", "full_title",\n'
                    '    "started", "paused_counter", "stopped",\n'
                    '    "duration"'
                )
        else:
            pass

        if payload['order_dir'] is not None:
            if type(payload['order_dir']) == str:
                if payload['order_dir'] in order_dir_list:
                    pass
                else:
                    raise ValueError(
                        '"order_dir=<val>" <val> MUST be one of the '
                        'following:\n'
                        '    "desc", "asc"'
                    )
            else:
                raise TypeError(
                    '"order_dir=<val>" <val> MUST be a STRING\n'
                    'ACCEPTED VALUES:\n'
                    '    "desc", "asc"'
                )
        else:
            pass

        if payload['start'] is not None:
            if type(payload['start']) == int:
                if payload['start'] >= 0:
                    pass
                else:
                    raise ValueError(
                        '"start=<val>" <val> CANNOT be NEGATIVE'
                    )
            else:
                raise TypeError(
                    '"start=<val>" <val> MUST be an INTEGER'
                )
        else:
            pass

        if payload['length'] is not None:
            if type(payload['length']) == int:
                if payload['length'] >= 0:
                    pass
                else:
                    raise ValueError(
                        '"length=<val>" <val> CANNOT be NEGATIVE'
                    )
            else:
                raise TypeError(
                    '"length=<val>" <val> MUST be an INTEGER'
                )
        else:
            pass

        if payload['search'] is not None:
            if type(payload['search']) == str:
                pass
            else:
                raise TypeError(
                    '"search=<search_str>" <search_str> MUST be a STRING'
                )
        else:
            pass

        r = requests.get(self._base_url, params=payload)
        if r.status_code == 200:
            records_total = json.loads(r.content.decode('utf-8'))
            records_total = records_total['response']
            records_total = json.dumps(records_total, sort_keys=True, indent=4)
            return records_total
