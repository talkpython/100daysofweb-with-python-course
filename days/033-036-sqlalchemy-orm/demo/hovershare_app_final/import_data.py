import datetime
import random

from data import session_factory
from data.models.locations import Location
from data.models.rentals import Rental
from data.models.scooters import Scooter
from data.models.users import User
from services import data_service


def import_if_empty():
    __import_locations()
    __import_scooters()
    __import_users()
    __import_rentals()


def __import_scooters():
    session = session_factory.create_session()
    if session.query(Scooter).count() > 0:
        return

    models = [
        'Hover-1 1st edition',
        'Hover-1 Sport 1st edition',
        'Hover-1 Touring 1st edition',
        'Hover-1 2nd edition',
        'Hover-1 Sport 2nd edition',
        'Hover-1 Touring 2nd edition',
        'Hover-1 3rd edition',
        'Hover-1 Sport 3rd edition',
        'Hover-1 Touring 3rd edition',
    ]

    vin_values = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    locations = list(session.query(Location).all())

    COUNT = 21
    for _ in range(0, COUNT):
        s = Scooter()
        s.model = random.choice(models)
        s.battery_level = 100
        s.vin = ''.join((random.choice(vin_values) for _ in range(0, 18)))
        s.location = random.choice(locations)
        session.add(s)

    session.commit()


def __import_users():
    session = session_factory.create_session()
    if session.query(User).count() > 0:
        return

    data_service.get_default_user()

    user2 = User()
    user2.email = 'user2@talkpython.fm'
    user2.name = 'user 2'
    session.add(user2)
    session.commit()


def __import_locations():
    session = session_factory.create_session()
    if session.query(Location).count() > 0:
        return

    location = Location()
    location.street = '123 Main St.'
    location.state = 'OR'
    location.city = 'Portland'
    location.max_storage = random.randint(10, 20)
    session.add(location)

    location = Location()
    location.street = '700 Terwilliger Blvd'
    location.state = 'OR'
    location.city = 'Portland'
    location.max_storage = random.randint(10, 20)
    session.add(location)

    location = Location()
    location.street = '600 Broadway'
    location.state = 'OR'
    location.city = 'Portland'
    location.max_storage = random.randint(10, 20)
    session.add(location)

    session.commit()


def __import_rentals():
    session = session_factory.create_session()
    if session.query(Rental).count() > 0:
        return

    scooters = list(session.query(Scooter))
    locations = list(session.query(Location))
    user = data_service.get_default_user()
    user2 = session.query(User).filter(User.email == 'user2@talkpython.fm').one()

    for _ in range(1, 5):
        selected = random.choice(scooters)
        data_service.book_scooter(
            scooter=selected,
            user=user,
            start_date=datetime.datetime.now() - datetime.timedelta(days=random.randint(1, 100))
        )
        scooters.remove(selected)
        data_service.park_scooter(selected.id, random.choice(locations).id)

    for _ in range(1, 10):
        selected = random.choice(scooters)
        data_service.book_scooter(
            scooter=selected,
            user=user2,
            start_date=datetime.datetime.now() - datetime.timedelta(days=random.randint(1, 100))
        )
        scooters.remove(selected)
