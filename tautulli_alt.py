from payload import Payload


class Tautulli:
    """Tautulli base class"""
    def __init__(self):
        pass

    @staticmethod
    def get_history(grouping=None, user=None,
                    user_id=None, rating_key=None, parent_rating_key=None,
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

        payload = Payload('get_history', out_type=out_type, callback=callback,
                          debug=debug, grouping=grouping, user=user,
                          user_id=user_id, rating_key=rating_key,
                          parent_rating_key=parent_rating_key,
                          grandparent_rating_key=grandparent_rating_key,
                          start_date=start_date, section_id=section_id,
                          media_type=media_type,
                          transcode_decision=transcode_decision,
                          order_column=order_column, order_dir=order_dir,
                          start=start, length=length, search=search)

        result = payload.get_results()
        return result
