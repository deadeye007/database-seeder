# main.py - Main Function
import argparse
import sys
import database
# import users


def logo():
    print('#'*50)
    print('#\n# Dummy Database Seeder and Feeder')
    print('#')
    print('# Version 0.0.4\n#')
    print('#'*50)
    print()


class MainOptions(object):

    def __init__(self):
        parser = argparse.ArgumentParser(
            description='Interact directly with the test database.',
            prog='coolname'
        )

        parser.add_argument('command', help='Subcommand to run.')
        # Limit the length of parse_args to prevent validation issues
        args = parser.parse_args(sys.argv[1:2])
        if not hasattr(self, args.command):
            print("Unrecognized Command")
            parser.print_help()
            exit(1)

        getattr(self, args.command)()

    def install(self):
        # TODO: Add the ability to install components individually.
        parser = argparse.ArgumentParser(
            description='Attempts to install the database and tables.')
        args = parser.parse_args(sys.argv[2:])
        print("Running the installer.")
        # database.create_db()
        # database.create_table()

    def find(self):
        parser = argparse.ArgumentParser(
            description='Interact directly with the database.')
        parser.add_argument('--customer')
        parser.add_argument('--employee')
        parser.add_argument('--item')
        args = parser.parse_args(sys.argv[2:4])

        if args.customer:
            print("Searching for customer: %s" % args.customer)
            employee = False
            database.find_user(employee, args.customer)

        if args.employee:
            print("Searching for employee: %s" % args.employee)
            employee = True
            database.find_user(employee, args.employee)

        if args.item:
            print("Searching for item: %s" % args.item)

    def add(self):
        # TODO: Flesh out the different variables
        parser = argparse.ArgumentParser(
            description='Add to the database.')
        parser.add_argument('--customer')
        parser.add_argument('--employee')
        parser.add_argument('--item')
        args = parser.parse_args(sys.argv[2:4])

        if args.customer:
            print("Adding customer: %s" % args.customer)
            employee = False
            database.find_user(employee, args.customer)

        if args.employee:
            print("Adding employee: %s" % args.employee)
            employee = True
            database.find_user(employee, args.employee)

        if args.item:
            print("Adding item: %s" % args.item)

    def delete(self):
        parser = argparse.ArgumentParser(
            description='Add to the database.')
        parser.add_argument('--customer')
        parser.add_argument('--employee')
        parser.add_argument('--item')
        args = parser.parse_args(sys.argv[2:4])
        print("This will delete something.")

        if args.customer:
            print("Deleting customer: %s" % args.customer)
            employee = False
            database.find_user(employee, args.customer)

        if args.employee:
            print("Deleting employee: %s" % args.employee)
            employee = True
            database.find_user(employee, args.employee)

        if args.item:
            print("Deleting item: %s" % args.item)

    # TODO: Flesh out the employee aspects.
    # TODO: Add ability to seed random items.


if __name__ == "__main__":
    MainOptions()
