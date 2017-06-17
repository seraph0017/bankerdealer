#!/usr/bin/env python
#encoding:utf-8

from src.models.basemodel import EntityModel
from src.ext import db


class Sales(EntityModel):

    product_name = db.Column(db.String(100))
    buyer_name = db.Column(db.String(100))
    corporate_year = db.Column(db.Float)
    sales_money = db.Column(db.Float)
    sales_percentage = db.Column(db.Float)
    company_id = db.Column(db.Integer)