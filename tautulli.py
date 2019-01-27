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

        Returns:
        json:
            {"draw": 1,
             "recordsTotal": 1000,
             "recordsFiltered": 250,
             "total_duration": "42 days 5 hrs 18 mins",
             "filter_duration": "10 hrs 12 mins",
             "data":
                [{"date": 1462687607,
                  "duration": 263,
                  "friendly_name": "Mother of Dragons",
                  "full_title": "Game of Thrones - The Red Woman",
                  "grandparent_rating_key": 351,
                  "grandparent_title": "Game of Thrones",
                  "original_title": "",
                  "group_count": 1,
                  "group_ids": "1124",
                  "id": 1124,
                  "ip_address": "xxx.xxx.xxx.xxx",
                  "media_index": 17,
                  "media_type": "episode",
                  "parent_media_index": 7,
                  "parent_rating_key": 544,
                  "parent_title": "",
                  "paused_counter": 0,
                  "percent_complete": 84,
                  "platform": "Chrome",
                  "player": "Plex Web (Chrome)",
                  "rating_key": 4348,
                  "reference_id": 1123,
                  "session_key": null,
                  "started": 1462688107,
                  "state": null,
                  "stopped": 1462688370,
                  "thumb": "/library/metadata/4348/thumb/1462414561",
                  "title": "The Red Woman",
                  "transcode_decision": "transcode",
                  "user": "DanyKhaleesi69",
                  "user_id": 8008135,
                  "watched_status": 0,
                  "year": 2016
                  },
                 {...},
                 {...}
                 ]
             }

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
            kwargs,
            param_check_dict,
            pos_int_list=pos_int_params,
            str_list=str_params,
            bin_list=bin_params
        )

        # Send request
        response = utils.send_receive_request(
            self._base_url, params_dict=payload
        )
        # Return request
        return response

    def add_newsletter_config(self, agent_id=None):
        """
        Add a new notification agent.

        Required parameters:
            agent_id (int):           The newsletter type to add

        Optional parameters:
            None

        Returns:
            None
        """

        payload = {
            'apikey': API_KEY,
            'cmd': 'add_newsletter_config'
        }

        if agent_id is not None:
            if type(agent_id) == int:
                payload['agent_id'] = agent_id
            else:
                raise TypeError(
                    '"agent_id=<val>" <val> MUST be an INTEGER'
                )
        else:
            raise ValueError(
                '"agent_id" is a required keyword argument'
            )

        # Send request
        response = utils.send_receive_request(
            self._base_url, params_dict=payload
        )
        # Return request
        return response

    def add_notifier_config(self, agent_id=None):
        """
        Add a new notification agent.

        Required parameters:
            agent_id (int):           The notification agent to add

        Optional parameters:
            None

        Returns:
            None
        """

        payload = {
            'apikey': API_KEY,
            'cmd': 'add_notifier_config'
        }

        if agent_id is not None:
            if type(agent_id) == int:
                payload['agent_id'] = agent_id
            else:
                raise TypeError(
                    '"agent_id=<val>" <val> MUST be an INTEGER'
                )
        else:
            raise ValueError(
                '"agent_id" is a required keyword argument'
            )

        # Send request
        response = utils.send_receive_request(
            self._base_url, params_dict=payload
        )
        # Return request
        return response

    def arnold(self):
        """
        Get to the chopper!
        """

        payload = {
            'apikey': API_KEY,
            'cmd': 'arnold'
        }

        # Send request
        response = utils.send_receive_request(
            self._base_url, params_dict=payload
        )
        # Return request
        return response

    def backup_config(self):
        """
        Create a manual backup of the `config.ini` file.
        """

        payload = {
            'apikey': API_KEY,
            'cmd': 'backup_config'
        }

        # Send request
        response = utils.send_receive_request(
            self._base_url, params_dict=payload
        )
        # Return request
        return response

    def backup_db(self):
        """
        Create a manual backup of the `plexpy.db` file.
        """

        payload = {
            'apikey': API_KEY,
            'cmd': 'backup_db'
        }

        # Send request
        response = utils.send_receive_request(
            self._base_url, params_dict=payload
        )
        # Return request
        return response

    def delete_all_library_history(self, section_id=None):
        """
        Delete all Tautulli history for a specific library.

        Required parameters:
            section_id (str):       The id of the Plex library section

        Optional parameters:
            None

        Returns:
            None
        """

        payload = {
            'apikey': API_KEY,
            'cmd': 'delete_all_library_history'
        }

        if section_id is not None:
            if type(section_id) == str:
                payload['section_id'] = section_id
                # Send request
                response = utils.send_receive_request(
                    self._base_url, params_dict=payload
                )
                # Return request
                return response
            else:
                raise TypeError(
                    '"section_id=<val>" <val> MUST be a STRING'
                )
        else:
            raise ValueError(
                '"section_id" is a required keyword argument'
            )

    def delete_all_user_history(self, user_id=None):
        """
        Delete all Tautulli history for a specific user.

        Required parameters:
            user_id (str):          The id of the Plex user

        Optional parameters:
            None

        Returns:
            None
        """

        payload = {
            'apikey': API_KEY,
            'cmd': 'delete_all_user_history'
        }

        if user_id is not None:
            if type(user_id) == str:
                payload['user_id'] = user_id
            else:
                raise TypeError(
                    '"user_id=<val>" <val> MUST be a STRING'
                )
        else:
            raise ValueError(
                '"user_id" is a required keyword argument'
            )

        # Send request
        response = utils.send_receive_request(
            self._base_url, params_dict=payload
        )
        # Return request
        return response

    def delete_cache(self):
        """
        Delete and recreate the cache directory.
        """

        payload = {
            'apikey': API_KEY,
            'cmd': 'delete_cache'
        }

        # Send request
        response = utils.send_receive_request(
            self._base_url, params_dict=payload
        )
        # Return request
        return response

    def delete_hosted_images(self, **kwargs):
        """
        Delete the images uploaded to image hosting services.

        Required parameters:
            None

        Optional parameters:
            rating_key (int):       1234
                                    (Note: Must be the movie, show,
                                    season, artist, or album rating key)
            service (str):          'imgur' or 'cloudinary'
            delete_all (bool):      'true' to delete all images form
                                    the service

        Returns:
            json:
                {"result": "success",
                 "message": "Deleted hosted images from Imgur."}
        """

        payload = {
            'apikey': API_KEY,
            'cmd': 'delete_hosted_images',
            'rating_key': None,     # (int)
            'service': None,        # (str)
            'delete_all': None      # (bool)
        }

        pos_int_params = [
            'rating_key'
        ]

        str_params = [
            'service'
        ]

        bool_params = [
            'delete_all'
        ]

        # Check parameters
        utils.check_kwargs(kwargs, payload)
        utils.check_param_types(
            kwargs,
            pos_int_list=pos_int_params,
            str_list=str_params,
            bool_list=bool_params
        )

        # Send request
        response = utils.send_receive_request(
            self._base_url, params_dict=payload
        )
        # Return request
        return response

    def delete_image_cache(self):
        """
        Delete and recreate the image cache directory.
        """

        payload = {
            'apikey': API_KEY,
            'cmd': 'delete_image_cache'
        }

        # Send request
        response = utils.send_receive_request(
            self._base_url, params_dict=payload
        )
        # Return request
        return response

    def delete_library(self, section_id=None):
        """
        Delete a library section from Tautulli.
        Also erases all history for the library.


        Required parameters:
            section_id (str):       The id of the Plex library section

        Optional parameters:
            None

        Returns:
            None
        """

        payload = {
            'apikey': API_KEY,
            'cmd': 'delete_library'
        }

        if section_id is not None:
            if type(section_id) == str:
                payload['section_id'] = section_id
            else:
                raise TypeError(
                    '"section_id=<val>" <val> MUST be a STRING'
                )
        else:
            raise ValueError(
                '"section_id" is a required keyword argument'
            )

        # Send request
        response = utils.send_receive_request(
            self._base_url, params_dict=payload
        )
        # Return request
        return response

    def delete_login_log(self):
        """
        Delete the Tautulli login logs.

        Required parameters:
            None

        Optional parameters:
            None

        Returns:
            None
        """

        payload = {
            'apikey': API_KEY,
            'cmd': 'delete_login_log'
        }

        # Send request
        response = utils.send_receive_request(
            self._base_url, params_dict=payload
        )
        # Return request
        return response

    def delete_lookup_info(self, rating_key=None):
        """
        Delete the 3rd party API lookup info.

        Required parameters:
            rating_key (int):       1234
                                    (Note: Must be the movie, show,
                                    or artist rating key)
        Optional parameters:
            None

        Returns:
            json:
                {"result": "success",
                 "message": "Deleted lookup info."}
        """

        payload = {
            'apikey': API_KEY,
            'cmd': 'delete_lookup_info'
        }

        if rating_key is not None:
            if type(rating_key) == int:
                payload['rating_key'] = rating_key
            else:
                raise TypeError(
                    '"rating_key=<val>" <val> MUST be an INTEGER'
                )
        else:
            raise ValueError(
                '"rating_key" is a required keyword argument'
            )

        # Send request
        response = utils.send_receive_request(
            self._base_url, params_dict=payload
        )
        # Return request
        return response

    def delete_media_info_cache(self, section_id=None):
        """
        Delete the media info table cache for a specific library.

        Required parameters:
            section_id (str):       The id of the Plex library section

        Optional parameters:
            None

        Returns:
            None
        """

        payload = {
            'apikey': API_KEY,
            'cmd': 'delete_media_info_cache'
        }

        if section_id is not None:
            if type(section_id) == str:
                payload['section_id'] = section_id
            else:
                raise TypeError(
                    '"section_id=<val>" <val> MUST be a STRING'
                )
        else:
            raise ValueError(
                '"section_id" is a required keyword argument'
            )

        # Send request
        response = utils.send_receive_request(
            self._base_url, params_dict=payload
        )
        # Return request
        return response

    def delete_mobile_device(self, mobile_device_id=None):
        """
        Remove a mobile device from the database.

        Required parameters:
            mobile_device_id (int):        The device id to delete

        Optional parameters:
            None

        Returns:
            None
        """

        payload = {
            'apikey': API_KEY,
            'cmd': 'delete_mobile_device'
        }

        if mobile_device_id is not None:
            if type(mobile_device_id) == int:
                payload['mobile_device_id'] = mobile_device_id
            else:
                raise TypeError(
                    '"mobile_device_id=<val>" <val> MUST be an INTEGER'
                )
        else:
            raise ValueError(
                '"mobile_device_id" is a required keyword argument'
            )

        # Send request
        response = utils.send_receive_request(
            self._base_url, params_dict=payload
        )
        # Return request
        return response

    def delete_newsletter(self, newsletter_id=None):
        """
        Remove a newsletter from the database.

        Required parameters:
            newsletter_id (int):        The newsletter to delete

        Optional parameters:
            None

        Returns:
            None
        """

        payload = {
            'apikey': API_KEY,
            'cmd': 'delete_newsletter'
        }

        if newsletter_id is not None:
            if type(newsletter_id) == int:
                payload['newsletter_id'] = newsletter_id
            else:
                raise TypeError(
                    '"newsletter_id=<val>" <val> MUST be an INTEGER'
                )
        else:
            raise ValueError(
                '"newsletter_id" is a required keyword argument'
            )

        # Send request
        response = utils.send_receive_request(
            self._base_url, params_dict=payload
        )
        # Return request
        return response

    def delete_newsletter_log(self):
        """
        Delete the Tautulli newsletter logs.

        Required parameters:
            None

        Optional parameters:
            None

        Returns:
            None
        """

        payload = {
            'apikey': API_KEY,
            'cmd': 'delete_newsletter_log'
        }

        # Send request
        response = utils.send_receive_request(
            self._base_url, params_dict=payload
        )
        # Return request
        return response

    def delete_notification_log(self):
        """
        Delete the Tautulli notification logs.

        Required parameters:
            None

        Optional parameters:
            None

        Returns:
            None
        """

        payload = {
            'apikey': API_KEY,
            'cmd': 'delete_notification_log'
        }

        # Send request
        response = utils.send_receive_request(
            self._base_url, params_dict=payload
        )
        # Return request
        return response

    def delete_notifier(self, notifier_id=None):
        """
        Remove a notifier from the database.

        Required parameters:
            notifier_id (int):        The notifier to delete

        Optional parameters:
            None

        Returns:
            None
        """

        payload = {
            'apikey': API_KEY,
            'cmd': 'delete_temp_sessions',
            'notifier_id': notifier_id
        }

        if notifier_id is not None:
            utils.check_pos_int_kw(payload, notifier_id)
            # Send request
            response = utils.send_receive_request(
                self._base_url, params_dict=payload
            )
            # Return request
            return response
        else:
            raise ValueError(
                '"notifier_id" is a required keyword argument'
            )

    def delete_temp_sessions(self):
        """
        Flush out all of the temporary sessions in the database.
        """

        payload = {
            'apikey': API_KEY,
            'cmd': 'delete_temp_sessions'
        }

        # Send request
        response = utils.send_receive_request(
            self._base_url, params_dict=payload
        )
        # Return request
        return response

    def delete_user(self, user_id=None):
        """
        Delete a user from Tautulli. Also erases all history for the user.

        Required parameters:
            user_id (str):          The id of the Plex user

        Optional parameters:
            None

        Returns:
            None
        """

        payload = {
            'apikey': API_KEY,
            'cmd': 'delete_user'
        }

        if user_id is not None:
            if type(user_id) == str:
                payload['user_id'] = user_id
                # Send request
                response = utils.send_receive_request(
                    self._base_url, params_dict=payload
                )
                # Return request
                return response
            else:
                raise TypeError(
                    '"user_id=<val>" <val> MUST be a STRING'
                )
        else:
            raise ValueError(
                '"user_id" is a required keyword argument'
            )

    def docs(self):
        """
        Return the api docs as a dict where commands are keys,
        docstring are value.
        """

        payload = {
            'apikey': API_KEY,
            'cmd': 'docs'
        }

        # Send request
        response = utils.send_receive_request(
            self._base_url, params_dict=payload
        )
        # Return request
        return response

    def docs_md(self):
        """
        Return the api docs formatted with markdown.
        """

        payload = {
            'apikey': API_KEY,
            'cmd': 'docs_md'
        }

        # Send request
        response = utils.send_receive_request(
            self._base_url, params_dict=payload
        )
        # Return request
        return response

    def download_config(self):
        """
        Download the Tautulli configuration file.
        """

        payload = {
            'apikey': API_KEY,
            'cmd': 'download_config'
        }

        # Send request
        response = utils.send_receive_request(
            self._base_url, params_dict=payload
        )
        # Return request
        return response

    def download_database(self):
        """
        Download the Tautulli database file.
        """

        payload = {
            'apikey': API_KEY,
            'cmd': 'download_database'
        }

        # Send request
        response = utils.send_receive_request(
            self._base_url, params_dict=payload
        )
        # Return request
        return response

    def download_log(self):
        """
        Download the Tautulli log file.
        """

        payload = {
            'apikey': API_KEY,
            'cmd': 'download_log'
        }

        # Send request
        response = utils.send_receive_request(
            self._base_url, params_dict=payload
        )
        # Return request
        return response

    def download_plex_log(self):
        """
        Download the Plex log file.
        """

        payload = {
            'apikey': API_KEY,
            'cmd': 'download_plex_log'
        }

        # Send request
        response = utils.send_receive_request(
            self._base_url, params_dict=payload
        )
        # Return request
        return response

    def edit_library(self, section_id=None, custom_thumb=None,
                     keep_history=None):
        """
        Update a library section on Tautulli.

        Required parameters:
            section_id (str):           The id of the Plex library section

        Optional parameters:
            custom_thumb (str):         The URL for the custom
                                        library thumbnail
            keep_history (int):         0 or 1

        Returns:
            None
        """

        payload = {
            'apikey': API_KEY,
            'cmd': 'edit_library',
            'section_id': section_id,
            'custom_thumb': custom_thumb,
            'keep_history': keep_history
        }

        # Check keyword arguments
        utils.check_str_kw(payload, section_id, is_required=True)
        utils.check_str_kw(payload, custom_thumb, is_required=False)
        utils.check_bin_kw(payload, keep_history, is_required=False)

        # Send request
        utils.send_receive_request(self._base_url, params_dict=payload)

    def edit_user(self, user_id=None, friendly_name=None, custom_thumb=None,
                  keep_history=None, allow_guest=None):
        """
        Update a user on Tautulli.

        Required parameters:
            user_id (str):              The id of the Plex user

        Optional parameters:
            friendly_name(str):         The friendly name of the user
            custom_thumb (str):         The URL for the custom user thumbnail
            keep_history (int):         0 or 1
            allow_guest (int):          0 or 1

        Returns:
            None
        """

        payload = {
            'apikey': API_KEY,
            'cmd': 'edit_user',
            'user_id': user_id,
            'friendly_name': friendly_name,
            'custom_thumb': custom_thumb,
            'keep_history': keep_history,
            'allow_guest': allow_guest
        }

        # Check keyword arguments
        utils.check_str_kw(payload, user_id, is_required=True)
        utils.check_str_kw(payload, friendly_name, is_required=False)
        utils.check_str_kw(payload, custom_thumb, is_required=False)
        utils.check_bin_kw(payload, keep_history, is_required=False)
        utils.check_bool_kw(payload, allow_guest, is_required=False)

        # Send/receive request
        utils.send_receive_request(self._base_url, params_dict=payload)

    def get_activity(self, session_key=None, session_id=None):
        """
        Get the current activity on the PMS.

        Required parameters:
            None

        Optional parameters:
            session_key (int):    Session key for the session info to return, OR
            session_id (str):     Session ID for the session info to return

        Returns:
            json:
                {"lan_bandwidth": 25318,
                 "sessions": [
                     {
                         "actors": [
                             "Kit Harington",
                             "Emilia Clarke",
                             "Isaac Hempstead-Wright",
                             "Maisie Williams",
                             "Liam Cunningham",
                         ],
                         "added_at": "1461572396",
                         "allow_guest": 1,
                         "art": "/library/metadata/1219/art/1503306930",
                         "aspect_ratio": "1.78",
                         "audience_rating": "",
                         "audience_rating_image":
                            "rottentomatoes://image.rating.upright",
                         "audio_bitrate": "384",
                         "audio_bitrate_mode": "",
                         "audio_channel_layout": "5.1(side)",
                         "audio_channels": "6",
                         "audio_codec": "ac3",
                         "audio_decision": "direct play",
                         "audio_language": "",
                         "audio_language_code": "",
                         "audio_profile": "",
                         "audio_sample_rate": "48000",
                         "bandwidth": "25318",
                         "banner": "/library/metadata/1219/banner/1503306930",
                         "bif_thumb": "/library/parts/274169/indexes/sd/1000",
                         "bitrate": "10617",
                         "channel_stream": 0,
                         "collections": [],
                         "container": "mkv",
                         "content_rating": "TV-MA",
                         "deleted_user": 0,
                         "device": "Windows",
                         "directors": [
                             "Jeremy Podeswa"
                         ],
                         "do_notify": 0,
                         "duration": "2998272",
                         "email": "Jon.Snow.1337@CastleBlack.com",
                         "file": "/media/TV Shows/Game of
                            Thrones/Season 06/Game of Thrones -
                            S06E01 - The Red Woman.mkv",
                         "file_size": "3979115377",
                         "friendly_name": "Jon Snow",
                         "full_title": "Game of Thrones - The Red Woman",
                         "genres": [
                             "Adventure",
                             "Drama",
                             "Fantasy"
                         ],
                         "grandparent_rating_key": "1219",
                         "grandparent_thumb":
                            "/library/metadata/1219/thumb/1503306930",
                         "grandparent_title": "Game of Thrones",
                         "guid":
                            "com.plexapp.agents.thetvdb://121361/6/1?lang=en",
                         "height": "1078",
                         "id": "",
                         "indexes": 1,
                         "ip_address": "10.10.10.1",
                         "ip_address_public": "64.123.23.111",
                         "is_admin": 1,
                         "is_allow_sync": null,
                         "is_home_user": 1,
                         "is_restricted": 0,
                         "keep_history": 1,
                         "labels": [],
                         "last_viewed_at": "1462165717",
                         "library_name": "TV Shows",
                         "local": "1",
                         "location": "lan",
                         "machine_id": "lmd93nkn12k29j2lnm",
                         "media_index": "1",
                         "media_type": "episode",
                         "optimized_version": 0,
                         "optimized_version_profile": "",
                         "optimized_version_title": "",
                         "originally_available_at": "2016-04-24",
                         "original_title": "",
                         "parent_media_index": "6",
                         "parent_rating_key": "153036",
                         "parent_thumb":
                            "/library/metadata/153036/thumb/1503889210",
                         "parent_title": "Season 6",
                         "platform": "Plex Media Player",
                         "platform_name": "plex",
                         "platform_version": "2.4.1.787-54a020cd",
                         "player": "Castle-PC",
                         "product": "Plex Media Player",
                         "product_version": "3.35.2",
                         "profile": "Konvergo",
                         "progress_percent": "0",
                         "quality_profile": "Original",
                         "rating": "7.8",
                         "rating_image": "rottentomatoes://image.rating.ripe",
                         "rating_key": "153037",
                         "relay": 0,
                         "section_id": "2",
                         "session_id": "helf15l3rxgw01xxe0jf3l3d",
                         "session_key": "27",
                         "shared_libraries": [
                             "10",
                             "1",
                             "4",
                             "5",
                             "15",
                             "20",
                             "2"
                         ],
                         "sort_title": "Red Woman",
                         "state": "playing",
                         "stream_aspect_ratio": "1.78",
                         "stream_audio_bitrate": "384",
                         "stream_audio_bitrate_mode": "",
                         "stream_audio_channel_layout": "5.1(side)",
                         "stream_audio_channel_layout_": "5.1(side)",
                         "stream_audio_channels": "6",
                         "stream_audio_codec": "ac3",
                         "stream_audio_decision": "direct play",
                         "stream_audio_language": "",
                         "stream_audio_language_code": "",
                         "stream_audio_sample_rate": "48000",
                         "stream_bitrate": "10617",
                         "stream_container": "mkv",
                         "stream_container_decision": "direct play",
                         "stream_duration": "2998272",
                         "stream_subtitle_codec": "",
                         "stream_subtitle_container": "",
                         "stream_subtitle_decision": "",
                         "stream_subtitle_forced": 0,
                         "stream_subtitle_format": "",
                         "stream_subtitle_language": "",
                         "stream_subtitle_language_code": "",
                         "stream_subtitle_location": "",
                         "stream_video_bit_depth": "8",
                         "stream_video_bitrate": "10233",
                         "stream_video_codec": "h264",
                         "stream_video_codec_level": "41",
                         "stream_video_decision": "direct play",
                         "stream_video_framerate": "24p",
                         "stream_video_height": "1078",
                         "stream_video_language": "",
                         "stream_video_language_code": "",
                         "stream_video_ref_frames": "4",
                         "stream_video_resolution": "1080",
                         "stream_video_width": "1920",
                         "studio": "HBO",
                         "subtitle_codec": "",
                         "subtitle_container": "",
                         "subtitle_decision": "",
                         "subtitle_forced": 0,
                         "subtitle_format": "",
                         "subtitle_language": "",
                         "subtitle_language_code": "",
                         "subtitle_location": "",
                         "subtitles": 0,
                         "summary": "Jon Snow is dead. Daenerys
                            meets a strong man. Cersei sees her
                            daughter again.",
                         "synced_version": 0,
                         "synced_version_profile": "",
                         "tagline": "",
                         "throttled": "0",
                         "thumb": "/library/metadata/153037/thumb/1503889207",
                         "title": "The Red Woman",
                         "transcode_audio_channels": "",
                         "transcode_audio_codec": "",
                         "transcode_container": "",
                         "transcode_decision": "direct play",
                         "transcode_height": "",
                         "transcode_hw_decode": "",
                         "transcode_hw_decode_title": "",
                         "transcode_hw_decoding": 0,
                         "transcode_hw_encode": "",
                         "transcode_hw_encode_title": "",
                         "transcode_hw_encoding": 0,
                         "transcode_hw_full_pipeline": 0,
                         "transcode_hw_requested": 0,
                         "transcode_key": "",
                         "transcode_progress": 0,
                         "transcode_protocol": "",
                         "transcode_speed": "",
                         "transcode_throttled": 0,
                         "transcode_video_codec": "",
                         "transcode_width": "",
                         "type": "",
                         "updated_at": "1503889207",
                         "user": "LordCommanderSnow",
                         "user_id": 133788,
                         "user_rating": "",
                         "user_thumb":
                            "https://plex.tv/users/k10w42309cynaopq/avatar",
                         "username": "LordCommanderSnow",
                         "video_bit_depth": "8",
                         "video_bitrate": "10233",
                         "video_codec": "h264",
                         "video_codec_level": "41",
                         "video_decision": "direct play",
                         "video_frame_rate": "23.976",
                         "video_framerate": "24p",
                         "video_height": "1078",
                         "video_language": "",
                         "video_language_code": "",
                         "video_profile": "high",
                         "video_ref_frames": "4",
                         "video_resolution": "1080",
                         "video_width": "1920",
                         "view_offset": "1000",
                         "width": "1920",
                         "writers": [
                             "David Benioff",
                             "D. B. Weiss"
                         ],
                         "year": "2016"
                     }
                 ],
                 "stream_count": "1",
                 "stream_count_direct_play": 1,
                 "stream_count_direct_stream": 0,
                 "stream_count_transcode": 0,
                 "total_bandwidth": 25318,
                 "wan_bandwidth": 0
                 }
        """

        payload = {
            'apikey': API_KEY,
            'cmd': 'get_activity',
            'session_key': session_key,
            'session_id': session_id
        }

        # Check keyword arguments
        utils.check_pos_int_kw(payload, session_key, is_required=False)
        utils.check_str_kw(payload, session_id, is_required=False)

        # Send/receive request
        utils.send_receive_request(self._base_url, params_dict=payload)

    def get_apikey(self, username=None, password=None):
        """
        Get the apikey. Username and password are required if auth is enabled.
        Makes and saves the apikey if it does not exist.

        Required parameters:
            None

        Optional parameters:
            username (str):     Your Tautulli username
            password (str):     Your Tautulli password

        Returns:
            string:             "apikey"
        """

        payload = {
            'apikey': API_KEY,
            'cmd': 'get_apikey',
            'username': username,
            'password': password
        }

        # Check keyword arguments
        utils.check_str_kw(payload, username, is_required=False)
        utils.check_str_kw(payload, password, is_required=False)

        # Send/receive request
        utils.send_receive_request(self._base_url, params_dict=payload)

    def get_date_formats(self):
        """
        Get the date and time formats used by Tautulli.

        Required parameters:
            None

        Optional parameters:
            None

        Returns:
            json:
                {"date_format": "YYYY-MM-DD",
                 "time_format": "HH:mm",
                 }
        """

        payload = {
            'apikey': API_KEY,
            'cmd': 'get_date_formats'
        }

        # Send request
        response = utils.send_receive_request(
            self._base_url, params_dict=payload
        )
        # Return request
        return response

    def get_geoip_lookup(self, ip_address=None):
        """
        Get the geolocation info for an IP address.
        The GeoLite2 database must be installed.

        Required parameters:
            ip_address

        Optional parameters:
            None

        Returns:
            json:
                {"continent": "North America",
                 "country": "United States",
                 "region": "California",
                 "city": "Mountain View",
                 "postal_code": "94035",
                 "timezone": "America/Los_Angeles",
                 "latitude": 37.386,
                 "longitude": -122.0838,
                 "accuracy": 1000
                 }
            json:
                {"error": "The address 127.0.0.1 is not in the database."
                 }
        """

        payload = {
            'apikey': API_KEY,
            'cmd': 'get_geoip_lookup',
            'ip_address': ip_address
        }

        # Check keyword arguments
        utils.check_str_kw(payload, ip_address, is_required=True)

        # Send/receive request
        utils.send_receive_request(self._base_url, params_dict=payload)

    def get_home_stats(self, grouping=None, time_range=None, stats_type=None,
                       stats_count=None):
        """
        Get the homepage watch statistics.

        Required parameters:
            None

        Optional parameters:
            grouping (int):         0 or 1
            time_range (str):       The time range to calculate statistics, '30'
            stats_type (int):       0 for plays, 1 for duration
            stats_count (str):      The number of top items to list, '5'

        Returns:
            json:
                [{"stat_id": "top_movies",
                  "stat_type": "total_plays",
                  "rows": [{...}]
                  },
                 {"stat_id": "popular_movies",
                  "rows": [{...}]
                  },
                 {"stat_id": "top_tv",
                  "stat_type": "total_plays",
                  "rows":
                    [{"content_rating": "TV-MA",
                      "friendly_name": "",
                      "grandparent_thumb":
                        "/library/metadata/1219/thumb/1462175063",
                      "labels": [],
                      "last_play": 1462380698,
                      "media_type": "episode",
                      "platform": "",
                      "platform_type": "",
                      "rating_key": 1219,
                      "row_id": 1116,
                      "section_id": 2,
                      "thumb": "",
                      "title": "Game of Thrones",
                      "total_duration": 213302,
                      "total_plays": 69,
                      "user": "",
                      "users_watched": ""
                      },
                     {...},
                     {...}
                     ]
                  },
                 {"stat_id": "popular_tv",
                  "rows": [{...}]
                  },
                 {"stat_id": "top_music",
                  "stat_type": "total_plays",
                  "rows": [{...}]
                  },
                 {"stat_id": "popular_music",
                  "rows": [{...}]
                  },
                 {"stat_id": "last_watched",
                  "rows": [{...}]
                  },
                 {"stat_id": "top_users",
                  "stat_type": "total_plays",
                  "rows": [{...}]
                  },
                 {"stat_id": "top_platforms",
                  "stat_type": "total_plays",
                  "rows": [{...}]
                  },
                 {"stat_id": "most_concurrent",
                  "rows": [{...}]
                  }
                 ]
        """

        payload = {
            'apikey': API_KEY,
            'cmd': 'get_home_stats',
            'grouping': grouping,
            'time_range': time_range,
            'stats_type': stats_type,
            'stats_count': stats_count
        }

        # Check keyword arguments
        utils.check_bin_kw(payload, grouping, is_required=False)
        utils.check_str_kw(payload, time_range, is_required=False)
        utils.check_bin_kw(payload, stats_type, is_required=False)
        utils.check_str_kw(payload, stats_count, is_required=False)

        # Send/receive request
        utils.send_receive_request(self._base_url, params_dict=payload)

    def get_libraries(self):
        """
        Get a list of all libraries on your server.

        Required parameters:
            None

        Optional parameters:
            None

        Returns:
            json:
                [{"art": "/:/resources/show-fanart.jpg",
                  "child_count": "3745",
                  "count": "62",
                  "parent_count": "240",
                  "section_id": "2",
                  "section_name": "TV Shows",
                  "section_type": "show",
                  "thumb": "/:/resources/show.png"
                  },
                 {...},
                 {...}
                 ]
        """

        payload = {
            'apikey': API_KEY,
            'cmd': 'get_libraries'
        }

        # Send request
        response = utils.send_receive_request(
            self._base_url, params_dict=payload
        )
        # Return request
        return response

    def get_libraries_table(self, order_column=None, order_dir=None,
                            start=None, length=None, search=None):
        """
        Get the data on the Tautulli libraries table.

        Required parameters:
            None

        Optional parameters:
            order_column (str):             "library_thumb", "section_name",
                                            "section_type", "count",
                                            "parent_count", "child_count",
                                            "last_accessed", "last_played",
                                            "plays", "duration"
            order_dir (str):                "desc" or "asc"
            start (int):                    Row to start from, 0
            length (int):                   Number of items to return, 25
            search (str):                   A string to search for, "Movies"

        Returns:
            json:
                {"draw": 1,
                 "recordsTotal": 10,
                 "recordsFiltered": 10,
                 "data":
                    [{"child_count": 3745,
                      "content_rating": "TV-MA",
                      "count": 62,
                      "do_notify": "Checked",
                      "do_notify_created": "Checked",
                      "duration": 1578037,
                      "id": 1128,
                      "keep_history": "Checked",
                      "labels": [],
                      "last_accessed": 1462693216,
                      "last_played": "Game of Thrones - The Red Woman",
                      "library_art": "/:/resources/show-fanart.jpg",
                      "library_thumb": "",
                      "media_index": 1,
                      "media_type": "episode",
                      "parent_count": 240,
                      "parent_media_index": 6,
                      "parent_title": "",
                      "plays": 772,
                      "rating_key": 153037,
                      "section_id": 2,
                      "section_name": "TV Shows",
                      "section_type": "Show",
                      "thumb": "/library/metadata/153036/thumb/1462175062",
                      "year": 2016
                      },
                     {...},
                     {...}
                     ]
                 }
        """

        payload = {
            'apikey': API_KEY,
            'cmd': 'get_libraries_table',
            'order_column': order_column,
            'order_dir': order_dir,
            'start': start,
            'length': length,
            'search': search
        }

        order_column_list = [
            "library_thumb", "section_name", "section_type", "count",
            "parent_count", "child_count", "last_accessed", "last_played",
            "plays", "duration"
        ]

        order_dir_list = ["asc", "desc"]

        # Check keyword arguments
        utils.check_str_kw(payload, order_column, order_column_list,
                           is_required=False)
        utils.check_str_kw(payload, order_dir, order_dir_list,
                           is_required=False)
        utils.check_pos_int_kw(payload, start, is_required=False)
        utils.check_pos_int_kw(payload, length, is_required=False)
        utils.check_str_kw(payload, search, is_required=False)

        # Send/receive request
        utils.send_receive_request(self._base_url, params_dict=payload)

    def get_library(self, section_id=None):
        """
        Get a library's details.

        Required parameters:
            section_id (int):               The id of the Plex library section

        Optional parameters:
            None

        Returns:
            json:
                {"child_count": null,
                 "count": 887,
                 "do_notify": 1,
                 "do_notify_created": 1,
                 "keep_history": 1,
                 "library_art": "/:/resources/movie-fanart.jpg",
                 "library_thumb": "/:/resources/movie.png",
                 "parent_count": null,
                 "section_id": 1,
                 "section_name": "Movies",
                 "section_type": "movie"
                 }
        """

        payload = {
            'apikey': API_KEY,
            'cmd': 'get_library',
            'section_id': section_id
        }

        # Check keyword arguments
        utils.check_pos_int_kw(payload, section_id, is_required=True)

        # Send/receive request
        utils.send_receive_request(self._base_url, params_dict=payload)

    def get_library_media_info(self, section_id=None, rating_key=None,
                               section_type=None, order_column=None,
                               order_dir=None, start=None, length=None,
                               search=None, refresh=None):
        """
        Get the data on the Tautulli media info tables.

        Required parameters:
            section_id (int):               The id of the Plex library
                                            section, OR
            rating_key (str):               The grandparent or parent rating key

        Optional parameters:
            section_type (str):             "movie", "show", "artist", "photo"
            order_column (str):             "added_at", "sort_title",
                                            "container", "bitrate",
                                            "video_codec", "video_resolution",
                                            "video_framerate", "audio_codec",
                                            "audio_channels", "file_size",
                                            "last_played", "play_count"
            order_dir (str):                "desc" or "asc"
            start (int):                    Row to start from, 0
            length (int):                   Number of items to return, 25
            search (str):                   A string to search for, "Thrones"
            refresh (str):                  "true" to refresh the media
                                            info table

        Returns:
            json:
                {"draw": 1,
                 "recordsTotal": 82,
                 "recordsFiltered": 82,
                 "filtered_file_size": 2616760056742,
                 "total_file_size": 2616760056742,
                 "data":
                    [{"added_at": "1403553078",
                      "audio_channels": "",
                      "audio_codec": "",
                      "bitrate": "",
                      "container": "",
                      "file_size": 253660175293,
                      "grandparent_rating_key": "",
                      "last_played": 1462380698,
                      "media_index": "1",
                      "media_type": "show",
                      "parent_media_index": "",
                      "parent_rating_key": "",
                      "play_count": 15,
                      "rating_key": "1219",
                      "section_id": 2,
                      "section_type": "show",
                      "thumb": "/library/metadata/1219/thumb/1436265995",
                      "title": "Game of Thrones",
                      "video_codec": "",
                      "video_framerate": "",
                      "video_resolution": "",
                      "year": "2011"
                      },
                     {...},
                     {...}
                     ]
                 }
        """

        payload = {
            'apikey': API_KEY,
            'cmd': 'get_library_media_info',
            'section_id': section_id,           # (int)
            'rating_key': rating_key,           # (str)
            'section_type': section_type,       # (str)
            'order_column': order_column,       # (str)
            'order_dir': order_dir,             # (str)
            'start': start,                     # (int)
            'length': length,                   # (int)
            'search': search,                   # (str)
            'refresh': refresh                  # (str)
        }

        section_type_list = ["movie", "show", "artist", "photo"]
        order_column_list = [
            "added_at", "sort_title", "container", "bitrate", "video_codec",
            "video_resolution", "video_framerate", "audio_codec",
            "audio_channels",  "file_size", "last_played", "play_count"
        ]
        order_dir_list = ["desc", "asc"]

        # Check for ONLY one required arguments
        if section_id and rating_key is None:
            raise ValueError(
                'Either "section_id" OR "rating_key" is required'
            )
        elif section_id and rating_key is not None:
            raise ValueError(
                'Only ONE required argument ("section_id" OR "rating_key") '
                'is required'
            )
        elif section_id is not None:
            utils.check_pos_int_kw(payload, section_id)
        elif rating_key is not None:
            utils.check_str_kw(payload, rating_key)

        # Check optional keyword arguments
        utils.check_str_kw(payload, section_type, section_type_list)
        utils.check_str_kw(payload, order_column, order_column_list)
        utils.check_str_kw(payload, order_dir, order_dir_list)
        utils.check_pos_int_kw(payload, start)
        utils.check_pos_int_kw(payload, length)
        utils.check_str_kw(payload, search)
        utils.check_str_kw(payload, refresh)

        # Send/receive request
        utils.send_receive_request(self._base_url, params_dict=payload)

    def get_library_names(self):
        """
        Get a list of library sections and ids on the PMS.

        Required parameters:
            None

        Optional parameters:
            None

        Returns:
            json:
                [{"section_id": 1,
                  "section_name": "Movies",
                  "section_type": "movie"
                  },
                 {"section_id": 7,
                  "section_name": "Music",
                  "section_type": "artist"
                  },
                 {"section_id": 2,
                  "section_name": "TV Shows",
                  "section_type": "show"
                  },
                 {...}
                 ]
        """

        payload = {
            'apikey': API_KEY,
            'cmd': 'get_library_names'
        }

        # Send/receive request
        utils.send_receive_request(self._base_url, params_dict=payload)

    def get_library_user_stats(self, section_id=None, grouping=None):
        """
        Get a library's user statistics.

        Required parameters:
            section_id (int):               The id of the Plex library section

        Optional parameters:
            grouping (int):         0 or 1

        Returns:
            json:
                [{"friendly_name": "Jon Snow",
                  "total_plays": 170,
                  "user_id": 133788,
                  "user_thumb": "https://plex.tv/users/k10w42309cynaopq/avatar"
                  },
                 {"platform_type": "DanyKhaleesi69",
                  "total_plays": 42,
                  "user_id": 8008135,
                  "user_thumb": "https://plex.tv/users/568gwwoib5t98a3a/avatar"
                  },
                 {...},
                 {...}
                 ]
        """

        payload = {
            'apikey': API_KEY,
            'cmd': 'get_library_user_stats',
            'section_id': section_id,           # (int)
            'grouping': grouping                # (int) 0 or 1
        }

        # Check keyword arguments
        utils.check_pos_int_kw(payload, section_id, is_required=True)
        utils.check_bin_kw(payload, grouping, is_required=False)

        # Send/receive request
        utils.send_receive_request(self._base_url, params_dict=payload)

    def get_library_watch_time_stats(self, section_id=None, grouping=None):
        """
        Get a library's watch time statistics.

        Required parameters:
            section_id (int):               The id of the Plex library section

        Optional parameters:
            grouping (int):         0 or 1

        Returns:
            json:
                [{"query_days": 1,
                  "total_plays": 0,
                  "total_time": 0
                  },
                 {"query_days": 7,
                  "total_plays": 3,
                  "total_time": 15694
                  },
                 {"query_days": 30,
                  "total_plays": 35,
                  "total_time": 63054
                  },
                 {"query_days": 0,
                  "total_plays": 508,
                  "total_time": 1183080
                  }
                 ]
        """

        payload = {
            'apikey': API_KEY,
            'cmd': 'get_library_watch_time_stats',
            'section_id': section_id,               # (int)
            'grouping': grouping                    # (int) 0 or 1
        }

        # Check keyword arguments
        utils.check_pos_int_kw(payload, section_id, is_required=True)
        utils.check_bin_kw(payload, grouping, is_required=False)

        # Send/receive request
        utils.send_receive_request(self._base_url, params_dict=payload)

    def get_logs(self, sort=None, search=None, order=None, regex=None,
                 start=None, end=None):
        """
        Get the Tautulli logs.

        Required parameters:
            None

        Optional parameters:
            sort (str):         "time", "thread", "msg", "loglevel"
            search (str):       A string to search for
            order (str):        "desc" or "asc"
            regex (str):        A regex string to search for
            start (int):        Row number to start from
            end (int):          Row number to end at

        Returns:
            json:
                [{"loglevel": "DEBUG",
                  "msg": "Latest version is
                         2d10b0748c7fa2ee4cf59960c3d3fffc6aa9512b",
                  "thread": "MainThread",
                  "time": "2016-05-08 09:36:51 "
                  },
                 {...},
                 {...}
                 ]
        """

        payload = {
            'apikey': API_KEY,
            'cmd': 'get_logs',
            'sort': sort,           # (str)
            'search': search,       # (str)
            'order': order,         # (str)
            'regex': regex,         # (str)
            'start': start,         # (int)
            'end': start            # (int)
        }

        sort_list = ["time", "thread", "msg", "loglevel"]
        order_list = ["desc", "asc"]

        # Check keyword arguments
        utils.check_str_kw(payload, sort, sort_list, is_required=False)
        utils.check_str_kw(payload, search, is_required=False)
        utils.check_str_kw(payload, order, order_list, is_required=False)
        utils.check_str_kw(payload, regex, is_required=False)
        utils.check_pos_int_kw(payload, start, is_required=False)
        utils.check_pos_int_kw(payload, end, is_required=False)

        # Send/receive request
        utils.send_receive_request(self._base_url, params_dict=payload)

    def get_metadata(self, rating_key=None):
        """
        Get the metadata for a media item.

        Required parameters:
            rating_key (str):       Rating key of the item

        Optional parameters:
            None

        Returns:
            json:
                {"actors": [
                    "Kit Harington",
                    "Emilia Clarke",
                    "Isaac Hempstead-Wright",
                    "Maisie Williams",
                    "Liam Cunningham",
                 ],
                 "added_at": "1461572396",
                 "art": "/library/metadata/1219/art/1462175063",
                 "audience_rating": "8",
                 "audience_rating_image":
                    "rottentomatoes://image.rating.upright",
                 "banner": "/library/metadata/1219/banner/1462175063",
                 "collections": [],
                 "content_rating": "TV-MA",
                 "directors": [
                    "Jeremy Podeswa"
                 ],
                 "duration": "2998290",
                 "full_title": "Game of Thrones - The Red Woman",
                 "genres": [
                    "Adventure",
                    "Drama",
                    "Fantasy"
                 ],
                 "grandparent_rating_key": "1219",
                 "grandparent_thumb": "/library/metadata/1219/thumb/1462175063",
                 "grandparent_title": "Game of Thrones",
                 "guid": "com.plexapp.agents.thetvdb://121361/6/1?lang=en",
                 "labels": [],
                 "last_viewed_at": "1462165717",
                 "library_name": "TV Shows",
                 "media_index": "1",
                 "media_info": [
                     {
                         "aspect_ratio": "1.78",
                         "audio_channel_layout": "5.1",
                         "audio_channels": "6",
                         "audio_codec": "ac3",
                         "audio_profile": "",
                         "bitrate": "10617",
                         "container": "mkv",
                         "height": "1078",
                         "id": "257925",
                         "optimized_version": 0,
                         "parts": [
                             {
                                 "file": "/media/TV Shows/Game of
                                         Thrones/Season 06/Game of Thrones -
                                         S06E01 - The Red Woman.mkv",
                                 "file_size": "3979115377",
                                 "id": "274169",
                                 "indexes": 1,
                                 "streams": [
                                     {
                                         "id": "511663",
                                         "type": "1",
                                         "video_bit_depth": "8",
                                         "video_bitrate": "10233",
                                         "video_codec": "h264",
                                         "video_codec_level": "41",
                                         "video_frame_rate": "23.976",
                                         "video_height": "1078",
                                         "video_language": "",
                                         "video_language_code": "",
                                         "video_profile": "high",
                                         "video_ref_frames": "4",
                                         "video_width": "1920",
                                         "selected": 0
                                     },
                                     {
                                         "audio_bitrate": "384",
                                         "audio_bitrate_mode": "",
                                         "audio_channel_layout": "5.1(side)",
                                         "audio_channels": "6",
                                         "audio_codec": "ac3",
                                         "audio_language": "",
                                         "audio_language_code": "",
                                         "audio_profile": "",
                                         "audio_sample_rate": "48000",
                                         "id": "511664",
                                         "type": "2",
                                         "selected": 1
                                     },
                                     {
                                         "id": "511953",
                                         "subtitle_codec": "srt",
                                         "subtitle_container": "",
                                         "subtitle_forced": 0,
                                         "subtitle_format": "srt",
                                         "subtitle_language": "English",
                                         "subtitle_language_code": "eng",
                                         "subtitle_location": "external",
                                         "type": "3",
                                         "selected": 1
                                     }
                                 ]
                             }
                         ],
                         "video_codec": "h264",
                         "video_framerate": "24p",
                         "video_profile": "high",
                         "video_resolution": "1080",
                         "width": "1920"
                     }
                 ],
                 "media_type": "episode",
                 "original_title": "",
                 "originally_available_at": "2016-04-24",
                 "parent_media_index": "6",
                 "parent_rating_key": "153036",
                 "parent_thumb": "/library/metadata/153036/thumb/1462175062",
                 "parent_title": "",
                 "rating": "7.8",
                 "rating_image": "rottentomatoes://image.rating.ripe",
                 "rating_key": "153037",
                 "section_id": "2",
                 "sort_title": "Game of Thrones",
                 "studio": "HBO",
                 "summary": "Jon Snow is dead. Daenerys meets a strong man.
                            Cersei sees her daughter again.",
                 "tagline": "",
                 "thumb": "/library/metadata/153037/thumb/1462175060",
                 "title": "The Red Woman",
                 "user_rating": "9.0",
                 "updated_at": "1462175060",
                 "writers": [
                    "David Benioff",
                    "D. B. Weiss"
                 ],
                 "year": "2016"
                 }
        """

        payload = {
            'apikey': API_KEY,
            'cmd': 'get_metadata',
            'rating_key': rating_key
        }

        # Check keyword arguments
        utils.check_str_kw(payload, rating_key, is_required=True)

        # Send/receive request
        utils.send_receive_request(self._base_url, params_dict=payload)

    def get_new_rating_keys(self, rating_key=None, media_type=None):
        """
        Get a list of new rating keys for the PMS of all of the
        item's parent/children.

        Required parameters:
            rating_key (str):       '12345'
            media_type (str):       "movie", "show", "season",
                                    "episode", "artist", "album",
                                    "track"

        Optional parameters:
            None

        Returns:
            json:
                {}
        """

        payload = {
            'apikey': API_KEY,
            'cmd': 'get_new_rating_keys',
            'rating_key': rating_key,
            'media_type': media_type
        }

        media_type_list = ['movie', 'show', 'season', 'episode', 'artist',
                           'album', 'track']

        # Check keyword arguments
        utils.check_str_kw(payload, rating_key, is_required=True)
        utils.check_str_kw(payload, media_type, media_type_list,
                           is_required=True)

        # Send/receive request
        utils.send_receive_request(self._base_url, params_dict=payload)

    def get_newsletter_config(self, newsletter_id=None):
        """
        Get the configuration for an existing notification agent.

        Required parameters:
            newsletter_id (int):        The newsletter config to retrieve

        Optional parameters:
            None

        Returns:
            json:
                {"id": 1,
                 "agent_id": 0,
                 "agent_name": "recently_added",
                 "agent_label": "Recently Added",
                 "friendly_name": "",
                 "id_name": "",
                 "cron": "0 0 * * 1",
                 "active": 1,
                 "subject": "Recently Added to {server_name}! ({end_date})",
                 "body": "View the newsletter here: {newsletter_url}",
                 "message": "",
                 "config": {"custom_cron": 0,
                            "filename": "newsletter_{newsletter_uuid}.html",
                            "formatted": 1,
                            "incl_libraries": ["1", "2"],
                            "notifier_id": 1,
                            "save_only": 0,
                            "time_frame": 7,
                            "time_frame_units": "days"
                            },
                 "email_config": {...},
                 "config_options": [{...}, ...],
                 "email_config_options": [{...}, ...]
                 }
        """

        payload = {
            'apikey': API_KEY,
            'cmd': 'get_newsletter_config',
            'newsletter_id': newsletter_id      # (int)
        }

        # Check keyword arguments
        utils.check_pos_int_kw(payload, newsletter_id, is_required=True)

        # Send/receive request
        utils.send_receive_request(self._base_url, params_dict=payload)

    def get_newsletter_log(self, order_column=None, order_dir=None,
                           start=None, length=None, search=None):
        """
        Get the data on the Tautulli newsletter logs table.

        Required parameters:
            None

        Optional parameters:
            order_column (str):             "timestamp", "newsletter_id",
                                            "agent_name", "notify_action",
                                            "subject_text", "start_date",
                                            "end_date", "uuid"
            order_dir (str):                "desc" or "asc"
            start (int):                    Row to start from, 0
            length (int):                   Number of items to return, 25
            search (str):                   A string to search for, "Telegram"

        Returns:
            json:
                {"draw": 1,
                 "recordsTotal": 1039,
                 "recordsFiltered": 163,
                 "data":
                    [{"agent_id": 0,
                      "agent_name": "recently_added",
                      "end_date": "2018-03-18",
                      "id": 7,
                      "newsletter_id": 1,
                      "notify_action": "on_cron",
                      "start_date": "2018-03-05",
                      "subject_text": "Recently Added to Plex
                                      (Winterfell-Server)! (2018-03-18)",
                      "success": 1,
                      "timestamp": 1462253821,
                      "uuid": "7fe4g65i"
                      },
                     {...},
                     {...}
                     ]
                 }
        """

        payload = {
            'apikey': API_KEY,
            'cmd': 'get_newsletter_log',
            'order_column': order_column,   # (str)
            'order_dir': order_dir,         # (str)
            'start': start,                 # (int)
            'length': length,               # (int)
            'search': search                # (str)
        }

        order_column_list = ["timestamp", "newsletter_id", "agent_name",
                             "notify_action", "subject_text", "start_date",
                             "end_date", "uuid"]
        order_dir_list = ["desc", "asc"]

        # Check keyword arguments
        utils.check_str_kw(payload, order_column, order_column_list,
                           is_required=False)
        utils.check_str_kw(payload, order_dir, order_dir_list,
                           is_required=False)
        utils.check_pos_int_kw(payload, start, is_required=False)
        utils.check_pos_int_kw(payload, length, is_required=False)
        utils.check_str_kw(payload, search, is_required=False)

        # Send/receive request
        utils.send_receive_request(self._base_url, params_dict=payload)

    def get_newsletters(self):
        """
        Get a list of configured newsletters.

        Required parameters:
            None

        Optional parameters:
            None

        Returns:
            json:
                [{"id": 1,
                  "agent_id": 0,
                  "agent_name": "recently_added",
                  "agent_label": "Recently Added",
                  "friendly_name": "",
                  "cron": "0 0 * * 1",
                  "active": 1
                  }
                 ]
        """

        payload = {
            'apikey': API_KEY,
            'cmd': 'get_newsletters'
        }

        # Send/receive request
        utils.send_receive_request(self._base_url, params_dict=payload)

    def get_notification_log(self, order_column=None, order_dir=None,
                             start=None, length=None, search=None):
        """
        Get the data on the Tautulli notification logs table.

        Required parameters:
            None

        Optional parameters:
            order_column (str):             "timestamp", "notifier_id",
                                            "agent_name", "notify_action",
                                            "subject_text", "body_text"
            order_dir (str):                "desc" or "asc"
            start (int):                    Row to start from, 0
            length (int):                   Number of items to return, 25
            search (str):                   A string to search for, "Telegram"

        Returns:
            json:
                {"draw": 1,
                 "recordsTotal": 1039,
                 "recordsFiltered": 163,
                 "data":
                    [{"agent_id": 13,
                      "agent_name": "telegram",
                      "body_text": "DanyKhaleesi69 started playing
                                   The Red Woman.",
                      "id": 1000,
                      "notify_action": "on_play",
                      "rating_key": 153037,
                      "session_key": 147,
                      "subject_text": "Tautulli (Winterfell-Server)",
                      "success": 1,
                      "timestamp": 1462253821,
                      "user": "DanyKhaleesi69",
                      "user_id": 8008135
                      },
                     {...},
                     {...}
                     ]
                 }
        """

        payload = {
            'apikey': API_KEY,
            'cmd': 'get_notification_log',
            'order_column': order_column,   # (str)
            'order_dir': order_dir,         # (str)
            'start': start,                 # (int)
            'length': length,               # (int)
            'search': search                # (str)
        }

        order_column_list = ["timestamp", "notifier_id", "agent_name",
                             "notify_action", "subject_text", "body_text"]
        order_dir_list = ["desc", "asc"]

        # Check keyword arguments
        utils.check_str_kw(payload, order_column, order_column_list,
                           is_required=False)
        utils.check_str_kw(payload, order_dir, order_dir_list,
                           is_required=False)
        utils.check_pos_int_kw(payload, start, is_required=False)
        utils.check_pos_int_kw(payload, length, is_required=False)
        utils.check_str_kw(payload, search, is_required=False)

        # Send/receive request
        utils.send_receive_request(self._base_url, params_dict=payload)

    def get_notifier_config(self, notifier_id=None):
        """
        Get the configuration for an existing notification agent.

        Required parameters:
            notifier_id (int):        The notifier config to retrieve

        Optional parameters:
            None

        Returns:
            json:
                {"id": 1,
                 "agent_id": 13,
                 "agent_name": "telegram",
                 "agent_label": "Telegram",
                 "friendly_name": "",
                 "config": {"incl_poster": 0,
                            "html_support": 1,
                            "chat_id": "123456",
                            "bot_token": "13456789:fio9040NNo04jLEp-4S",
                            "incl_subject": 1,
                            "disable_web_preview": 0
                            },
                 "config_options": [{...}, ...]
                 "actions": {"on_play": 0,
                             "on_stop": 0,
                             ...
                             },
                 "notify_text": {"on_play": {"subject": "...",
                                             "body": "..."
                                             }
                                 "on_stop": {"subject": "...",
                                             "body": "..."
                                             }
                                 ...
                                 }
                 }
        """

        payload = {
            'apikey': API_KEY,
            'cmd': 'get_notifier_config',
            'notifier_id': notifier_id          # (int)
        }

        # Check keyword arguments
        utils.check_pos_int_kw(payload, notifier_id, is_required=True)

        # Send/receive request
        utils.send_receive_request(self._base_url, params_dict=payload)

    def get_notifier_parameters(self):
        """
        Get the list of available notification parameters.

        Required parameters:
            None

        Optional parameters:
            None

        Returns:
            json:
                {
                 }
        """

        payload = {
            'apikey': API_KEY,
            'cmd': 'get_notifier_parameters'
        }

        # Send/receive request
        utils.send_receive_request(self._base_url, params_dict=payload)

    def get_notifiers(self, notify_action=None):
        """
        Get a list of configured notifiers.

        Required parameters:
            None

        Optional parameters:
            notify_action (str):        The notification action to filter out

        Returns:
            json:
                [{"id": 1,
                  "agent_id": 13,
                  "agent_name": "telegram",
                  "agent_label": "Telegram",
                  "friendly_name": "",
                  "active": 1
                  }
                 ]
        """

        payload = {
            'apikey': API_KEY,
            'cmd': 'get_notifiers',
            'notify_action': notify_action      # (str)
        }

        # Check keyword arguments
        utils.check_str_kw(payload, notify_action, is_required=False)

        # Send/receive request
        utils.send_receive_request(self._base_url, params_dict=payload)
        
    def get_old_rating_keys(self, rating_key=None, media_type=None):
        """
        Get a list of old rating keys from the Tautulli database for all
        of the item's parent/children.

        Required parameters:
            rating_key (str):       '12345'
            media_type (str):       "movie", "show", "season",
                                    "episode", "artist", "album",
                                    "track"

        Optional parameters:
            None

        Returns:
            json:
                {}
        """

        payload = {
            'apikey': API_KEY,
            'cmd': 'get_old_rating_keys',
            'rating_key': rating_key,
            'media_type': media_type
        }

        media_type_list = ['movie', 'show', 'season', 'episode', 'artist',
                           'album', 'track']

        # Check keyword arguments
        utils.check_str_kw(payload, rating_key, is_required=True)
        utils.check_str_kw(payload, media_type, media_type_list,
                           is_required=True)

        # Send/receive request
        utils.send_receive_request(self._base_url, params_dict=payload)

    def get_plays_by_date(self, time_range=None, y_axis=None, user_id=None,
                          grouping=None):
        """
        Get graph data by date.

        Required parameters:
            None

        Optional parameters:
            time_range (str):       The number of days of data to return
            y_axis (str):           "plays" or "duration"
            user_id (str):          The user id to filter the data
            grouping (int):         0 or 1

        Returns:
            json:
                {"categories":
                    ["YYYY-MM-DD", "YYYY-MM-DD", ...]
                 "series":
                    [{"name": "Movies", "data": [...]}
                     {"name": "TV", "data": [...]},
                     {"name": "Music", "data": [...]}
                     ]
                 }
        """

        payload = {
            'apikey': API_KEY,
            'cmd': 'get_plays_by_date',
            'time_range': time_range,           # (str)
            'y_axis': y_axis,                   # (str)
            'user_id': user_id,                 # (str)
            'grouping': grouping                # (bin)
        }

        y_axis_list = ['plays', 'duration']

        # Check keyword arguments
        utils.check_str_kw(payload, time_range, is_required=False)
        utils.check_str_kw(payload, y_axis, y_axis_list, is_required=False)
        utils.check_str_kw(payload, user_id, is_required=False)
        utils.check_bin_kw(payload, grouping, is_required=False)

        # Send/receive request
        utils.send_receive_request(self._base_url, params_dict=payload)

    def get_plays_by_dayofweek(self, time_range=None, y_axis=None,
                               user_id=None, grouping=None):
        """
        Get graph data by day of the week.

        Required parameters:
            None

        Optional parameters:
            time_range (str):       The number of days of data to return
            y_axis (str):           "plays" or "duration"
            user_id (str):          The user id to filter the data
            grouping (int):         0 or 1

        Returns:
            json:
                {"categories":
                    ["Sunday", "Monday", "Tuesday", ..., "Saturday"]
                 "series":
                    [{"name": "Movies", "data": [...]}
                     {"name": "TV", "data": [...]},
                     {"name": "Music", "data": [...]}
                     ]
                 }
        """

        payload = {
            'apikey': API_KEY,
            'cmd': 'get_plays_by_dayofweek',
            'time_range': time_range,               # (str)
            'y_axis': y_axis,                       # (str)
            'user_id': user_id,                     # (str)
            'grouping': grouping                    # (bin)
        }

        y_axis_list = ['plays', 'duration']

        # Check keyword arguments
        utils.check_str_kw(payload, time_range, is_required=False)
        utils.check_str_kw(payload, y_axis, y_axis_list, is_required=False)
        utils.check_str_kw(payload, user_id, is_required=False)
        utils.check_bin_kw(payload, grouping, is_required=False)

        # Send/receive request
        utils.send_receive_request(self._base_url, params_dict=payload)

    def get_plays_by_hourofday(self, time_range=None, y_axis=None,
                               user_id=None, grouping=None):
        """
        Get graph data by hour of the day.

        Required parameters:
            None

        Optional parameters:
            time_range (str):       The number of days of data to return
            y_axis (str):           "plays" or "duration"
            user_id (str):          The user id to filter the data
            grouping (int):         0 or 1

        Returns:
            json:
                {"categories":
                    ["00", "01", "02", ..., "23"]
                 "series":
                    [{"name": "Movies", "data": [...]}
                     {"name": "TV", "data": [...]},
                     {"name": "Music", "data": [...]}
                     ]
                 }
        """

        payload = {
            'apikey': API_KEY,
            'cmd': 'get_plays_by_hourofday',
            'time_range': time_range,           # (str)
            'y_axis': y_axis,                   # (str)
            'user_id': user_id,                 # (str)
            'grouping': grouping                # (bin)
        }

        y_axis_list = ['plays', 'duration']

        # Check keyword arguments
        utils.check_str_kw(payload, time_range, is_required=False)
        utils.check_str_kw(payload, y_axis, y_axis_list, is_required=False)
        utils.check_str_kw(payload, user_id, is_required=False)
        utils.check_bin_kw(payload, grouping, is_required=False)

        # Send/receive request
        utils.send_receive_request(self._base_url, params_dict=payload)

    def get_plays_by_source_resolution(self, time_range=None, y_axis=None,
                                       user_id=None, grouping=None):
        """
        Get graph data by source resolution.

        Required parameters:
            None

        Optional parameters:
            time_range (str):       The number of days of data to return
            y_axis (str):           "plays" or "duration"
            user_id (str):          The user id to filter the data
            grouping (int):         0 or 1

        Returns:
            json:
                {"categories":
                    ["720", "1080", "sd", ...]
                 "series":
                    [{"name": "Direct Play", "data": [...]}
                     {"name": "Direct Stream", "data": [...]},
                     {"name": "Transcode", "data": [...]}
                     ]
                 }
        """
        payload = {
            'apikey': API_KEY,
            'cmd': 'get_plays_by_source_resolution',
            'time_range': time_range,           # (str)
            'y_axis': y_axis,                   # (str)
            'user_id': user_id,                 # (str)
            'grouping': grouping                # (bin)
        }

        y_axis_list = ['plays', 'duration']

        # Check keyword arguments
        utils.check_str_kw(payload, time_range, is_required=False)
        utils.check_str_kw(payload, y_axis, y_axis_list, is_required=False)
        utils.check_str_kw(payload, user_id, is_required=False)
        utils.check_bin_kw(payload, grouping, is_required=False)

        # Send/receive request
        utils.send_receive_request(self._base_url, params_dict=payload)

    def get_plays_by_stream_resolution(self, time_range=None, y_axis=None,
                                       user_id=None, grouping=None):
        """
        Get graph data by stream resolution.

        Required parameters:
            None

        Optional parameters:
            time_range (str):       The number of days of data to return
            y_axis (str):           "plays" or "duration"
            user_id (str):          The user id to filter the data
            grouping (int):         0 or 1

        Returns:
            json:
                {"categories":
                    ["720", "1080", "sd", ...]
                 "series":
                    [{"name": "Direct Play", "data": [...]}
                     {"name": "Direct Stream", "data": [...]},
                     {"name": "Transcode", "data": [...]}
                     ]
                 }
        """

        payload = {
            'apikey': API_KEY,
            'cmd': 'get_plays_by_stream_resolution',
            'time_range': time_range,  # (str)
            'y_axis': y_axis,  # (str)
            'user_id': user_id,  # (str)
            'grouping': grouping  # (bin)
        }

        y_axis_list = ['plays', 'duration']

        # Check keyword arguments
        utils.check_str_kw(payload, time_range, is_required=False)
        utils.check_str_kw(payload, y_axis, y_axis_list, is_required=False)
        utils.check_str_kw(payload, user_id, is_required=False)
        utils.check_bin_kw(payload, grouping, is_required=False)

        # Send/receive request
        utils.send_receive_request(self._base_url, params_dict=payload)

    def get_plays_by_stream_type(self, time_range=None, y_axis=None,
                                 user_id=None, grouping=None):
        """
        Get graph data by stream type by date.

        Required parameters:
            None

        Optional parameters:
            time_range (str):       The number of days of data to return
            y_axis (str):           "plays" or "duration"
            user_id (str):          The user id to filter the data
            grouping (int):         0 or 1

        Returns:
            json:
                {"categories":
                    ["YYYY-MM-DD", "YYYY-MM-DD", ...]
                 "series":
                    [{"name": "Direct Play", "data": [...]}
                     {"name": "Direct Stream", "data": [...]},
                     {"name": "Transcode", "data": [...]}
                     ]
                 }
        """

        payload = {
            'apikey': API_KEY,
            'cmd': 'get_plays_by_stream_type',
            'time_range': time_range,  # (str)
            'y_axis': y_axis,  # (str)
            'user_id': user_id,  # (str)
            'grouping': grouping  # (bin)
        }

        y_axis_list = ['plays', 'duration']

        # Check keyword arguments
        utils.check_str_kw(payload, time_range, is_required=False)
        utils.check_str_kw(payload, y_axis, y_axis_list, is_required=False)
        utils.check_str_kw(payload, user_id, is_required=False)
        utils.check_bin_kw(payload, grouping, is_required=False)

        # Send/receive request
        utils.send_receive_request(self._base_url, params_dict=payload)

    def get_plays_by_top_10_platforms(self, time_range=None, y_axis=None,
                                      user_id=None, grouping=None):
        """
        Get graph data by top 10 platforms.

        Required parameters:
            None

        Optional parameters:
            time_range (str):       The number of days of data to return
            y_axis (str):           "plays" or "duration"
            user_id (str):          The user id to filter the data
            grouping (int):         0 or 1

        Returns:
            json:
                {"categories":
                    ["iOS", "Android", "Chrome", ...]
                 "series":
                    [{"name": "Movies", "data": [...]}
                     {"name": "TV", "data": [...]},
                     {"name": "Music", "data": [...]}
                     ]
                 }
        """

        payload = {
            'apikey': API_KEY,
            'cmd': 'get_plays_by_top_10_platforms',
            'time_range': time_range,  # (str)
            'y_axis': y_axis,  # (str)
            'user_id': user_id,  # (str)
            'grouping': grouping  # (bin)
        }

        y_axis_list = ['plays', 'duration']

        # Check keyword arguments
        utils.check_str_kw(payload, time_range, is_required=False)
        utils.check_str_kw(payload, y_axis, y_axis_list, is_required=False)
        utils.check_str_kw(payload, user_id, is_required=False)
        utils.check_bin_kw(payload, grouping, is_required=False)

        # Send/receive request
        utils.send_receive_request(self._base_url, params_dict=payload)

    def get_plays_by_top_10_users(self, time_range=None, y_axis=None,
                                  user_id=None, grouping=None):
        """
        Get graph data by top 10 users.

        Required parameters:
            None

        Optional parameters:
            time_range (str):       The number of days of data to return
            y_axis (str):           "plays" or "duration"
            user_id (str):          The user id to filter the data
            grouping (int):         0 or 1

        Returns:
            json:
                {"categories":
                    ["Jon Snow", "DanyKhaleesi69", "A Girl", ...]
                 "series":
                    [{"name": "Movies", "data": [...]}
                     {"name": "TV", "data": [...]},
                     {"name": "Music", "data": [...]}
                     ]
                 }
        """

        payload = {
            'apikey': API_KEY,
            'cmd': 'get_plays_by_top_10_users',
            'time_range': time_range,  # (str)
            'y_axis': y_axis,  # (str)
            'user_id': user_id,  # (str)
            'grouping': grouping  # (bin)
        }

        y_axis_list = ['plays', 'duration']

        # Check keyword arguments
        utils.check_str_kw(payload, time_range, is_required=False)
        utils.check_str_kw(payload, y_axis, y_axis_list, is_required=False)
        utils.check_str_kw(payload, user_id, is_required=False)
        utils.check_bin_kw(payload, grouping, is_required=False)

        # Send/receive request
        utils.send_receive_request(self._base_url, params_dict=payload)

    def get_plays_per_month(self, time_range=None, y_axis=None,
                            user_id=None, grouping=None):
        """
        Get graph data by month.

        Required parameters:
            None

        Optional parameters:
            time_range (str):       The number of months of data to return
            y_axis (str):           "plays" or "duration"
            user_id (str):          The user id to filter the data
            grouping (int):         0 or 1

        Returns:
            json:
                {"categories":
                    ["Jan 2016", "Feb 2016", "Mar 2016", ...]
                 "series":
                    [{"name": "Movies", "data": [...]}
                     {"name": "TV", "data": [...]},
                     {"name": "Music", "data": [...]}
                     ]
                 }
        """

        payload = {
            'apikey': API_KEY,
            'cmd': 'get_plays_per_month',
            'time_range': time_range,           # (str)
            'y_axis': y_axis,                   # (str)
            'user_id': user_id,                 # (str)
            'grouping': grouping                # (bin)
        }

        y_axis_list = ['plays', 'duration']

        # Check keyword arguments
        utils.check_str_kw(payload, time_range, is_required=False)
        utils.check_str_kw(payload, y_axis, y_axis_list, is_required=False)
        utils.check_str_kw(payload, user_id, is_required=False)
        utils.check_bin_kw(payload, grouping, is_required=False)

        # Send/receive request
        utils.send_receive_request(self._base_url, params_dict=payload)

    def get_plex_log(self, window=None, log_type=None):
        """
        Get the PMS logs.

        Required parameters:
            None

        Optional parameters:
            window (int):           The number of tail lines to return
            log_type (str):         "server" or "scanner"

        Returns:
            json:
                [["May 08, 2016 09:35:37",
                  "DEBUG",
                  "Auth: Came in with a super-token, authorization succeeded."
                  ],
                 [...],
                 [...]
                 ]
        """

        payload = {
            'apikey': API_KEY,
            'cmd': 'get_plex_log',
            'window': window,           # (int)
            'log_type': log_type        # (str)
        }

        log_type_list = ['server', 'scanner']

        # Check keyword arguments
        utils.check_pos_int_kw(payload, window, is_required=False)
        utils.check_str_kw(payload, log_type, log_type_list, is_required=False)

        # Send/receive request
        utils.send_receive_request(self._base_url, params_dict=payload)

    def get_pms_token(self, username=None, password=None):
        """
        Get the user's Plex token used for Tautulli.

        Required parameters:
            username (str):     The Plex.tv username
            password (str):     The Plex.tv password

        Optional parameters:
            None

        Returns:
            string:             The Plex token used for Tautulli
        """

        payload = {
            'apikey': API_KEY,
            'cmd': 'get_pms_token',
            'username': username,           # (str)
            'password': password            # (str)
        }

        # Check keyword arguments
        utils.check_str_kw(payload, username, is_required=True)
        utils.check_str_kw(payload, password, is_required=True)

        # Send/receive request
        utils.send_receive_request(self._base_url, params_dict=payload)

    def get_pms_update(self):
        """
        Check for updates to the Plex Media Server.

        Required parameters:
            None

        Optional parameters:
            None

        Returns:
            json:
                {"update_available": true,
                 "platform": "Windows",
                 "release_date": "1473721409",
                 "version": "1.1.4.2757-24ffd60",
                 "requirements": "...",
                 "extra_info": "...",
                 "changelog_added": "...",
                 "changelog_fixed": "...",
                 "label": "Download",
                 "distro": "english",
                 "distro_build": "windows-i386",
                 "download_url": "https://downloads.plex.tv/...",
                 }
        """

        payload = {
            'apikey': API_KEY,
            'cmd': 'get_pms_update'
        }

        # Send/receive request
        utils.send_receive_request(self._base_url, params_dict=payload)
        
    def get_recently_added(self, count=25, start=None, media_type=None,
                           section_id=None):
        """
        Get all items that where recently added to plex.

        Required parameters:
            count (int):        Number of items to return (default=25)

        Optional parameters:
            start (int):        The item number to start at
            media_type (str):   The media type:
                                "movie", "show", "artist"
            section_id (int):   The id of the Plex library section

        Returns:
            json:
                {"recently_added":
                    [{"added_at": "1461572396",
                      "grandparent_rating_key": "1219",
                      "grandparent_thumb":
                          "/library/metadata/1219/thumb/1462175063",
                      "grandparent_title": "Game of Thrones",
                      "library_name": "",
                      "media_index": "1",
                      "media_type": "episode",
                      "original_title": "",
                      "parent_media_index": "6",
                      "parent_rating_key": "153036",
                      "parent_thumb":
                          "/library/metadata/153036/thumb/1462175062",
                      "parent_title": "",
                      "rating_key": "153037",
                      "section_id": "2",
                      "thumb": "/library/metadata/153037/thumb/1462175060",
                      "title": "The Red Woman",
                      "year": "2016"
                      },
                     {...},
                     {...}
                     ]
                 }
        """

        payload = {
            'apikey': API_KEY,
            'cmd': 'get_recently_added',
            'count': count,             # (int)
            'start': start,             # (int)
            'type': media_type,         # (str)
            'section_id': section_id    # (int)
        }

        media_type_list = ["movie", "show", "artist"]

        # Check keyword arguments
        utils.check_pos_int_kw(payload, count, is_required=True)
        utils.check_pos_int_kw(payload, start, is_required=False)
        utils.check_str_kw(payload, media_type, media_type_list,
                           is_required=False)
        utils.check_pos_int_kw(payload, section_id, is_required=False)

        # Send/receive request
        utils.send_receive_request(self._base_url, params_dict=payload)

    def get_server_friendly_name(self):
        """
        Get the name of the PMS.

        Required parameters:
            None

        Optional parameters:
            None

        Returns:
            string:     "Winterfell-Server"
        """

        payload = {
            'apikey': API_KEY,
            'cmd': 'get_server_friendly_name'
        }

        # Send/receive request
        utils.send_receive_request(self._base_url, params_dict=payload)

    def get_server_id(self, hostname='localhost', port=32400, ssl=None,
                      remote=None):
        """
        Get the PMS server identifier.

        Required parameters:
            hostname (str):     'localhost' or '192.160.0.10'
            port (int):         32400

        Optional parameters:
            ssl (int):          0 or 1
            remote (int):       0 or 1

        Returns:
            json:
                {'identifier': '08u2phnlkdshf890bhdlksghnljsahgleikjfg9t'}
        """

        payload = {
            'apikey': API_KEY,
            'cmd': 'get_server_id',
            'hostname': hostname,
            'port': port,
            'ssl': ssl,
            'remote': remote
        }

        # Check keyword arguments
        utils.check_str_kw(payload, hostname, is_required=True)
        utils.check_pos_int_kw(payload, port, is_required=True)
        utils.check_str_kw(payload, ssl, is_required=False)
        utils.check_str_kw(payload, remote, is_required=False)

        # Send/receive request
        utils.send_receive_request(self._base_url, params_dict=payload)

    def get_server_identity(self):
        """
        Get info about the local server.

        Required parameters:
            None

        Optional parameters:
            None

        Returns:
            json:
                [{"machine_identifier": "ds48g4r354a8v9byrrtr697g3g79w",
                  "version": "0.9.15.x.xxx-xxxxxxx"
                  }
                 ]
        """

        payload = {
            'apikey': API_KEY,
            'cmd': 'get_server_identity'
        }

        # Send/receive request
        utils.send_receive_request(self._base_url, params_dict=payload)

    def get_server_list(self):
        """
        Get all your servers that are published to Plex.tv.

        Required parameters:
            None

        Optional parameters:
            None

        Returns:
            json:
                [{"clientIdentifier": "ds48g4r354a8v9byrrtr697g3g79w",
                  "httpsRequired": "0",
                  "ip": "xxx.xxx.xxx.xxx",
                  "label": "Winterfell-Server",
                  "local": "1",
                  "port": "32400",
                  "value": "xxx.xxx.xxx.xxx"
                  },
                 {...},
                 {...}
                 ]
        """

        payload = {
            'apikey': API_KEY,
            'cmd': 'get_server_list'
        }

        # Send/receive request
        utils.send_receive_request(self._base_url, params_dict=payload)

    def get_server_pref(self, pref=None):
        """
        Get a specified PMS server preference.

        Required parameters:
            pref (str):         Name of preference

        Returns:
            string:             Value of preference
        """

        payload = {
            'apikey': API_KEY,
            'cmd': 'get_server_pref',
            'pref': pref                    # (str)
        }

        # Check keyword arguments
        utils.check_str_kw(payload, pref, is_required=True)

        # Send/receive request
        utils.send_receive_request(self._base_url, params_dict=payload)

    def get_servers_info(self):
        """
        Get info about the PMS.

        Required parameters:
            None

        Optional parameters:
            None

        Returns:
            json:
                [{"port": "32400",
                  "host": "10.0.0.97",
                  "version": "0.9.15.2.1663-7efd046",
                  "name": "Winterfell-Server",
                  "machine_identifier": "ds48g4r354a8v9byrrtr697g3g79w"
                  }
                 ]
        """

        payload = {
            'apikey': API_KEY,
            'cmd': 'get_servers_info'
        }

        # Send/receive request
        utils.send_receive_request(self._base_url, params_dict=payload)

    def get_settings(self, key=None):
        """
        Gets all settings from the config file.

        Required parameters:
            None

        Optional parameters:
            key (str):      Name of a config section to return

        Returns:
            json:
                {"General": {"api_enabled": true, ...}
                 "Advanced": {"cache_sizemb": "32", ...},
                 ...
                 }
        """

        payload = {
            'apikey': API_KEY,
            'cmd': 'get_settings',
            'key': key                  # (str)
        }

        # Check keyword arguments
        utils.check_str_kw(payload, key, is_required=False)

        # Send/receive request
        utils.send_receive_request(self._base_url, params_dict=payload)

    def get_stream_data(self, row_id=None, session_key=None):
        """
        Get the stream details from history or current stream.

        Required parameters:
            row_id (int):       The row ID number for the history item, OR
            session_key (int):  The session key of the current stream

        Optional parameters:
            None

        Returns:
            json:
                {"aspect_ratio": "2.35",
                 "audio_bitrate": 231,
                 "audio_channels": 6,
                 "audio_codec": "aac",
                 "audio_decision": "transcode",
                 "bitrate": 2731,
                 "container": "mp4",
                 "current_session": "",
                 "grandparent_title": "",
                 "media_type": "movie",
                 "optimized_version": "",
                 "optimized_version_profile": "",
                 "optimized_version_title": "",
                 "original_title": "",
                 "pre_tautulli": "",
                 "quality_profile": "1.5 Mbps 480p",
                 "stream_audio_bitrate": 203,
                 "stream_audio_channels": 2,
                 "stream_audio_codec": "aac",
                 "stream_audio_decision": "transcode",
                 "stream_bitrate": 730,
                 "stream_container": "mkv",
                 "stream_container_decision": "transcode",
                 "stream_subtitle_codec": "",
                 "stream_subtitle_decision": "",
                 "stream_video_bitrate": 527,
                 "stream_video_codec": "h264",
                 "stream_video_decision": "transcode",
                 "stream_video_framerate": "24p",
                 "stream_video_height": 306,
                 "stream_video_resolution": "SD",
                 "stream_video_width": 720,
                 "subtitle_codec": "",
                 "subtitles": "",
                 "synced_version": "",
                 "synced_version_profile": "",
                 "title": "Frozen",
                 "transcode_hw_decoding": "",
                 "transcode_hw_encoding": "",
                 "video_bitrate": 2500,
                 "video_codec": "h264",
                 "video_decision": "transcode",
                 "video_framerate": "24p",
                 "video_height": 816,
                 "video_resolution": "1080",
                 "video_width": 1920
                 }
        """

        payload = {
            'apikey': API_KEY,
            'cmd': 'get_stream_data',
            'row_id': row_id,           # (int)
            'session_key': session_key  # (int)
        }

        # Check for ONLY one required arguments
        if row_id and session_key is None:
            raise ValueError(
                'Either "row_id" OR "session_key" is required'
            )
        elif row_id and session_key is not None:
            raise ValueError(
                'Only ONE required argument ("row_id" OR "session_key") '
                'is required'
            )
        elif row_id is not None:
            utils.check_pos_int_kw(payload, row_id)
        elif session_key is not None:
            utils.check_pos_int_kw(payload, session_key)

        # Send/receive request
        utils.send_receive_request(self._base_url, params_dict=payload)

    def get_stream_type_by_top_10_platforms(self, time_range=None,
                                            y_axis=None, user_id=None,
                                            grouping=None):
        """
        Get graph data by stream type by top 10 platforms.

        Required parameters:
            None

        Optional parameters:
            time_range (str):       The number of days of data to return
            y_axis (str):           "plays" or "duration"
            user_id (str):          The user id to filter the data
            grouping (int):         0 or 1

        Returns:
            json:
                {"categories":
                    ["iOS", "Android", "Chrome", ...]
                 "series":
                    [{"name": "Direct Play", "data": [...]}
                     {"name": "Direct Stream", "data": [...]},
                     {"name": "Transcode", "data": [...]}
                     ]
                 }
        """

        payload = {
            'apikey': API_KEY,
            'cmd': 'get_stream_type_by_top_10_platforms',
            'time_range': time_range,  # (str)
            'y_axis': y_axis,  # (str)
            'user_id': user_id,  # (str)
            'grouping': grouping  # (bin)
        }

        y_axis_list = ['plays', 'duration']

        # Check keyword arguments
        utils.check_str_kw(payload, time_range, is_required=False)
        utils.check_str_kw(payload, y_axis, y_axis_list, is_required=False)
        utils.check_str_kw(payload, user_id, is_required=False)
        utils.check_bin_kw(payload, grouping, is_required=False)

        # Send/receive request
        utils.send_receive_request(self._base_url, params_dict=payload)

    def get_stream_type_by_top_10_users(self, time_range=None, y_axis=None,
                                        user_id=None, grouping=None):
        """
        Get graph data by stream type by top 10 users.

        Required parameters:
            None

        Optional parameters:
            time_range (str):       The number of days of data to return
            y_axis (str):           "plays" or "duration"
            user_id (str):          The user id to filter the data
            grouping (int):         0 or 1

        Returns:
            json:
                {"categories":
                    ["Jon Snow", "DanyKhaleesi69", "A Girl", ...]
                 "series":
                    [{"name": "Direct Play", "data": [...]}
                     {"name": "Direct Stream", "data": [...]},
                     {"name": "Transcode", "data": [...]}
                    ]
                 }
        """

        payload = {
            'apikey': API_KEY,
            'cmd': 'get_stream_type_by_top_10_users',
            'time_range': time_range,  # (str)
            'y_axis': y_axis,  # (str)
            'user_id': user_id,  # (str)
            'grouping': grouping  # (bin)
        }

        y_axis_list = ['plays', 'duration']

        # Check keyword arguments
        utils.check_str_kw(payload, time_range, is_required=False)
        utils.check_str_kw(payload, y_axis, y_axis_list, is_required=False)
        utils.check_str_kw(payload, user_id, is_required=False)
        utils.check_bin_kw(payload, grouping, is_required=False)

        # Send/receive request
        utils.send_receive_request(self._base_url, params_dict=payload)

    def get_synced_items(self, machine_id=None, user_id=None):
        """
        Get a list of synced items on the PMS.
        
        Required parameters:
            machine_id (str):       The PMS identifier
        
        Optional parameters:
            user_id (str):          The id of the Plex user
        
        Returns:
            json:
                [{"audio_bitrate": "192",
                  "client_id": "95434se643fsf24f-com-plexapp-android",
                  "content_type": "video",
                  "device_name": "Tyrion's iPad",
                  "failure": "",
                  "item_complete_count": "1",
                  "item_count": "1",
                  "item_downloaded_count": "1",
                  "item_downloaded_percent_complete": 100,
                  "metadata_type": "movie",
                  "photo_quality": "74",
                  "platform": "iOS",
                  "rating_key": "154092",
                  "root_title": "Movies",
                  "state": "complete",
                  "sync_id": "11617019",
                  "sync_title": "Deadpool",
                  "total_size": "560718134",
                  "user": "DrukenDwarfMan",
                  "user_id": "696969",
                  "username": "DrukenDwarfMan",
                  "video_bitrate": "4000"
                  "video_quality": "100"
                  },
                 {...},
                 {...}
                 ]
        """

        payload = {
            'apikey': API_KEY,
            'cmd': 'get_synced_items',
            'machine_id': machine_id,
            'user_id': user_id
        }

        # Check keyword arguments
        utils.check_str_kw(payload, machine_id, is_required=True)
        utils.check_str_kw(payload, user_id, is_required=False)

        # Send/receive request
        utils.send_receive_request(self._base_url, params_dict=payload)
    
    def get_user(self, user_id=None):
        """
        Get a user's details.
        
        Required parameters:
            user_id (str):          The id of the Plex user
        
        Optional parameters:
            None
        
        Returns:
            json:
                {"allow_guest": 1,
                 "deleted_user": 0,
                 "do_notify": 1,
                 "email": "Jon.Snow.1337@CastleBlack.com",
                 "friendly_name": "Jon Snow",
                 "is_allow_sync": 1,
                 "is_home_user": 1,
                 "is_restricted": 0,
                 "keep_history": 1,
                 "shared_libraries": ["10", "1", "4", "5", "15", "20", "2"],
                 "user_id": 133788,
                 "user_thumb": "https://plex.tv/users/k10w42309cynaopq/avatar",
                 "username": "LordCommanderSnow"
                 }
        """

        payload = {
            'apikey': API_KEY,
            'cmd': 'get_user',
            'user_id': user_id              # (str)
        }

        # Check keyword arguments
        utils.check_str_kw(payload, user_id, is_required=True)

        # Send/receive request
        utils.send_receive_request(self._base_url, params_dict=payload)

    def get_user_ips(self, user_id=None, order_column=None, order_dir=None,
                     start=None, length=None, search=None):
        """
        Get the data on Tautulli users IP table.
        
        Required parameters:
            user_id (str):                  The id of the Plex user
        
        Optional parameters:
            order_column (str):             "last_seen", "ip_address", 
                                            "platform", "player",
                                            "last_played", "play_count"
            order_dir (str):                "desc" or "asc"
            start (int):                    Row to start from, 0
            length (int):                   Number of items to return, 25
            search (str):                   A string to search for, 
                                            "xxx.xxx.xxx.xxx"
        
        Returns:
            json:
                {"draw": 1,
                 "recordsTotal": 2344,
                 "recordsFiltered": 10,
                 "data":
                    [{"friendly_name": "Jon Snow",
                      "id": 1121,
                      "ip_address": "xxx.xxx.xxx.xxx",
                      "last_played": "Game of Thrones - The Red Woman",
                      "last_seen": 1462591869,
                      "media_index": 1,
                      "media_type": "episode",
                      "parent_media_index": 6,
                      "parent_title": "",
                      "platform": "Chrome",
                      "play_count": 149,
                      "player": "Plex Web (Chrome)",
                      "rating_key": 153037,
                      "thumb": "/library/metadata/153036/thumb/1462175062",
                      "transcode_decision": "transcode",
                      "user_id": 133788,
                      "year": 2016
                      },
                     {...},
                     {...}
                     ]
                 }
        """

        payload = {
            'apikey': API_KEY,
            'cmd': 'get_user_ips',
            'user_id': user_id,                 # (str) (req)
            'order_column': order_column,       # (str)
            'order_dir': order_dir,             # (str)
            'start': start,                     # (int)
            'length': length,                   # (int)
            'search': search                    # (str)
        }

        order_column_list = ["last_seen", "ip_address", "platform", "player", 
                             "last_played", "play_count"]
        order_dir_list = ["desc", "asc"]

        # Check keyword arguments
        utils.check_str_kw(payload, user_id, is_required=True)
        utils.check_str_kw(payload, order_column, order_column_list,
                           is_required=False)
        utils.check_str_kw(payload, order_dir, order_dir_list,
                           is_required=False)
        utils.check_pos_int_kw(payload, start, is_required=False)
        utils.check_pos_int_kw(payload, length, is_required=False)
        utils.check_str_kw(payload, search, is_required=False)

        # Send/receive request
        utils.send_receive_request(self._base_url, params_dict=payload)

    def get_user_logins(self, user_id=None, order_column=None,
                        order_dir=None, start=None, length=None, search=None):
        """
        Get the data on Tautulli user login table.

        Required parameters:
            user_id (str):                  The id of the Plex user

        Optional parameters:
            order_column (str):             "date", "time", "ip_address",
                                            "host", "os", "browser"
            order_dir (str):                "desc" or "asc"
            start (int):                    Row to start from, 0
            length (int):                   Number of items to return, 25
            search (str):                   A string to search for,
                                            "xxx.xxx.xxx.xxx"

        Returns:
            json:
                {"draw": 1,
                 "recordsTotal": 2344,
                 "recordsFiltered": 10,
                 "data":
                    [{"browser": "Safari 7.0.3",
                      "friendly_name": "Jon Snow",
                      "host": "http://plexpy.castleblack.com",
                      "ip_address": "xxx.xxx.xxx.xxx",
                      "os": "Mac OS X",
                      "timestamp": 1462591869,
                      "user": "LordCommanderSnow",
                      "user_agent": "Mozilla/5.0 (Macintosh;
                                    Intel Mac OS X 10_9_3)
                                    AppleWebKit/537.75.14 (KHTML, like Gecko)
                                    Version/7.0.3 Safari/7046A194A",
                      "user_group": "guest",
                      "user_id": 133788
                      },
                     {...},
                     {...}
                     ]
                 }
        """

        payload = {
            'apikey': API_KEY,
            'cmd': 'get_user_logins',
            'user_id': user_id,  # (str) (req)
            'order_column': order_column,  # (str)
            'order_dir': order_dir,  # (str)
            'start': start,  # (int)
            'length': length,  # (int)
            'search': search  # (str)
        }

        order_column_list = ["date", "time", "ip_address", "host",
                             "os", "browser"]
        order_dir_list = ["desc", "asc"]

        # Check keyword arguments
        utils.check_str_kw(payload, user_id, is_required=True)
        utils.check_str_kw(payload, order_column, order_column_list,
                           is_required=False)
        utils.check_str_kw(payload, order_dir, order_dir_list,
                           is_required=False)
        utils.check_pos_int_kw(payload, start, is_required=False)
        utils.check_pos_int_kw(payload, length, is_required=False)
        utils.check_str_kw(payload, search, is_required=False)

        # Send/receive request
        utils.send_receive_request(self._base_url, params_dict=payload)

    def get_user_names(self):
        """
        Get a list of all user and user ids.

        Required parameters:
            None

        Optional parameters:
            None

        Returns:
            json:
                [{"friendly_name": "Jon Snow", "user_id": 133788},
                 {"friendly_name": "DanyKhaleesi69", "user_id": 8008135},
                 {"friendly_name": "Tyrion Lannister", "user_id": 696969},
                 {...},
                ]
        """

        payload = {
            'apikey': API_KEY,
            'cmd': 'get_user_names'
        }

        # Send/receive request
        utils.send_receive_request(self._base_url, params_dict=payload)

    def get_user_player_stats(self, user_id=None, grouping=None):
        """
        Get a user's player statistics.

        Required parameters:
            user_id (str):          The id of the Plex user

        Optional parameters:
            grouping (int):         0 or 1

        Returns:
            json:
                [{"platform_type": "Chrome",
                  "player_name": "Plex Web (Chrome)",
                  "result_id": 1,
                  "total_plays": 170
                  },
                 {"platform_type": "Chromecast",
                  "player_name": "Chromecast",
                  "result_id": 2,
                  "total_plays": 42
                  },
                 {...},
                 {...}
                 ]
        """

        payload = {
            'apikey': API_KEY,
            'cmd': 'get_user_player_stats',
            'user_id': user_id,             # (str) (req)
            'grouping': grouping            # (bin)
        }

        # Check keyword arguments
        utils.check_str_kw(payload, user_id, is_required=True)
        utils.check_bin_kw(payload, grouping, is_required=False)

        # Send/receive request
        utils.send_receive_request(self._base_url, params_dict=payload)

    def get_user_watch_time_stats(self, user_id=None, grouping=None):
        """
        Get a user's watch time statistics.

        Required parameters:
            user_id (str):          The id of the Plex user

        Optional parameters:
            grouping (int):         0 or 1

        Returns:
            json:
                [{"query_days": 1,
                  "total_plays": 0,
                  "total_time": 0
                  },
                 {"query_days": 7,
                  "total_plays": 3,
                  "total_time": 15694
                  },
                 {"query_days": 30,
                  "total_plays": 35,
                  "total_time": 63054
                  },
                 {"query_days": 0,
                  "total_plays": 508,
                  "total_time": 1183080
                  }
                 ]
        """

        payload = {
            'apikey': API_KEY,
            'cmd': 'get_user_watch_time_stats',
            'user_id': user_id,             # (str) (req)
            'grouping': grouping            # (bin)
        }

        # Check keyword arguments
        utils.check_str_kw(payload, user_id, is_required=True)
        utils.check_bin_kw(payload, grouping, is_required=False)

        # Send/receive request
        utils.send_receive_request(self._base_url, params_dict=payload)

    def get_users(self):
        """
        Get a list of all users that have access to your server.

        Required parameters:
            None

        Optional parameters:
            None

        Returns:
            json:
                [{"allow_guest": 1,
                  "do_notify": 1,
                  "email": "Jon.Snow.1337@CastleBlack.com",
                  "filter_all": "",
                  "filter_movies": "",
                  "filter_music": "",
                  "filter_photos": "",
                  "filter_tv": "",
                  "is_admin": 0,
                  "is_allow_sync": 1,
                  "is_home_user": 1,
                  "is_restricted": 0,
                  "keep_history": 1,
                  "server_token": "PU9cMuQZxJKFBtGqHk68",
                  "shared_libraries": "1;2;3",
                  "thumb": "https://plex.tv/users/k10w42309cynaopq/avatar",
                  "user_id": "133788",
                  "username": "Jon Snow"
                  },
                 {...},
                 {...}
                 ]
        """

        payload = {
            'apikey': API_KEY,
            'cmd': 'get_users'
        }

        # Send/receive request
        utils.send_receive_request(self._base_url, params_dict=payload)

    def get_users_table(self, order_column=None, order_dir=None, start=None, 
                        length=None, search=None):
        """
        Get the data on Tautulli users table.

        Required parameters:
            None

        Optional parameters:
            order_column (str):             "user_thumb", "friendly_name",
                                            "last_seen", "ip_address",
                                            "platform", "player", 
                                            "last_played", "plays",
                                            "duration"
            order_dir (str):                "desc" or "asc"
            start (int):                    Row to start from, 0
            length (int):                   Number of items to return, 25
            search (str):                   A string to search for, "Jon Snow"

        Returns:
            json:
                {"draw": 1,
                 "recordsTotal": 10,
                 "recordsFiltered": 10,
                 "data":
                    [{"allow_guest": "Checked",
                      "do_notify": "Checked",
                      "duration": 2998290,
                      "friendly_name": "Jon Snow",
                      "id": 1121,
                      "ip_address": "xxx.xxx.xxx.xxx",
                      "keep_history": "Checked",
                      "last_played": "Game of Thrones - The Red Woman",
                      "last_seen": 1462591869,
                      "media_index": 1,
                      "media_type": "episode",
                      "parent_media_index": 6,
                      "parent_title": "",
                      "platform": "Chrome",
                      "player": "Plex Web (Chrome)",
                      "plays": 487,
                      "rating_key": 153037,
                      "thumb": "/library/metadata/153036/thumb/1462175062",
                      "transcode_decision": "transcode",
                      "user_id": 133788,
                      "user_thumb":
                          "https://plex.tv/users/568gwwoib5t98a3a/avatar",
                      "year": 2016
                      },
                     {...},
                     {...}
                     ]
                 }
        """

        payload = {
            'apikey': API_KEY,
            'cmd': 'get_user_logins',
            'order_column': order_column,   # (str)
            'order_dir': order_dir,         # (str)
            'start': start,                 # (int)
            'length': length,               # (int)
            'search': search                # (str)
        }

        order_column_list = ["user_thumb", "friendly_name", "last_seen", 
                             "ip_address", "platform", "player",
                             "last_played", "plays", "duration"]
        order_dir_list = ["desc", "asc"]

        # Check keyword arguments
        utils.check_str_kw(payload, order_column, order_column_list,
                           is_required=False)
        utils.check_str_kw(payload, order_dir, order_dir_list,
                           is_required=False)
        utils.check_pos_int_kw(payload, start, is_required=False)
        utils.check_pos_int_kw(payload, length, is_required=False)
        utils.check_str_kw(payload, search, is_required=False)

        # Send/receive request
        utils.send_receive_request(self._base_url, params_dict=payload)
        
    def get_whois_lookup(self, ip_address=None):
        """
        Get the connection info for an IP address.

        Required parameters:
            ip_address (str):               IP address of connection for 
                                            whois lookup
        
        Optional parameters:
            None
        
        Returns:
            json:
                {"host": "google-public-dns-a.google.com",
                 "nets": [{"description": "Google Inc.",
                           "address": "1600 Amphitheatre Parkway",
                           "city": "Mountain View",
                           "state": "CA",
                           "postal_code": "94043",
                           "country": "United States",
                           ...
                           },
                           {...}
                          ]
            json:
                {"host": "Not available",
                 "nets": [],
                 "error": "IPv4 address 127.0.0.1 is already defined as 
                          Loopback via RFC 1122, Section 3.2.1.3."
        """

        payload = {
            'apikey': API_KEY,
            'cmd': 'get_whois_lookup',
            'ip_address': ip_address            # (str) (req)
        }

        # Check keyword arguments
        utils.check_str_kw(payload, ip_address, is_required=True)

        # Send/receive request
        utils.send_receive_request(self._base_url, params_dict=payload)
    
    def import_database(self, app=None, database_path=None, table_name=None, 
                        import_ignore_interval=None):
        """
        Import a PlexWatch or Plexivity database into Tautulli.

        Required parameters:
            app (str):                      "plexwatch" or "plexivity"
            database_path (str):            The full path to the plexwatch 
                                            database file
            table_name (str):               "processed" or "grouped"
        
        Optional parameters:
            import_ignore_interval (int):   The minimum number of seconds 
                                            for a stream to import
        
        Returns:
            None
        """

        payload = {
            'apikey': API_KEY,
            'cmd': 'import_database',
            'app': app,                                         # (str) (req)
            'database_path': database_path,                     # (str) (req)
            'table_name': table_name,                           # (str) (req)
            'import_ignore_interval': import_ignore_interval    # (int)
        }
        
        app_list = ['plexwatch', 'plexivity']
        table_name_list = ['processed', 'grouped']

        # Check keyword arguments
        utils.check_str_kw(payload, app, app_list, is_required=True)
        utils.check_str_kw(payload, database_path, is_required=True)
        utils.check_str_kw(payload, table_name, table_name_list, 
                           is_required=True)
        utils.check_pos_int_kw(payload, import_ignore_interval, 
                               is_required=False)

        # Send/receive request
        utils.send_receive_request(self._base_url, params_dict=payload)
    
    def install_geoip_db(self):
        """
        Downloads and installs the GeoLite2 database
        """

        payload = {
            'apikey': API_KEY,
            'cmd': 'install_geoip_db'
        }

        # Send/receive request
        utils.send_receive_request(self._base_url, params_dict=payload)
    
    def notify(self, notifier_id=None, subject=None, body=None, 
               script_args=None):
        """
        Send a notification using Tautulli.

        Required parameters:
            notifier_id (int):      The ID number of the notification agent
            subject (str):          The subject of the message
            body (str):             The body of the message
        
        Optional parameters:
            script_args (str):      The arguments for script notifications
        
        Returns:
            None
        """

        payload = {
            'apikey': API_KEY,
            'cmd': 'notify',
            'notifier_id': notifier_id,         # (int) (req)
            'subject': subject,                 # (str) (req)
            'body': body,                       # (str) (req)
            'script_args': script_args          # (str)
        }

        # Check keyword arguments
        utils.check_pos_int_kw(payload, notifier_id, is_required=True)
        utils.check_str_kw(payload, subject, is_required=True)
        utils.check_str_kw(payload, body, is_required=True)
        utils.check_str_kw(payload, script_args, is_required=False)

        # Send/receive request
        utils.send_receive_request(self._base_url, params_dict=payload)
    
    def notify_newsletter(self, newsletter_id=None, subject=None, body=None, 
                          message=None):
        """
        Send a newsletter using Tautulli.
        
        Required parameters:
            newsletter_id (int):    The ID number of the newsletter agent
        
        Optional parameters:
            subject (str):          The subject of the newsletter
            body (str):             The body of the newsletter
            message (str):          The message of the newsletter
        
        Returns:
            None
        """

        payload = {
            'apikey': API_KEY,
            'cmd': 'notify_newsletter',
            'newsletter_id': newsletter_id,     # (int) (req)
            'subject': subject,                 # (str)
            'body': body,                       # (str)
            'message': message                  # (str)
        }

        # Check keyword arguments
        utils.check_pos_int_kw(payload, newsletter_id, is_required=True)
        utils.check_str_kw(payload, subject, is_required=False)
        utils.check_str_kw(payload, body, is_required=False)
        utils.check_str_kw(payload, message, is_required=False)

        # Send/receive request
        utils.send_receive_request(self._base_url, params_dict=payload)
        
    def notify_recently_added(self, rating_key=None, notifier_id=None):
        """
        Send a recently added notification using Tautulli.

        Required parameters:
            rating_key (int):       The rating key for the media

        Optional parameters:
            notifier_id (int):      The ID number of the notification agent.
                                    The notification will send to all enabled
                                    notification agents if notifier id is not
                                    provided.

        Returns:
            json
                {"result": "success",
                 "message": "Notification queued."
                }
        """

        payload = {
            'apikey': API_KEY,
            'cmd': 'notify_recently_added',
            'rating_key': rating_key,               # (int) (req)
            'notifier_id': notifier_id              # (int)
        }

        # Check keyword arguments
        utils.check_pos_int_kw(payload, rating_key, is_required=True)
        utils.check_pos_int_kw(payload, notifier_id, is_required=False)

        # Send/receive request
        utils.send_receive_request(self._base_url, params_dict=payload)

    def pms_image_proxy(self, img=None, rating_key=None, width=None,
                        height=None, opacity=None, background=None,
                        blur=None, img_format=None, fallback=None,
                        refresh=None, return_hash=None):
        """
        Gets an image from the PMS and saves it to the image cache directory.

        Required parameters:
            img (str):              /library/metadata/153037/thumb/1462175060
            or
            rating_key (int):       54321

        Optional parameters:
            width (int):            300
            height (int):           450
            opacity (int):          25
            background (int):       282828
            blur (int):             3
            img_format (str):       png
            fallback (str):         "poster", "cover", "art"
            refresh (bool):         True or False whether to refresh the
                                    image cache
            return_hash (bool):     True or False to return the self-hosted
                                    image hash instead of the image

        Returns:
            None
        """

        payload = {
            'apikey': API_KEY,
            'cmd': 'pms_image_proxy',
            'img': img,                             # (str) (req, bitwise)
            'rating_key': rating_key,               # (int) (req, bitwise)
            'width': width,                         # (int)
            'height': height,                       # (int)
            'opacity': opacity,                     # (int)
            'background': background,               # (int)
            'blur': blur,                           # (int)
            'img_format': img_format,               # (str)
            'fallback': fallback,                   # (str)
            'refresh': refresh,                     # (bool)
            'return_hash': return_hash              # (bool)
        }

        fallback_list = ["poster", "cover", "art"]

        # Check for ONLY one required arguments
        if img and rating_key is None:
            raise ValueError(
                'Either "img" OR "rating_key" is required'
            )
        elif img and rating_key is not None:
            raise ValueError(
                'Only ONE required argument ("img" OR "rating_key") '
                'is required'
            )
        elif img is not None:
            utils.check_str_kw(payload, img)
        elif rating_key is not None:
            utils.check_pos_int_kw(payload, rating_key)

        # Check keyword arguments
        utils.check_pos_int_kw(payload, width, is_required=False)
        utils.check_pos_int_kw(payload, height, is_required=False)
        utils.check_pos_int_kw(payload, opacity, is_required=False)
        utils.check_pos_int_kw(payload, background, is_required=False)
        utils.check_pos_int_kw(payload, blur, is_required=False)
        utils.check_str_kw(payload, img_format, is_required=False)
        utils.check_str_kw(payload, fallback, fallback_list, is_required=False)
        utils.check_bool_kw(payload, refresh, is_required=False)
        utils.check_bool_kw(payload, return_hash, is_required=False)

        # Send/receive request
        utils.send_receive_request(self._base_url, params_dict=payload)

    def refresh_libraries_list(self):
        """
        Refresh the Tautulli libraries list.
        """

        payload = {
            'apikey': API_KEY,
            'cmd': 'refresh_libraries_list'
        }

        # Send/receive request
        utils.send_receive_request(self._base_url, params_dict=payload)

    def refresh_users_list(self):
        """
        Refresh the Tautulli users list.
        """

        payload = {
            'apikey': API_KEY,
            'cmd': 'refresh_users_list'
        }

        # Send/receive request
        utils.send_receive_request(self._base_url, params_dict=payload)

    def register_device(self, device_name=None, device_id=None,
                        friendly_name=None):
        """
        Registers the Tautulli Android App for notifications.

        Required parameters:
            device_name (str):        The device name of the Tautulli
                                      Android App
            device_id (str):          The OneSignal device id of the Tautulli
                                      Android App

        Optional parameters:
            friendly_name (str):      A friendly name to identify the
                                      mobile device

        Returns:
            None
        """

        payload = {
            'apikey': API_KEY,
            'cmd': 'register_device',
            'device_name': device_name,                 # (str)
            'device_id': device_id,                     # (str)
            'friendly_name': friendly_name              # (str)
        }

        # Check keyword arguments
        utils.check_str_kw(payload, device_name, is_required=True)
        utils.check_str_kw(payload, device_id, is_required=True)
        utils.check_str_kw(payload, friendly_name, is_required=False)

        # Send/receive request
        utils.send_receive_request(self._base_url, params_dict=payload)

    def restart(self):
        """
        Restart Tautulli.
        """

        payload = {
            'apikey': API_KEY,
            'cmd': 'restart',
        }

        # Send/receive request
        utils.send_receive_request(self._base_url, params_dict=payload)

    def search(self, query=None, limit=None):
        """
        Get search results from the PMS.

        Required parameters:
            query (str):        The query string to search for

        Optional parameters:
            limit (int):        The maximum number of items to return per
                                media type

        Returns:
            json:
                {"results_count": 69,
                 "results_list":
                    {"movie":
                        [{...},
                         {...},
                         ]
                     },
                    {"episode":
                        [{...},
                         {...},
                         ]
                     },
                    {...}
                 }
        """

        payload = {
            'apikey': API_KEY,
            'cmd': 'search',
            'query': query,                     # (str) (req)
            'limit': limit                      # (int)
        }

        # Check keyword arguments
        utils.check_str_kw(payload, query, is_required=True)
        utils.check_pos_int_kw(payload, limit, is_required=False)

        # Send/receive request
        utils.send_receive_request(self._base_url, params_dict=payload)
