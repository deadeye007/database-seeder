# names.py - A Python File Containing the Names Class

import random


def get_new_name():
    with open("names.txt", "r") as file:
        lines = file.readlines()
        lines_end = len(lines)
        fn = random.randrange(1, lines_end, 1)
        ln = random.randrange(1, lines_end, 1)
        first_name = str.rstrip(lines[fn])
        last_name = str.rstrip(lines[ln])
        name = f'{first_name} {last_name}'
        return str(name)


