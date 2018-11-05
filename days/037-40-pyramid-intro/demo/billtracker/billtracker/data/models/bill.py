import datetime
import sqlalchemy
from sqlalchemy import orm
from billtracker.data.modelbase import SqlAlchemyBase


class Bill(SqlAlchemyBase):
    __tablename__ = 'bills'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    created_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now, index=True)
    description = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    paid = sqlalchemy.Column(sqlalchemy.Float, default=0, index=True)
    total = sqlalchemy.Column(sqlalchemy.Float, default=0, index=True)

    # User's relationship
    user_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('users.id'))
    user = orm.relation('User', back_populates='bills')

    @property
    def is_paid(self):
        return self.total <= self.paid
