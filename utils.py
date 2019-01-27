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


# Check kwarg type functions
def check_bin_kw(kw_dict, kw_item, is_required=False):
    if kw_dict[kw_item] is not None:
        if kw_dict[kw_item] == 0 | 1:
            pass
        else:
            raise TypeError(
                '"{0}=<val>" <val> MUST be 0 or 1'.format(kw_item)
            )
    elif is_required:
            raise ValueError(
                '"{0}" is a required keyword argument'
            )
    else:
        pass


def check_bool_kw(kw_dict, kw_item, is_required=False):
    if kw_dict[kw_item] is not None:
        if type(kw_dict[kw_item]) == bool:
            pass
        else:
            raise TypeError(
                '"{0}=<val>" <val> MUST be BOOLEAN'.format(kw_item)
            )
    elif is_required:
            raise ValueError(
                '"{0}" is a required keyword argument'
            )
    else:
        pass


def check_str_kw(kw_dict, kw_item, *value_check_dict, is_required=False):
    if kw_dict[kw_item] is not None:
        if type(kw_dict[kw_item]) == str:
            if kw_dict[kw_item] in value_check_dict:
                if kw_dict[kw_item] in value_check_dict[kw_item]:
                    pass
                else:
                    raise ValueError(
                        '"{0}=<val>" <val> MUST be one of the following:\n'
                        '    {1}'.format(kw_item, value_check_dict[kw_item])
                    )
            else:
                pass
        else:
            raise TypeError(
                '"{0}=<val>" <val> MUST be a STRING'.format(kw_item)
            )
    elif is_required:
            raise ValueError(
                '"{0}" is a required keyword argument'
            )
    else:
        pass


def check_pos_int_kw(kw_dict, kw_item, is_required=False):
    if kw_dict[kw_item] is not None:
        if type(kw_dict[kw_item]) == int:
            if kw_dict[kw_item] >= 0:
                pass
            else:
                raise ValueError(
                    '"{0}=<val>" <val> CANNOT be NEGATIVE'.format(kw_item)
                )
        else:
            raise TypeError(
                '"{0}=<val>" <val> MUST be an INTEGER'.format(kw_item)
            )
    elif is_required:
            raise ValueError(
                '"{0}" is a required keyword argument'
            )
    else:
        pass


def check_param_types(
    kw_dict,
    *value_check_dict,
    pos_int_list=None,
    str_list=None,
    bin_list=None,
    bool_list=None,
):
    for kw in kw_dict.items():
        if pos_int_list is not None and kw in pos_int_list:
            check_pos_int_kw(kw_dict, kw)
        elif str_list is not None and kw in str_list:
            check_str_kw(kw_dict, kw, value_check_dict)
        elif bin_list is not None and kw in bin_list:
            check_bin_kw(kw_dict, kw)
        elif bool_list is not None and kw in bool_list:
            check_bool_kw(kw_dict, kw)


# Send/receive requests
def send_receive_request(url, params_dict):
    r = requests.get(url, params=params_dict)
    if r.status_code == 200:
        response = json.loads(r.content.decode('utf-8'))
        return response
    else:
        r.raise_for_status()
