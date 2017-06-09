#!/usr/bin/env python
#encoding:utf-8


from functools import wraps
from flask import request, abort
from config.settings import AUTH_KEY
from src.business.auth import AuthBusiness



def required(rolename):
    def dec(func):
        @wraps(func)
        def _(*args, **kwargs):
            jwt = request.headers.get(AUTH_KEY)
            if jwt:
                try:
                    info = AuthBusiness.jwt_decode(jwt)
                except:
                    abort(403)
                role = info.get('role')
                if role == rolename:
                    return func(*args, **kwargs)
                abort(403)
            abort(403)
        return _
    return dec




