"""
Utility functions for tautulli_api
"""


# Function to check if kwargs are correct
def check_kwargs(kwarg_dict, payload_dict):
    for k, v in kwarg_dict.items():
        if k in payload_dict:
            payload_dict[k] = v
        else:
            raise ValueError(
                '{0} is not an accepted parameter'.format(k)
            )


# Check kwarg type functions
def check_bin_kw(kw_dict, kw_item):
    if kw_dict[kw_item] is not None:
        if kw_dict[kw_item] == 0 | 1:
            pass
        else:
            raise TypeError(
                '"{0}=<val>" <val> MUST be 0 or 1'.format(kw_item)
            )
    else:
        pass


def check_str_kw(kw_dict, kw_item, *value_check_dict):
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
    else:
        pass


def check_pos_int_kw(kw_dict, kw_item):
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
    else:
        pass


def check_param_types(kw_dict, pos_int_list,
                      str_list, bin_list, *value_check_dict):
    for k in kw_dict.items():
        if k in pos_int_list:
            check_pos_int_kw(kw_dict, k)
        elif k in str_list:
            check_str_kw(kw_dict, k, value_check_dict)
        elif k in bin_list:
            check_bin_kw(kw_dict, k)
