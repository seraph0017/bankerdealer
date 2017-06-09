#!/usr/bin/env python
#encoding:utf-8

from src.models.basemodel import EntityModel
from src.ext import db



class UserBindRole(EntityModel):

    user_id = db.Column(db.Integer)
    role_id = db.Column(db.Integer)