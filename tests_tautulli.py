from tautulli import Tautulli
import os
import unittest
import json
from jsonschema import validate, ValidationError, SchemaError, RefResolver


def validate_payload(schema_json, payload_dict):
    schema_dir = os.path.abspath('schemas')
    try:
        # with open(schema_path, 'r') as schema_file:
        with open(os.path.join(schema_dir, schema_json)) as schema_file:
            schema = json.load(schema_file)
            resolver = RefResolver('file:///{}/'.format(schema_dir), None)
            validate(instance=payload_dict, schema=schema, resolver=resolver)
            schema_file.close()
    except ValidationError as e:
        print('VALIDATION ERROR::: {}'.format(e.message))
    except SchemaError as e:
        print('SCHEMA ERROR::: {}'.format(e.message))


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
        # TODO: Figure out issue with validation 'None' error.
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
        pl = {}
        for k in payload:
            if payload[k] is not None:
                pl[k] = payload[k]
            else:
                pass
        schema_json = 'get_history.json'
        validate_payload(schema_json, pl)
        print("\nCheck 01 finished\n")

        pl["user"] = "nettles4349"
        print('    user={}'.format(pl["user"]))
        validate_payload(schema_json, pl)
        print("Check 02 finished --- user=\"nettles4349\"\n")

        pl["grandparent_rating_key"] = 3744
        '    grandparent_rating_key={}'.format(
            pl["grandparent_rating_key"]
        )
        print('   "grandparent_rating_key"={}'.format(
            pl["grandparent_rating_key"])
        )
        validate_payload(schema_json, pl)
        print("Check 03 finished --- gp_rtg_ky=3744\n")

        pl["grandparent_rating_key"] = "3744"
        print('    grandparent_rating_key={}'.format(
            pl["grandparent_rating_key"])
        )
        validate_payload(schema_json, pl)
        print("Check 04 finished --- gp_rtg_ky=\"3744\"\n")

        pl["cmd"] = None
        print('    cmd={}'.format(pl["cmd"]))
        validate_payload(schema_json, pl)
        print("Check 05 finished --- cmd=None (FAIL)")


if __name__ == '__main__':
    unittest.main()
