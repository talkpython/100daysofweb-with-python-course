from typing import Optional

from sqlalchemy.orm import subqueryload

from billtracker.data.db_session import DbSession
from billtracker.data.models.users import User
from billtracker.data.models.bill import Bill


def get_user_by_id(user_id: int, include_bills=True) -> Optional[User]:
    session = DbSession.create_session()
    try:
        if not include_bills:
            return session.query(User).filter(User.id == user_id).first()
        else:
            return session.query(User) \
                .options(subqueryload(User.bills)) \
                .filter(User.id == user_id) \
                .first()
    finally:
        session.close()


def get_bill_by_id(bill_id: int) -> Optional[Bill]:
    session = DbSession.create_session()
    try:
        return session.query(Bill) \
            .filter(Bill.id == bill_id) \
            .first()
    finally:
        session.close()


def add_payment(amount: float, bill_id: int) -> Optional[Bill]:
    session = DbSession.create_session()
    session.expire_on_commit = False

    try:
        bill = session.query(Bill) \
            .filter(Bill.id == bill_id) \
            .first()

        if not bill:
            return None

        bill.paid += amount
        session.commit()

        return bill
    finally:
        session.close()
