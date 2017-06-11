#!/usr/bin/env python
#encoding:utf-8


from src.models import *



class UserBusiness(object):


    @classmethod
    def _query(cls):
        return User.query\
            .outerjoin(Role, Role.id == User.role_id)\
            .add_columns(

            )


    @classmethod
    def login(cls, username, password):
        ret = User.query.get(username=username, password=User.gen_password(password))
        if len(ret) == 0:
            return 3001
        pass

