import psycopg2
import logging
import sys


TOKEN = '5185823851:AAFAge_AJJ7uAhys_OIyBUU-fS2YHdfqiIQ'
URL = ''

# Database
HOST = ''
DATABASE = ''
USER = ''
PORT = 5432
PASSWORD = ''
URI = ''

formatter = logging.Formatter('%(asctime)s\t%(levelname)s\t%(filename)s\t%(message)s')
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
handler.setFormatter(formatter)
logger = logging.getLogger('bot')
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)


def pg_connect():
    connection = psycopg2.connect(
        dbname=DATABASE,
        user=USER,
        password=PASSWORD,
        host=HOST,
        port=PORT,
    )
    cursor = connection.cursor()
    return connection, cursor
