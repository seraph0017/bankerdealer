#!/usr/bin/env python
#encoding:utf-8

from src.models.basemodel import EntityModel
from src.ext import db


class History(EntityModel):


    content = db.Column(db.String(120))
    change_time = db.Column(db.String(120))
    change_before = db.Column(db.String(200))
    change_after = db.Column(db.String(200))
    company_id = db.Column(db.Integer)