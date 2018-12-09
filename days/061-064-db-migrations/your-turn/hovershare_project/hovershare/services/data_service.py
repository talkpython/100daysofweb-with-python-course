import datetime
import random
from typing import List

from data import session_factory
from data.models.rentals import Rental
from data.models.scooters import Scooter
from data.models.users import User


def get_default_user():
    session = session_factory.create_session()

    user = session.query(User).filter(User.email == 'test@talkpython.fm').first()
    if user:
        return user

    user = User()
    user.email = 'test@talkpython.fm'
    user.name = 'Test user 1'
    session.add(user)

    session.commit()

    return user


def book_scooter(scooter: Scooter, user: User, start_date: datetime.datetime) -> Rental:
    session = session_factory.create_session()

    scooter = session.query(Scooter).filter(Scooter.id == scooter.id).one()
    scooter.location_id = None
    scooter.battery_level = random.randint(50, 100)

    rental = Rental()
    rental.scooter_id = scooter.id
    rental.user_id = user.id
    rental.start_time = start_date
    rental.end_time = rental.start_time + datetime.timedelta(days=1)

    session.add(rental)
    session.commit()

    return rental


def park_scooter(scooter_id: int, location_id: int) -> Scooter:
    session = session_factory.create_session()

    scooter = session.query(Scooter).filter(Scooter.id == scooter_id).one()
    scooter.location_id = location_id
    scooter.battery_level = 100

    session.commit()

    return scooter


def rented_scooters() -> List[Scooter]:
    session = session_factory.create_session()

    # noinspection PyComparisonWithNone
    scooters = session.query(Scooter).filter(Scooter.location_id == None).all()

    return list(scooters)


def parked_scooters() -> List[Scooter]:
    session = session_factory.create_session()

    # noinspection PyComparisonWithNone
    scooters = session.query(Scooter).filter(Scooter.location_id != None).all()

    return list(scooters)
