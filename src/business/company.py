#!/usr/bin/env python
#encoding:utf-8

from src.models import *
from src.ext import db


class CompanyBusiness(object):


    @classmethod
    def save(cls, info):
        company = Company(**info)
        db.session.add(company)
        db.session.commit()

    @classmethod
    def get_by_id(cls, id):
        return Company.query.get(id)