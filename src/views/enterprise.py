#!/usr/bin/env python
#encoding:utf-8

from flask import Blueprint
from src.misc.auth import require_role


enterprise = Blueprint('enterprise', __name__)


@enterprise.route('/login', methods = ['GET', 'POST'])
def login_handler():
    pass