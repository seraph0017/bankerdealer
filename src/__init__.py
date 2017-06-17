#!/usr/bin/env python
#encoding:utf-8

import yaml
import jwt
from flask import Flask, jsonify, g, request, abort, url_for

from config import settings

from src.ext import db
from src.admin import admin
from src.views.enterprise import enterprise
from src.views.bank import banker





DEFAULT_APP_NAME = settings.PROJECT_NAME

DEFAULT_MODULES = (
        (banker,'/banker'),
        (enterprise,'/enterprise'),
        )


def create_app(app_name=None, modules = None):
    if app_name is None: app_name = DEFAULT_APP_NAME
    if modules is None: modules = DEFAULT_MODULES
    app = Flask(app_name)
    configure_conf(app)
    configure_template(app)
    configure_static(app)
    configure_exts(app)
    configure_modules(app, modules)
    configure_before_handlers(app)
    configure_logout(app)
    return app




def configure_conf(app):
    app.config.from_pyfile('config/settings.py')


def configure_logout(app):

    @app.route('/logout')
    def logout_handler():
        request.cookies.pop(settings.AUTH_KEY, None)


def configure_errorhandlers(app):

    if app.debug: return

    @app.errorhandler(404)
    def not_found(error):
        return jsonify(dict(status_code=404))



def configure_modules(app,modules):
    for module, url_prefix in modules:
        app.register_blueprint(module,url_prefix=url_prefix)



def configure_before_handlers(app):

    @app.before_request
    def auth():
        g.menus = [
            {'name': u'概况','href': url_for('enterprise.detail_handler')},
            {'name': u'历史沿革','href': url_for('enterprise.history_handler')},
            {'name': u'行业','href': url_for('enterprise.industry_handler')},
            {'name': u'经营范围','href': url_for('enterprise.operate_handler')},
            {'name': u'资产情况','href': url_for('enterprise.finance_handler')},
            {'name': u'信用','href': url_for('enterprise.credit_handler')},
        ]
        cj = request.cookies.get(settings.AUTH_KEY)
        g.role = ''
        g.username = ''
        g.userid = ''
        if cj:
            info = {}
            try:
                info = jwt.decode(cj, settings.SECRET)
            except Exception as e:
                abort(403)
            g.role = info.get('role')
            g.username = info.get('username')
            g.userid = info.get('userid')





def configure_exts(app):
    db.init_app(app)
    admin.init_app(app)


def configure_template(app):
    app.template_folder = app.config['TEMPLATE_FOLDER']


def configure_static(app):
    app.static_folder = app.config['STATIC_FOLDER']