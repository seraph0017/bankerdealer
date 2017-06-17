#!/usr/bin/env python
#encoding:utf-8

import jwt
import datetime

from src.models import *
from flask import request
from config.settings import AUTH_KEY, SESSION_TIME, SECRET, JWT_ALGORITHM



class AuthBusiness(object):


    @classmethod
    def _query(cls):
        return User.query\
            .outerjoin(Role, User.role_id == Role.id)\
            .add_columns(
                User.id.label('userid'),
                User.name.label('username'),
                Role.name.label('role')
            )


    @classmethod
    def login(cls, username, password):
        ret = cls._query().filter(User.name == username, User.password == User.gen_password(password)).first()
        if ret is None:
            return False
        return cls.jwt_encode(ret.userid, ret.username, ret.role)


    @classmethod
    def jwt_encode(cls, userid, username, role, exp = SESSION_TIME):
        return jwt.encode(
            dict(username=username,\
                userid=userid,\
                role=role,\
                exp=datetime.datetime.now() + datetime.timedelta(seconds=SESSION_TIME)),\
                SECRET,\
                algorithm = JWT_ALGORITHM
        )


    @classmethod
    def jwt_decode(cls, st):
        return jwt.decode(st, SECRET, algorithm=JWT_ALGORITHM)