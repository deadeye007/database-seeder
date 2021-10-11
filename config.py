import configparser

# Read configuration globally.
config = configparser.ConfigParser()

try:
    config.read('settings.cfg')

except FileNotFoundError:
    print(" [E] Create 'settings.cfg' from settings.cfg.example and try again.")


def server():
    return config['mysql']['server']


def name():
    return config['mysql']['db']


def user():
    return config['mysql']['user']


def password():
    return config['mysql']['passwd']
