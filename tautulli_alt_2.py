"""
Tautulli base class
"""
from payload import Payload
from validator import Validator
from requester import Requester
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

    def _cmd(self, pprint=False, **params):
        """Sends and receives API command"""
        payload = {'apikey': self.apikey}
        payload.update(Payload(params=params).payload)
        validator = Validator(payload)
        validator.validate()
        requester = Requester(self.url, payload)
        r = requester.get(pprint=pprint)
        return r

    def get_history(self, pprint=False, grouping=None, user=None, user_id=None,
                    rating_key=None, parent_rating_key=None,
                    grandparent_rating_key=None, start_date=None,
                    section_id=None, media_type=None,
                    transcode_decision=None, order_column=None,
                    order_dir=None, start=None, length=None, search=None,
                    out_type=None, callback=None, debug=None):
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

        req = self._cmd(cmd='get_history', pprint=pprint, grouping=grouping,
                        user=user, user_id=user_id, rating_key=rating_key,
                        parent_rating_key=parent_rating_key,
                        grandparent_rating_key=grandparent_rating_key,
                        start_date=start_date, section_id=section_id,
                        media_type=media_type,
                        transcode_decision=transcode_decision,
                        order_column=order_column, order_dir=order_dir,
                        start=start, length=length, search=search,
                        out_type=out_type, callback=callback, debug=debug)
        return req

    def get_activity(self, pprint=False, session_key=None, session_id=None,
                     out_type=None, callback=None, debug=None):
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

        req = self._cmd(cmd='get_activity', pprint=pprint,
                        session_key=session_key, session_id=session_id,
                        out_type=out_type, callback=callback, debug=debug)
        return req
