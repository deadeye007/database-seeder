# main.py - Main Function
import database
import users


def logo():
    print('#'*50)
    print('#\n# Dummy Database Seeder')
    print('# v 0.0.3\n#')
    print('#'*50)


def main():
    logo()

    input(" [i] The script will automatically attempt to create the database.")
    database.create_db()

    print(" [i] The script will now attempt to create the table.")
    database.create_table()

    # Create customers
    users.create()


main()
