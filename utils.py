import os
from sys import platform
import json
import requests
from jsonschema import validate, ValidationError, SchemaError, RefResolver
"""Utility functions for tautulli_api"""


def get_os():
    """Checks user's operating system"""
    linux = 'linux'
    windows = 'windows'
    osx = 'osx'
    # Linux
    if platform == 'linux' or platform == 'linux2':
        return linux
    # OS X
    elif platform == 'darwin':
        return osx
    # Windows
    elif platform == 'win32' or platform == 'cygwin':
        return windows


# Function to check if kwargs are correct
def check_kwargs(kw_dict, payload_dict):
    for kw, val in kw_dict.items():
        if kw in payload_dict:
            payload_dict[kw] = val
        else:
            raise ValueError(
                '{0} is not an accepted parameter'.format(kw)
            )


def check_bin_kw(kw_item, is_required=False):
    if kw_item is not None:
        if kw_item == 0 | 1:
            pass
        else:
            raise TypeError(
                'BINARY TYPE ERROR'
            )
    elif is_required:
            raise ValueError(
                'ERROR - BINARY VALUE IS REQUIRED'
            )
    else:
        pass


def check_bool_kw(kw_item, is_required=False):
    if kw_item is not None:
        if type(kw_item) == bool:
            pass
        else:
            raise TypeError(
                'BOOLEAN TYPE ERROR'
            )
    elif is_required:
            raise ValueError(
                'ERROR - BOOLEAN VALUE IS REQUIRED'
            )
    else:
        pass


def check_str_kw(kw_item, value_check_dict=None, is_required=False):
    if kw_item is not None:
        if type(kw_item) == str:
            if value_check_dict is None:
                pass
            elif kw_item in value_check_dict:
                pass
            else:
                raise ValueError(
                    'INCORRECT STRING ERROR'
                )
        else:
            raise TypeError(
                'STRING TYPE ERROR'
            )
    elif is_required:
            raise ValueError(
                'ERROR - STRING VALUE IS REQUIRED'
            )
    else:
        pass


def check_pos_int_kw(kw_item, is_required=False):
    if kw_item is not None:
        if type(kw_item) == int:
            if kw_item >= 0:
                pass
            else:
                raise ValueError(
                    'ERROR - INTEGER VALUE CANNOT BE NEGATIVE'
                )
        else:
            raise TypeError(
                'INTEGER TYPE ERROR'
            )
    elif is_required:
            raise ValueError(
                'ERROR - INTEGER VALUE IS REQUIRED'
            )
    else:
        pass


# Send/receive requests
def send_receive_request(url, params_dict):
    r = requests.get(url, params=params_dict)
    if r.status_code == 200:
        response = json.loads(r.content.decode('utf-8'))
        return response
    else:
        r.raise_for_status()


# Send/receive request with text response
def send_receive_request_text(url, params_dict):
    r = requests.get(url, params=params_dict)
    if r.status_code == 200:
        return r
    else:
        r.raise_for_status()


# Pretty print json
def pprint_json(json_data, sort_keys=True, indent=4):
    pprint_result = json.dumps(json_data, sort_keys=sort_keys, indent=indent)
    return pprint_result


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
