#!/usr/bin/env python
#encoding:utf-8
from copy import deepcopy
from functools import wraps
from config.settings import YML_JSON
from flask import request, abort


def validation(validate_name = None):

    def validate_required(key, value):
        request_value = request.form.get(key)
        expect_value = value
        if request_value is None:
            abort(314)
        return True, 1


    def validate_min_length(key, value):
        request_value = request.form.get(key)
        expect_value = value
        if request_value is not None and len(request_value) < expect_value:
            abort(314)
        return True, 1


    def validate_max_length(key, value):
        request_value = request.form.get(key)
        expect_value = value
        if request_value is not None and len(request_value) > expect_value:
            abort(314)
        return True, 1

    def validate_type(key, value):
        ttype_dict = {
            'list': list,
            'basestring': basestring,
            'dict': dict,
            'int': int,
            'bool': bool,
        }
        request_value = request.form.get(key)
        expect_value = value
        if request_value is not None and not isinstance(request_value, ttype_dict.get(value)):
            return False, json_detail_render(203, [], "{} should be a {}".format(key, value))
        return True, 1

    KEY_FUNC_MAP = {
        'required': validate_required,
        'min_length': validate_min_length,
        'max_length': validate_max_length,
        'type': validate_type,
    }

    def wrapper(func):
        @wraps(func)
        def _(*args, **kwargs):
            protocol, vname = validate_name.split(':')
            if request.method == protocol:
                all_json = YML_JSON
                validate_json = deepcopy(all_json.get(vname))
                del validate_json['returnvalue']
                for item, settings in validate_json.items():
                    for key, value in settings.items():
                        f = KEY_FUNC_MAP.get(key)
                        ret = f(item, value)
                        if not ret[0]:
                            return ret[1]
            return func(*args, **kwargs)
        return _
    return wrapper