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

        # Send request
        response = utils.send_receive_request(
            self._base_url, params_dict=payload
        )
        # Return request
        return response
