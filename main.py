# main.py - Main Function
import customer

def logo():
    print('#'*50)
    print('#\n# Dummy Database Seeder')
    print('# v 0.0.0\n#')
    print('#'*50)


def main():
    logo()
    print("\nThis operation will attempt to create a new dummy entry for a\
        database.")

    # Pull two seemingly random names out of a very large text file.
    name = customer.get_new_name()
    address = customer.get_address()

    # Print it out to console.
    new_name = name.rsplit(" ")
    first_name = new_name[0]
    last_name = new_name[1]
    user_name = f'{name[0].lower()}{new_name[1].lower()}'
    print(f'First Name: {first_name}')
    print(f'Last Name: {last_name}')
    print(f'Username: {user_name}')
    print(f'Address: {address}')


main()
