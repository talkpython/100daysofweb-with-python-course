import datetime

import sqlalchemy
from sqlalchemy import orm

from data.sqlalchemybase import SqlAlchemyBase


class Location(SqlAlchemyBase):
    __tablename__ = 'locations'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)

    created_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now, index=True)

    street = sqlalchemy.Column(sqlalchemy.String)
    city = sqlalchemy.Column(sqlalchemy.String, index=True)
    state = sqlalchemy.Column(sqlalchemy.String, index=True)

    max_storage = sqlalchemy.Column(sqlalchemy.Integer, index=True)

    scooters = orm.relation('Scooter', back_populates='location')
