#!/usr/bin/env python
#encoding:utf-8

from src.models.basemodel import EntityModel
from src.ext import db


class Credit(EntityModel):

    credict_info = db.Column(db.String(300))
    lawsuit_info = db.Column(db.String(300))
    company_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer)