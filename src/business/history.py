#!/usr/bin/env python
#encoding:utf-8

import json
from src.models import *
from src.ext import db




class HistoryBusiness(object):


    @classmethod
    def save(cls, info_dict, user_id):
        history = History(
            content = json.dumps(info_dict),
            user_id = user_id
        )
        db.session.add(history)
        db.session.commit()
        return 0


    @classmethod
    def get_by_id(cls, enterprise_id):
        return History.query.filter(History.user_id == enterprise_id).first()
        