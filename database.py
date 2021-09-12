import configparser
import mysql.connector


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

        result = f"Customer added to database with id {r_id}."

        return result
