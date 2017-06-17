#!/usr/bin/env python
#encoding:utf-8

from src.models import *
from src.ext import db


class CompanyBusiness(object):


    @classmethod
    def save(cls, info):
        ret = cls.get_by_id(info.get('user_id'))
        if ret is None:
            company = Company(**info)
            db.session.add(company)
            db.session.commit()
            return 0
        for k,v in info.iteritems():
            setattr(ret, k, v)
        db.session.add(ret)
        db.session.commit()
        return 0



    @classmethod
    def get_by_id(cls, id):
        return Company.query.filter(Company.user_id == id).first()