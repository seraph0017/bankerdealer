#!/usr/bin/env python
#encoding:utf-8

from flask import Blueprint, request, render_template, \
    g, redirect, make_response, url_for, abort
from src.misc.auth import required
from src.misc.validation import validation
from src.misc.parse import parse_form
from src.business import *
from config.settings import AUTH_KEY


banker = Blueprint('banker', __name__)


@banker.route('/login', methods = ['GET', 'POST'])
@validation('POST:login')
def login_handler():
    role = u'银行'
    if request.method == 'POST':
        info = parse_form('login')
        token = AuthBusiness.login(**info)
        if token:
            resp = make_response(redirect(url_for('banker.index_handler')))
            resp.set_cookie(AUTH_KEY, token)
            return resp
        abort(314)
    return render_template('login.html', **locals())

@banker.route('/logout')
def logout_handler():
    resp = make_response(redirect(url_for('banker.login_handler')))
    resp.set_cookie(AUTH_KEY, "")
    return resp

@banker.route('/')
@required('banker')
def index_handler():
    menus = [
        dict(
            name = u'申请列表',
            href = '/banker/'
        )
    ]
    enterprise_list = EnterpriseBusiness.get_list()
    return render_template('banker/list.html', menus = menus, enterprise_list = enterprise_list)



@banker.route('/<int:enterprise_id>', methods = ['GET', 'POST'])
@required('banker')
@validation('POST:add_company')
def detail_handler(enterprise_id):
    menus = [
        dict(
            name = u'申请列表',
            href = '/banker/'
        )
    ]
    company = CompanyBusiness.get_by_id(enterprise_id)
    if request.method == 'POST':
        info = parse_form('add_company')
        info.update(dict(user_id=enterprise_id))
        CompanyBusiness.save(info)
        return render_template('banker/detail.html',user_id = enterprise_id, menus = menus, company=company)
    return render_template('banker/detail.html',user_id = enterprise_id, menus = menus, company=company)


