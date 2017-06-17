#!/usr/bin/env python
#encoding:utf-8

from config.settings import YML_JSON
from flask import request



def parse_form(name):
    form_json = YML_JSON.get(name)
    returnvalue = form_json.get('returnvalue')
    return dict(zip(returnvalue, [request.form.get(x) for x in returnvalue]))


def parse_history(form):
    history_dict = {}
    times = len(form) / 4
    for time in xrange(times+1):
        if time != 0:
            history_dict[str(time)] = {k.split('-')[0]: v  for k,v in form.iteritems() if int(k.split('-')[1]) == time}
    return history_dict