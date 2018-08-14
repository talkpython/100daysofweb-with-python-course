import datetime
import sys

import import_data
from data import session_factory
from data.models.users import User
from infrastructure.numbers import try_int
from infrastructure.switchlang import switch
from services import data_service

user: User = None


def main():
    setup_db()

    options = 'Enter a command, [r]ent, [a]vailable, [l]ocate, [h]istory, e[X]it: '
    cmd = "NOT SET"

    while cmd:
        cmd = input(options).lower().strip()
        with switch(cmd) as s:
            s.case('r', rent_a_scooter)
            s.case('a', find_available_scooters)
            s.case('l', locate_our_scooters)
            s.case('h', my_history)
            s.case(['x', ''], exit_app)
            s.default(lambda: print(f"Don't know what to do with {cmd}."))


def setup_db():
    global user
    session_factory.global_init('hover_share.sqlite')
    session_factory.create_tables()
    import_data.import_if_empty()
    user = data_service.get_default_user()


def rent_a_scooter():
    print("********* Rent a scooter ********* ")
    scooters = find_available_scooters(True)
    chose_it = try_int(input('Which one do you want? ')) - 1

    if not (0 <= chose_it or chose_it < len(scooters)):
        print("Error: Pick another number.")
        return

    scooter = scooters[chose_it]

    data_service.book_scooter(scooter, user, datetime.datetime.now())


def find_available_scooters(suppress_header=False):
    if not suppress_header:
        print("********* Available scooters: ********* ")

    parked_scooters = data_service.parked_scooters()
    for idx, s in enumerate(parked_scooters, start=1):
        print(f"#{idx}. Loc: {s.location.street} {s.location.city}, "
              f"{s.id} {s.model} VIN: {s.vin} with battery level {s.battery_level}%")

    print()
    return parked_scooters


def locate_our_scooters():
    print("********* Current location of our scooters ********* ")
    rented_scooters = data_service.rented_scooters()
    parked_scooters = data_service.parked_scooters()

    print(f"Out with clients [{len(rented_scooters)} scooters]:")
    for s in rented_scooters:
        print(f" {s.id} {s.model} VIN: {s.vin} with battery level {s.battery_level}%")

    print()

    print(f"Parked [{len(parked_scooters)} scooters]:")
    for s in parked_scooters:
        print(f"Loc: {s.location.street} {s.location.city}, "
              f"{s.id} {s.model} VIN: {s.vin} with battery level {s.battery_level}%")


def my_history():
    print('********* Your rental history ********* ')
    user_local = data_service.get_default_user()
    for r in user_local.rentals:
        print(f" * {r.start_time.date().isoformat()} {r.scooter.model}")


def exit_app():
    print("")
    print("Bye!")
    sys.exit(0)


if __name__ == '__main__':
    main()
