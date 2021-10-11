import config
import mysql.connector

try:
    cnx = mysql.connector.connect(host=config.server(),
                                  user=config.user(),
                                  password=config.password(),
                                  database=config.name()
                                  )
except mysql.connector.errors.ProgrammingError as e:
    if "1049" in str(e):
        cnx = mysql.connector.connect(host=config.server(),
                                      user=config.user(),
                                      password=config.password()
                                      )

cursor = cnx.cursor()


def create_db():

    input(" [i] The script will automatically attempt to create the database.")

    try:
        create_database = f"CREATE DATABASE IF NOT EXISTS `{config.name()}`"

        cursor.execute(create_database)

    except ConnectionError:
        print(" [E] Something went wrong!")

    except mysql.connector.errors.ProgrammingError as e:
        if "1064" in str(e):
            print(f" [E] Check your SQL syntax and try again.")
            exit()


def create_table():
    # Use the proper database.
    use_database = f"USE `{config.name()}`"

    # Define tables in SQL Syntax.
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

    input(" [i] The script will now attempt to create the tables.")

    try:
        cursor.execute(use_database)
        print(" [i] Creating customer table.")
        cursor.execute(customer_tab)
        print("     [!] Created customer table.")

        print(" [i] Creating item table.")
        cursor.execute(item_tab)
        print("     [!] Created item table.")

        print(" [i] Creating employee table.")
        cursor.execute(employee_tab)
        print("     [!] Created employee table.")

    except mysql.connector.errors.ProgrammingError as e:
        if "1064" in str(e):
            print(f"\n [E] Check your SQL syntax and try again.")
            exit()


def add_customer(first_name, last_name, address):
    # Use the proper database.
    use_database = f"USE `{config.name()}`"

    # Define customers in SQL Syntax.
    add_record = ("INSERT INTO `customers` "
                  "(first_name,"
                  "last_name,"
                  "street_address,"
                  "city,"
                  "state,"
                  "country)"
                  "VALUES (%s, %s, %s, %s, %s, %s)")

    record_data = (first_name, last_name, address, 'Anytown', 'AW', 'USA')

    try:
        cursor.execute(use_database)
        cursor.execute(add_record, record_data)

        r_id = cursor.lastrowid

        result = f"     [i] Customer added to database with id {str(r_id)}."

        return result

    except mysql.connector.errors.ProgrammingError as e:
        if "1064" in str(e):
            print(f"\n [E] Check your SQL syntax and try again.")
            exit()


def find_customer():
    # TODO: Add the ability to find customers
    print(" [i] Attempting to find customer.")
