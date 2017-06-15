#!/usr/bin/env python
#encoding:utf-8

from flask import Blueprint, request, render_template, \
    g, redirect, make_response, url_for, abort
from src.misc.auth import required
from src.misc.validation import validation
from src.misc.parse import parse_form
from src.business import *
from config.settings import AUTH_KEY


enterprise = Blueprint('enterprise', __name__)


@enterprise.route('/login', methods = ['GET', 'POST'])
@validation('POST:login')
def login_handler():
    role = u'企业'
    if request.method == 'POST':
        info = parse_form('login')
        token = AuthBusiness.login(**info)
        if token:
            resp = make_response(redirect(url_for('enterprise.index_handler')))
            resp.set_cookie(AUTH_KEY, token)
            return resp
        abort(314)
    return render_template('login.html', **locals())


@enterprise.route('/logout')
def logout_handler():
    resp = make_response(redirect(url_for('enterprise.login_handler')))
    resp.set_cookie(AUTH_KEY, "")
    return resp

@enterprise.route('/')
@required('enterprise')
def index_handler():
    return render_template('enterprise/list.html', menus = g.menus)



@enterprise.route('/<int:enterprise_id>', methods = ['GET', 'POST'])
@required('enterprise')
@validation('POST:add_company')
def detail_handler(enterprise_id):
    company = CompanyBusiness.get_by_id(enterprise_id)
    if request.method == 'POST':
        info = parse_form('add_company')
        info.update(dict(user_id=enterprise_id))
        CompanyBusiness.save(info)
        return render_template('enterprise/detail.html',user_id = enterprise_id, menus = g.menus, company=company)
    return render_template('enterprise/detail.html',user_id = enterprise_id, menus = g.menus, company=company)









