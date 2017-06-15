#!/usr/bin/env python
#encoding:utf-8

from src.models.basemodel import EntityModel
from src.ext import db


class Revenue(EntityModel):

    profit_ability = db.Column(db.String(100))
    debtpay_ability = db.Column(db.String(100))
    cashflow_ability = db.Column(db.String(100))
    company_id = db.Column(db.Integer)