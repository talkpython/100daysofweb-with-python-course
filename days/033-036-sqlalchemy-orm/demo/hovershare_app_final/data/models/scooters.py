import datetime

import sqlalchemy as sa
from sqlalchemy import orm

from data.sqlalchemybase import SqlAlchemyBase


class Scooter(SqlAlchemyBase):
    __tablename__ = 'scooters'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    created_date = sa.Column(sa.DateTime, default=datetime.datetime.now)
    vin = sa.Column(sa.String, index=True, unique=True)
    model = sa.Column(sa.String, index=True)
    battery_level = sa.Column(sa.Integer, index=True)

    location_id = sa.Column(sa.Integer,
                            sa.ForeignKey('locations.id'),
                            nullable=True)
    location = orm.relation('Location')
