from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from project_awesome import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=False, nullable=False)

    def __repr__(self):
        return 'User {}'.format(self.username)
