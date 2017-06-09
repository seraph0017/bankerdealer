#!/usr/bin/env python
#encoding:utf-8


from src.models.basemodel import EntityWithNameModel
from src.ext import db



class Role(EntityWithNameModel):

    commit = db.Column(db.String(120))