#!/usr/bin/env python
#encoding:utf-8

from flask import Blueprint
from src.misc.auth import required


administrator = Blueprint('administrator', __name__)


@administrator.route('/login', methods = ['GET', 'POST'])
def login_handler():
    pass