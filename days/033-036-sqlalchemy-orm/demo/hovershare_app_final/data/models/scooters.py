import datetime

import sqlalchemy as sa

from data.sqlalchemybase import SqlAlchemyBase


class Scooter(SqlAlchemyBase):
    __tablename__ = 'scooters'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    created_date = sa.Column(sa.DateTime, default=datetime.datetime.now)
    vin = sa.Column(sa.String, index=True, unique=True)
    model = sa.Column(sa.String, index=True)
    battery_level = sa.Column(sa.Integer, index=True)

    # TODO: Relationships
