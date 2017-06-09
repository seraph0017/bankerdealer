#!/usr/bin/env python
#encoding:utf-8

import logging
import logging.config

from os.path import abspath, dirname, join




PROJECT_NAME                    = 'bankerdealer'
PROJECT_PATH                    = dirname(dirname(abspath(__file__)))

TEMPLATE_FOLDER                 = join(PROJECT_PATH, 'src', 'template')
STATIC_FOLDER                   = join(PROJECT_PATH, 'src', 'template')
SQLALCHEMY_TRACK_MODIFICATIONS  = False
SQLALCHEMY_DATABASE_URI         = 'mysql://root:123456@127.0.0.1:3306/bankerdealer'
AUTH_KEY                        = 'Authorization'
SECRET_KEY                      = 'shizifan'


SALT                            = 'i>_<i'
SECRET                          = 'max'
JWT_ALGORITHM                   = 'HS256'



CODE_MAP                        = {
    3001 : u"用户名或密码错误"
}

