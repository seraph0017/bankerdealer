#!/usr/bin/env python
#encoding:utf-8


from flask_admin.contrib.sqla import ModelView
from src.ext import db, admin
from src.models import *


admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Role, db.session))
admin.add_view(ModelView(Company, db.session))
admin.add_view(ModelView(History, db.session))
admin.add_view(ModelView(ShareHolder, db.session))




admin.add_view(ModelView(UserBindRole, db.session))