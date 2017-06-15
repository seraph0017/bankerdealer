#!/usr/bin/env python
#encoding:utf-8

from src.models.basemodel import EntityModel
from src.ext import db


class Industry(EntityModel):

    first_industry = db.Column(db.String(50))
    second_industry = db.Column(db.String(50))
    major_product = db.Column(db.String(100))
    technical_factor = db.Column(db.String(500))
    supdem_factor = db.Column(db.String(500))
    government_factor = db.Column(db.String(500))
    humanity_factor = db.Column(db.String(500))
    international_factor = db.Column(db.String(500))
    profit_factor = db.Column(db.String(500))
    other_factor = db.Column(db.String(500))
    company_id = db.Column(db.Integer)