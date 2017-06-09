#!/usr/bin/env python
#encoding:utf-8


from src.models import *



class UserBusiness(object):


    @classmethod
    def _query(cls):
        return User.query\
            .outerjoin(UserBindRole, User.id == UserBindRole.user_id)\
            .outerjoin(Role, Role.id == UserBindRole.role_id)

    @classmethod
    def login(cls, username, password):
        ret = User.query.get(username=username, password=User.gen_password(password))
        if len(ret) == 0:
            return 3001
        pass

