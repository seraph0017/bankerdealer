#!/usr/bin/env python
#encoding:utf-8

from src.models.basemodel import EntityModel
from src.ext import db


class ShareHolder(EntityModel):

    name = db.Column(db.String(120))
    id_num = db.Column(db.String(120))
    investment_method = db.Column(db.String(120))
    money = db.Column(db.Float)
    shareholding_ratio = db.Column(db.Float)
    relationship = db.Column(db.String(120))
    company_id = db.Column(db.Integer)