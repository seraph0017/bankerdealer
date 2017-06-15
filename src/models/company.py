#!/usr/bin/env python
#encoding:utf-8

from src.models.basemodel import EntityModel
from src.ext import db



class Company(EntityModel):

    name = db.Column(db.String(120))
    credit_code = db.Column(db.Integer)
    register_addr = db.Column(db.String(120))
    register_capital = db.Column(db.String(120))
    representative = db.Column(db.String(120))
    establish_time = db.Column(db.String(120))
    business_scope = db.Column(db.Text)
    user_id = db.Column(db.Integer)
