#!/usr/bin/env python
#encoding:utf-8

from src.models.basemodel import EntityModel
from src.ext import db


class Supply(EntityModel):

    product_name = db.Column(db.String(100))
    supplier_name = db.Column(db.String(100))
    corporate_year = db.Column(db.Float)
    purchase_money = db.Column(db.Float)
    purchase_percentage = db.Column(db.Float)
    company_id = db.Column(db.Integer)