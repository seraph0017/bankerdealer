#!/usr/bin/env python
#encoding:utf-8

from src.models.basemodel import EntityModel
from src.ext import db


class Operate(EntityModel):

    operate_statement = db.Column(db.String(500))
    purchase_statement = db.Column(db.String(500))
    production_statement = db.Column(db.String(500))
    market_statement = db.Column(db.String(500))
    company_id = db.Column(db.Integer)