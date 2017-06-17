#!/usr/bin/env python
#encoding:utf-8

import json
from collections import OrderedDict
from src.models import *
from src.ext import db




class HistoryBusiness(object):


    @classmethod
    def save(cls, info_dict, user_id):
        ret = cls._get_by_id(user_id)
        if ret is None:
            history = History(
                content = json.dumps(info_dict),
                user_id = user_id
            )
            db.session.add(history)
            db.session.commit()
            return 0
        ret.content = json.dumps(info_dict)
        db.session.add(ret)
        db.session.commit()
        return 0

    @classmethod
    def _get_by_id(cls, enterprise_id):
        return History.query.filter(History.user_id == enterprise_id).first()

    @classmethod
    def get_by_id(cls, enterprise_id):
        ret = History.query.filter(History.user_id == enterprise_id).first()
        if ret:
            ori_history = json.loads(ret.content)
            pipe_history = OrderedDict(sorted(ori_history.items(), key=lambda t: t[0]))
            return [v for k,v in pipe_history.iteritems()]
        return None


        