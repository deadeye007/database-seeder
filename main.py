# main.py - Main Function
import database
import users


def logo():
    print('#'*50)
    print('#\n# Dummy Database Seeder')
    print('# v 0.0.3\n#')
    print('#'*50)
    print('Script will attempt to create and fill database with random info.\n')


def main():
    logo()

    # Create database and tables.
    database.create_db()
    database.create_table()

    # Create customers.
    users.create()


main()
