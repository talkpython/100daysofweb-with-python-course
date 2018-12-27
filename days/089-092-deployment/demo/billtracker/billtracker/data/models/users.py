import datetime
from typing import List

import sqlalchemy
from sqlalchemy import orm
from billtracker.data.modelbase import SqlAlchemyBase
from billtracker.data.models.bill import Bill


class User(SqlAlchemyBase):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    email = sqlalchemy.Column(sqlalchemy.String, index=True, nullable=True)
    hashed_password = sqlalchemy.Column(sqlalchemy.String, nullable=True, index=True)
    created_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now, index=True)
    last_login = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now, index=True)

    # noinspection PyUnresolvedReferences
    bills = orm.relation("Bill", order_by=Bill.created_date.desc(), back_populates='user')

    @property
    def paid_bills(self) -> List[Bill]:
        return [b for b in self.bills if b.paid >= b.total]

    @property
    def open_bills(self) -> List[Bill]:
        return [b for b in self.bills if b.paid < b.total]

    @property
    def total_owed(self) -> float:
        return sum(b.total - b.paid for b in self.open_bills)

    @property
    def total_paid_off(self) -> float:
        return sum(b.total for b in self.paid_bills)
