# main.py - Main Function
import customer
import database


def logo():
    print('#'*50)
    print('#\n# Dummy Database Seeder')
    print('# v 0.0.3\n#')
    print('#'*50)


def create_user():
    i = 0
    number = input("How many users do you want created?\n")

    while i != int(number):

        # Pull two seemingly random names out of a very large text file.
        name = customer.get_new_name()
        address = customer.get_address()

        # Print it out to console.
        new_name = name.rsplit(" ")
        first_name = new_name[0]
        last_name = new_name[1]
        user_name = f'{name[0].lower()}{new_name[1].lower()}'
        print(f"First Name: {first_name}")
        print(f"Last Name: {last_name}")
        print(f"Username: {user_name}")
        print(f"Address: {address}")

        print(f" [i] Adding customer to database...")
        result = database.add_customer(first_name, last_name, address)
        print(result)
        i = i + 1


def main():
    logo()

    input("The script will automatically attempt to create the database.")
    database.create_db()

    print("The script will now attempt to create the table.")
    database.create_table()

    # Create customers
    create_user()


main()
