#!/usr/bin/env python
#encoding:utf-8

from src.models.basemodel import EntityModel
from src.ext import db


class Revenue(EntityModel):

    year = db.Column(db.String(10))
    product_name = db.Column(db.String(100))
    income = db.Column(db.Float)
    percentage = db.Column(db.Float)
    gross = db.Column(db.Float)
    company_id = db.Column(db.Integer)