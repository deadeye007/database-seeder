import configparser
import mysql.connector


def create_db():
    # Create the customer database.
    config = configparser.ConfigParser()
    try:
        config.read('settings.cfg')

    except FileNotFoundError:
        print(" [E] Create 'settings.cfg' and try again.")

    else:
        cnx = mysql.connector.connect(host=config['mysql']['server'],
                                      user=config['mysql']['user'],
                                      password=config['mysql']['passwd']
                                      )
        cursor = cnx.cursor()

        try:
            create_database = f"CREATE DATABASE `{config['mysql']['db']}`"

            cursor.execute(create_database)

        except ConnectionError:
            print(" [E] Something went wrong!")

        except mysql.connector.errors.ProgrammingError as e:
            if e == 42000:
                print(f"Error: {e}")
                print(" [E] You need to do better, programmatically in SQL.")
        except mysql.connector.errors.DatabaseError:
            pass


def create_table():
    config = configparser.ConfigParser()
    try:
        config.read('settings.cfg')

    except FileNotFoundError:
        print(" [E] Create 'settings.cfg' and try again.")

    else:
        cnx = mysql.connector.connect(host=config['mysql']['server'],
                                      user=config['mysql']['user'],
                                      password=config['mysql']['passwd'],
                                      database=config['mysql']['db']
                                      )
        cursor = cnx.cursor()

        customer_tab = (f"CREATE TABLE IF NOT EXISTS `customers`"
                        "(customer_id MEDIUMINT AUTO_INCREMENT,"
                        "first_name VARCHAR(20) NOT NULL,"
                        "last_name VARCHAR(20) NOT NULL,"
                        "street_address VARCHAR(100) NOT NULL,"
                        "city VARCHAR(20) NOT NULL,"
                        "state VARCHAR(20) NOT NULL,"
                        "country VARCHAR(20) NOT NULL,"
                        "phone_number VARCHAR(20),"
                        "PRIMARY KEY (customer_id))")

        item_tab = (f"CREATE TABLE IF NOT EXISTS `item`"
                    "(item_sku MEDIUMINT NOT NULL,"
                    "name VARCHAR(20) NOT NULL,"
                    "description VARCHAR(100) NOT NULL,"
                    "price DECIMAL(5,2) UNSIGNED NOT NULL,"
                    "quantity SMALLINT UNSIGNED,"
                    "PRIMARY KEY (item_sku))")

        employee_tab = (f"CREATE TABLE IF NOT EXISTS `employees`"
                        "(employee_id MEDIUMINT NOT NULL,"
                        "first_name VARCHAR(20) NOT NULL,"
                        "last_name VARCHAR(20) NOT NULL,"
                        "street_address VARCHAR(100) NOT NULL,"
                        "city VARCHAR(20) NOT NULL,"
                        "state VARCHAR(20) NOT NULL,"
                        "country VARCHAR(20) NOT NULL,"
                        "phone_number VARCHAR(20) NOT NULL,"
                        "work_region VARCHAR(20) NOT NULL,"
                        "PRIMARY KEY (employee_id))")

        try:
            print(" [i] Creating customer table.")
            cursor.execute(customer_tab)
            print(" [!] Created customer table.")

            print(" [i] Creating item table.")
            cursor.execute(item_tab)
            print(" [!] Created item table.")

            print(" [i] Creating employee table.")
            cursor.execute(employee_tab)
            print(" [!] Created employee table.")

        except mysql.connector.errors.ProgrammingError as e:
            if "42000" in str(e):
                print(f" [E] Check your SQL syntax and try again.")
                exit()
            else:
                print(f" [E] Something went wrong!\nError Number: {e}\n\n")
                exit()


def add_customer(fn, ln, addy):
    config = configparser.ConfigParser()

    try:
        config.read('settings.cfg')

    except FileNotFoundError:
        print(" [E] Create 'settings.cfg' and try again.")

    else:
        cnx = mysql.connector.connect(host=config['mysql']['server'],
                                      user=config['mysql']['user'],
                                      password=config['mysql']['passwd'],
                                      database=config['mysql']['db']
                                      )
        cursor = cnx.cursor()

        add_record = ("INSERT INTO `customers` "
                      "(first_name,"
                      "last_name,"
                      "street_address,"
                      "city,"
                      "state,"
                      "country)"
                      "VALUES (%s, %s, %s, %s, %s, %s)")

        record_data = (fn, ln, addy, 'Anytown', 'AW', 'USA')

        cursor.execute(add_record, record_data)
        cnx.commit()

        r_id = cursor.lastrowid

        result = f" [i] Customer added to database with id {str(r_id)}."

        return result


def find_customer():
    # TODO: Add the ability to find customers
    print("Attempting to find customer")
