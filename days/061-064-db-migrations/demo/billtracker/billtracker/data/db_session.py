import os

import sqlalchemy
import sqlalchemy.orm
from sqlalchemy.orm import Session

from billtracker.data.modelbase import SqlAlchemyBase
# noinspection PyUnresolvedReferences
from billtracker.data.__all_models import *


class DbSession:
    factory = None
    engine = None
    db_folder = None

    @staticmethod
    def global_init(db_file: str):

        if DbSession.factory:
            return

        if not db_file or not db_file.strip():
            raise Exception("You must specify a data file.")

        DbSession.db_folder = os.path.dirname(db_file)

        conn_str = 'sqlite:///' + db_file
        print("Connecting to DB at: {}".format(conn_str))

        engine = sqlalchemy.create_engine(conn_str, echo=False)
        DbSession.engine = engine
        DbSession.factory = sqlalchemy.orm.sessionmaker(bind=engine)

        SqlAlchemyBase.metadata.create_all(engine)

    @staticmethod
    def create_session() -> Session:
        return DbSession.factory()
