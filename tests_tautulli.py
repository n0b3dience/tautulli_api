from tautulli import Tautulli
import unittest


class TestGetHistory(unittest.TestCase):
    """
    Test get_history()
    """

    def test_get_history(self):
        tautulli = Tautulli()
        hist_test_1_exp = \
            '{\n' \
            '    "data": {\n' \
            '        "data": [\n' \
            '            {\n' \
            '                "date": 1542905815,\n' \
            '                "duration": 601,\n' \
            '                "friendly_name": "nettles4349",\n' \
            '                "full_title": "Blade Runner 2049",\n' \
            '                "grandparent_rating_key": "",\n' \
            '                "grandparent_title": "",\n' \
            '                "group_count": 1,\n' \
            '                "group_ids": "76",\n' \
            '                "id": 76,\n' \
            '                "ip_address": "192.168.1.9",\n' \
            '                "media_index": "",\n' \
            '                "media_type": "movie",\n' \
            '                "original_title": "",\n' \
            '                "parent_media_index": "",\n' \
            '                "parent_rating_key": "",\n' \
            '                "parent_title": "",\n' \
            '                "paused_counter": 2,\n' \
            '                "percent_complete": 6,\n' \
            '                "platform": "Vivaldi",\n' \
            '                "player": "Vivaldi",\n' \
            '                "rating_key": 4536,\n' \
            '                "reference_id": 76,\n' \
            '                "session_key": null,\n' \
            '                "started": 1542905815,\n' \
            '                "state": null,\n' \
            '                "stopped": 1542906418,\n' \
            '                "thumb": ' \
            '"/library/metadata/4536/thumb/1542104201",\n' \
            '                "title": "",\n' \
            '                "transcode_decision": "transcode",\n' \
            '                "user": "nettles4349",\n' \
            '                "user_id": 7324448,\n' \
            '                "watched_status": 0,\n' \
            '                "year": 2017\n' \
            '            }\n' \
            '        ],\n' \
            '        "draw": 1,\n' \
            '        "filter_duration": "10 mins",\n' \
            '        "recordsFiltered": 1,\n' \
            '        "recordsTotal": 179,\n' \
            '        "total_duration": "10 mins"\n' \
            '    },\n' \
            '    "message": null,\n' \
            '    "result": "success"\n' \
            '}'
        hist_test_1_act = tautulli.get_history(
            length=1, media_type='movie', user='nettles4349'
        )
        self.assertEqual(hist_test_1_act, hist_test_1_exp)


if __name__ == '__main__':
    unittest.main()
