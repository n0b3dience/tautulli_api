import json
import requests
"""
Utility functions for tautulli_api
"""


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
