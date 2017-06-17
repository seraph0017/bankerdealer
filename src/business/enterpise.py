#!/usr/bin/env python
#encoding:utf-8

from src.models import *
from src.ext import db



class EnterpriseBusiness(object):


    @classmethod
    def get_list(cls):
        return User.query.filter(User.role_id == 3).all()

