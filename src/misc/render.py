#!/usr/bin/env python
#encoding:utf-8


from config.settings import CODE_MAP


def brender(code):
    return CODE_MAP.get(code)
