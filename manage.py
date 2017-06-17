#!/usr/bin/env python
#encoding:utf-8

from flask import current_app
from flask_script import Manager, Server, Shell

from src import create_app
from src.models import *
from src.ext import db

manager = Manager(create_app)
server = Server(host='0.0.0.0',port=5001,use_debugger=True)

def make_shell_context():
    return dict(
            app     = current_app,
            )

manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('runserver', server)


def dadd(inputs):
    for i in inputs:
        db.session.add(i)
    db.session.commit()


@manager.command
def createdb():
    db.create_all()

    #固定配置 初始化
    #----------------------------------------------------------
    r1 = Role(name='administrator')
    r2 = Role(name='banker')
    r3 = Role(name='enterprise')

    dadd([r1, r2, r3])
    #----------------------------------------------------------

    u1 = User(real_name=u"键盘侠骨骼专业医院", name=u'seraph0017@hotmail.com', password=User.gen_password('1q2w3e4r'), role_id = r1.id)
    u2 = User(real_name=u"鼠标侠骨骼专业医院", name=u'372499885@qq.com', password=User.gen_password('1q2w3e4r'), role_id = r2.id)
    u3 = User(real_name=u"德国制造骨骼专业医院", name=u'jjrddu@qq.com', password=User.gen_password('1q2w3e4r'), role_id = r3.id)

    dadd([u1, u2, u3])



@manager.command
def dropdb():
    db.drop_all()


@manager.command
def initdb():
    dropdb()
    createdb()

if __name__ == "__main__":
    manager.run()