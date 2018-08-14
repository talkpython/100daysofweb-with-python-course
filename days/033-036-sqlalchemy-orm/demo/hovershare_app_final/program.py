import datetime
import sys
from typing import List
from infrastructure.numbers import try_int
from infrastructure.switchlang import switch


user = None


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
    pass
    # todo setup the setup_db
    # 1. initialize the connection / engine
    # 2. create the tables
    # 3. import data
    # 4. set default user


def rent_a_scooter():
    print("********* Rent a scooter ********* ")
    scooters = find_available_scooters(True)
    chose_it = try_int(input('Which one do you want? ')) - 1

    if not (0 <= chose_it or chose_it < len(scooters)):
        print("Error: Pick another number.")
        return

    scooter = scooters[chose_it]
    # todo show book scooter


def find_available_scooters(suppress_header=False):
    if not suppress_header:
        print("********* Available scooters: ********* ")

    parked_scooters = []
    # todo show parked scooters
    print()
    return parked_scooters


def locate_our_scooters():
    print("********* Current location of our scooters ********* ")
    rented_scooters = []
    parked_scooters = []

    print(f"Out with clients [{len(rented_scooters)} scooters]:")
    # todo show rented scooters

    print()

    print(f"Parked [{len(parked_scooters)} scooters]:")
    # todo show parked scooters


def my_history():
    print('********* Your rental history ********* ')
    # todo show rentals


def exit_app():
    print("")
    print("Bye!")
    sys.exit(0)


if __name__ == '__main__':
    main()
