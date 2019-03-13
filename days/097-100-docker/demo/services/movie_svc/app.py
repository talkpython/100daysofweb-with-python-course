# noinspection PyUnresolvedReferences
from app_instance import api
from routes import *
from data import db

db.global_init()


api.run(port=7007, address="0.0.0.0")
