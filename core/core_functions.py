from decimal import Decimal
from babel.numbers import format_decimal

from Calculus.settings import LANGUAGE_CODE


def format_list_decimal2string(queryset):
    res = []
    for elem in list(queryset.values()):
        reformatted_elem = {}
        for k, v in elem.items():
            if type(v) == Decimal:
                # Format Decimal to string
                reformatted_elem[k] = format_decimal(v, format='#,##0.00', locale=LANGUAGE_CODE[:2])
            else:
                # Keep as is
                reformatted_elem[k] = v
        res.append(reformatted_elem)
    return res


def format_dict_decimal2string(queryset):
    res = {}
    d = queryset if type(queryset) == dict else queryset.__dict__
    for k, v in d.items():
        if type(v) == Decimal:
            # Format Decimal to string
            res[k] = format_decimal(v, format='#,##0.00', locale=LANGUAGE_CODE[:2])
        elif k != '_state':
            # Keep as is
            res[k] = v
    return res
