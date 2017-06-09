#!/usr/bin/env python
#encoding:utf-8

from flask import current_app
from flask.ext.script import Manager, Server, Shell

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
    r2 = Role(name='bank')
    r3 = Role(name='enterprise')

    dadd([r1, r2, r3])
    #----------------------------------------------------------

    u1 = User(name=u'张三', password=User.gen_password('1q2w3e4r'))
    u2 = User(name=u'李四', password=User.gen_password('1q2w3e4r'))
    u3 = User(name=u'王麻子', password=User.gen_password('1q2w3e4r'))

    ubr1 = UserBindRole(user_id = u1.id, role_id = r1.id)
    ubr2 = UserBindRole(user_id = u2.id, role_id = r2.id)
    ubr3 = UserBindRole(user_id = u3.id, role_id = r3.id)

    dadd([ubr1, ubr2, ubr3])

@manager.command
def dropdb():
    db.drop_all()

if __name__ == "__main__":
    manager.run()