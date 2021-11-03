# main.py - Main Function
import database
import users


def logo():
    print('#'*50)
    print('#\n# Dummy Database Seeder')
    print('# v 0.0.4\n#')
    print('#'*50)
    print()


def main():
    logo()

    # Create database and tables.
    database.create_db()
    database.create_table()

    # Create customers.
    users.create()

    database.find_random_customer()
    last = database.last_customer()

    print(f"There are currently {last} customers in the database.")


main()
