#!/usr/bin/env python
#encoding:utf-8


from src.models.basemodel import EntityWithNameModel
from src.ext import db
from config.settings import SALT
from hashlib import md5




class User(EntityWithNameModel):


    password = db.Column(db.String(120), default='a13f7d4051bfcd2280f8848be893dc10')
    role_id = db.Column(db.Integer)
    real_name = db.Column(db.String(300))


    @classmethod
    def gen_password(cls, origin_password):
        return md5("{}{}".format(SALT, origin_password)).hexdigest()