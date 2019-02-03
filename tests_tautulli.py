from tautulli import Tautulli
import unittest
import json
from jsonschema import validate, ValidationError, SchemaError


def validate_payload(schema_path, payload_dict):
    try:
        with open(schema_path, 'r') as schema_file:
            schema = json.load(schema_file)
            validate(instance=payload_dict, schema=schema)
    except ValidationError as e:
        print(e.message)
    except SchemaError as e:
        print(e.message)


class TestGetHistory(unittest.TestCase):
    """
    Test get_history()
    """

    def test_get_history(self):
        tautulli = Tautulli()
        hist_test_1_exp = 'Blade Runner 2049'

        resp = tautulli.get_history(
            length=2, media_type='movie', user='nettles4349'
        )
        hist_test_1_act = resp['response']['data']['data'][1]['full_title']

        self.assertEqual(hist_test_1_act, hist_test_1_exp)
    
    def test_get_hist_schema(self):
        payload = {
            "apikey": "WE431DU51235DAQ100T",
            "cmd": "get_history",
            "grouping": None,
            "user": None,
            "user_id": None, 
            "rating_key": None, 
            "parent_rating_key": None,
            "grandparent_rating_key": None, 
            "start_date": None,
            "section_id": None,
            "media_type": None,
            "transcode_decision": None,
            "order_column": None,
            "order_dir": None,
            "start": None,
            "length": None,
            "search": None,
            "out_type": None,
            "callback": None,
            "debug": None
        }
        schema_path = './schemas/get_history.json'
        validate_payload(schema_path, payload)
        print("Check 01 OK")
        payload["user"] = "nettles4349"
        validate_payload(schema_path, payload)
        print("Check 02 OK --- user=\"nettles4349\"")
        payload["grandparent_rating_key"] = 3744
        validate_payload(schema_path, payload)
        print("Check 03 OK --- gp_rtg_ky=3744")
        payload["grandparent_rating_key"] = "3744"
        print("Check 03 OK --- gp_rtg_ky=\"3744\"")


if __name__ == '__main__':
    unittest.main()
