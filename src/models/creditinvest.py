#!/usr/bin/env python
#encoding:utf-8

from src.models.basemodel import EntityModel
from src.ext import db


class CreditInvest(EntityModel):

    item_info = db.Column(db.String(300))
    company_id = db.Column(db.Integer)