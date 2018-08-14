import datetime

import sqlalchemy
from sqlalchemy import orm

from data.sqlalchemybase import SqlAlchemyBase


class Rental(SqlAlchemyBase):
    __tablename__ = 'rentals'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)

    created_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now, index=True)
    start_time = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now, index=True)
    end_time = sqlalchemy.Column(sqlalchemy.DateTime, index=True)

    user_id = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey('users.id'), nullable=False)
    user = orm.relation('User', back_populates='rentals')

    scooter_id = sqlalchemy.Column(sqlalchemy.String, sqlalchemy.ForeignKey('scooters.id'), nullable=False)
    scooter = orm.relation('Scooter')
