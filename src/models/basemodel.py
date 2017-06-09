#!/usr/bin/env python
#encoding: utf-8


from datetime import datetime

from src.ext import db


class EntityModel(db.Model):

    __abstract__ = True

    __table_args__ = (
        dict(
            mysql_engine='InnoDB',
            mysql_charset='utf8',
        )
    )


    id = db.Column(db.Integer, primary_key=True)
    creation_time = db.Column(db.DateTime, default=datetime.now)
    modified_time = db.Column(db.TIMESTAMP,
                              nullable=False,
                              default=db.func.current_timestamp())

    @classmethod
    def gets(cls, ids):
        return cls.query.filter(cls.id.in_(ids)).all()







class EntityWithNameModel(EntityModel):

    __abstract__ = True

    name = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return self.name

    def __unicode__(self):
        return self.name
