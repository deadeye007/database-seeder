# customer.py - A Python File Containing the Names Class

import random


def get_new_name():
    with open("names.txt", "r") as file:
        lines = file.readlines()
        lines_end = len(lines)

        # First Name variable
        fn = random.randrange(1, lines_end, 1)

        # Last Name Variable
        ln = random.randrange(1, lines_end, 1)

        # Strip Variables for Readability
        first_name = str.rstrip(lines[fn])
        last_name = str.rstrip(lines[ln])

        # Concatenate names
        name = f'{first_name} {last_name}'

        return str(name)


def get_address():
    with open("streets-names.txt", "r") as file:
        lines = file.readlines()
        lines_end = len(lines)

        # House Number
        hn = random.randrange(0, 9999)

        # Street Name
        sn = random.randrange(1, lines_end, 1)

        # Strip Variables for Readability
        street_name = str.rstrip(lines[hn])

        address = f"{hn} {street_name}"

        return(address)