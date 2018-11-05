import json
import os
import random
from typing import List

import dateutil.parser
from sqlalchemy.orm import Session

from billtracker.data.db_session import DbSession
from billtracker.data.models.bill import Bill
from billtracker.data.models.users import User


def load_starter_data():
    print("Loading starter data...")
    session = DbSession.create_session()
    if session.query(Bill).count() > 0:
        session.close()
        print("Data already loaded...")
        return

    session.expire_on_commit = False

    users = add_users(session)
    add_bills(users)

    session.commit()
    session.close()


def add_users(session: Session) -> List[User]:
    users = []
    data_file = os.path.join(DbSession.db_folder, 'MOCK_USERS.json')
    with open(data_file, 'r', encoding='utf-8') as fin:
        data = json.load(fin)

    for u in data:
        user = User()
        users.append(user)
        user.email = u.get('email')
        user.name = u.get('name')
        user.created_date = dateutil.parser.parse(u.get('created_date'))
        user.last_login = dateutil.parser.parse(u.get('last_login'))
        user.last_login = dateutil.parser.parse(u.get('last_login'))
        user.hashed_password = u.get('hashed_password')
        session.add(user)

    return users


def add_bills(users: List[User]):
    data_file = os.path.join(DbSession.db_folder, 'MOCK_PAYMENTS.json')
    with open(data_file, 'r', encoding='utf-8') as fin:
        data = json.load(fin)

    for p in data:
        user = random.choice(users)

        bill = Bill()
        bill.created_date = dateutil.parser.parse(p.get('created_date'))
        bill.description = p.get('description')
        bill.total = int(p.get('total'))
        bill.paid = min(bill.total, int(p.get('paid')))

        user.bills.append(bill)
