#!/usr/bin/env python
#encoding:utf-8

from config.settings import YML_JSON
from flask import request



def parse_form(name):
    form_json = YML_JSON.get(name)
    returnvalue = form_json.get('returnvalue')
    return dict(zip(returnvalue, [request.form.get(x) for x in returnvalue]))