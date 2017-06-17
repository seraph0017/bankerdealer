#!/usr/bin/env python
#encoding:utf-8


import yaml
import logging
import logging.config
from os import listdir
from os.path import abspath, dirname, join




PROJECT_NAME                    = 'bankerdealer'
PROJECT_PATH                    = dirname(dirname(abspath(__file__)))
VALIDATE_YML_PATH               = join(PROJECT_PATH, 'src', 'validation')

TEMPLATE_FOLDER                 = join(PROJECT_PATH, 'src', 'template')
STATIC_FOLDER                   = join(PROJECT_PATH, 'src', 'static')
SQLALCHEMY_TRACK_MODIFICATIONS  = False
SQLALCHEMY_DATABASE_URI         = 'mysql://root:123456@127.0.0.1:3306/bankerdealer'
AUTH_KEY                        = 'Authorization'
SECRET_KEY                      = 'shizifan'


SALT                            = 'i>_<i'
SECRET                          = 'max'
JWT_ALGORITHM                   = 'HS256'
SESSION_TIME                    = 60 * 60

logging.config.fileConfig(join(PROJECT_PATH, 'config', 'logging.conf'))
logger = logging.getLogger('liaoning')


CODE_MAP                        = {
    3001 : u"用户名或密码错误"
}

YML_JSON = {}
for fi in listdir(VALIDATE_YML_PATH):
    with open(join(VALIDATE_YML_PATH, fi), 'rb') as f:
        YML_JSON.update(yaml.load(f.read()))