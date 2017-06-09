#!/usr/bin/env python
#encoding:utf-8

import yaml
from flask import Flask, jsonify, g

from config import settings

from src.ext import db
from src.admin import admin
from src.views.administrator import administrator





DEFAULT_APP_NAME = settings.PROJECT_NAME

DEFAULT_MODULES = (
        (administrator,'/administrator'),
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
    return app




def configure_conf(app):
    app.config.from_pyfile('config/settings.py')



def configure_errorhandlers(app):

    if app.debug: return

    @app.errorhandler(404)
    def not_found(error):
        return jsonify(dict(status_code=404))



def configure_modules(app,modules):
    for module, url_prefix in modules:
        app.register_blueprint(module,url_prefix="/v1{}".format(url_prefix))



def configure_before_handlers(app):

    @app.before_request
    def auth():
        #TODO
        g.user = ''


def configure_exts(app):
    db.init_app(app)
    admin.init_app(app)


def configure_template(app):
    app.template_folder = app.config['TEMPLATE_FOLDER']


def configure_static(app):
    app.static_folder = app.config['STATIC_FOLDER']