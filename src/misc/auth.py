#!/usr/bin/env python
#encoding:utf-8


from functools import wraps
from flask import request, abort, redirect, url_for, make_response
from config.settings import AUTH_KEY, logger
from src.business.auth import AuthBusiness



def required(rolename):
    def dec(func):
        @wraps(func)
        def _(*args, **kwargs):
            jwt = request.cookies.get(AUTH_KEY)
            if jwt:
                info = {}
                try:
                    info = AuthBusiness.jwt_decode(jwt)
                except Exception as e:
                    resp = make_response(redirect(url_for('{}.login_handler'.format(rolename))))
                    resp.set_cookie(AUTH_KEY, "")
                    return resp
                role = info.get('role')
                if role == rolename:
                    return func(*args, **kwargs)
                abort(403)
            resp = make_response(redirect(url_for('{}.login_handler'.format(rolename))))
            resp.set_cookie(AUTH_KEY, "")
            return resp
        return _
    return dec




