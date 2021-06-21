# names.py - A Python File Containing the Names Class

import random


class Creator:

    def __init__(self):
        print('Names Class')

    def get_name(self):
        with open("names.txt", "r") as file:
            lines = file.readlines()
            lines_end = len(lines)
            fn = random.randrange(1, lines_end, 1)
            ln = random.randrange(1, lines_end, 1)
            first_name = str.rstrip(lines[fn])
            last_name = str.rstrip(lines[ln])
            print(f'{first_name} {last_name}')
