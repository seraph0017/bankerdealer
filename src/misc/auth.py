#!/usr/bin/env python
#encoding:utf-8


from functools import wraps
from flask import request, abort, redirect, url_for
from config.settings import AUTH_KEY, logger
from src.business.auth import AuthBusiness



def required(rolename):
    def dec(func):
        @wraps(func)
        def _(*args, **kwargs):
            jwt = request.cookies.get(AUTH_KEY)
            if jwt:
                try:
                    info = AuthBusiness.jwt_decode(jwt)
                except Exception as e:
                    redirect(url_for('{}.login_handler'.format(rolename)))
                role = info.get('role')
                if role == rolename:
                    return func(*args, **kwargs)
                abort(403)
            redirect(url_for('{}.login_handler'.format(rolename)))
        return _
    return dec




