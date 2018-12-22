import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.pool import NullPool
import time
import psycopg2

from config import Config

SCHEMA_VERSION = 5

engine = None

DUMP_DEFAULT_THREAD_COUNT = 4

def initialize_db_conn(conn_url):

    global engine

    while True:
        try:
            engine = create_engine(conn_url, poolclass=NullPool)
            print("Database connection estabilished!") 
            break
        except psycopg2.OperationalError as e:
            print("Database connection couldn't estabilished.")
            print("Error: {}".format(str(e)))
            print("Trying in 2 seconds ...")
            time.sleep(5) 

def run_script(sql_script_path):

    with open(sql_script_path) as sql:
        with engine.connect() as connection:
            connection.execute(sql.read())
            
def run_script_init(sql_script_path):

    with open(sql_script_path) as sql:
        connection = engine.connect()
        connection.connection.set_isolation_level(0)
        lines = sql.read().splitlines()
        try:
            for line in lines:
                connection.execute(line)
        except sqlalchemy.exc.ProgrammingError as e:
            print("Error: {}".format(e))
            return False
        finally:
            connection.connection.set_isolation_level(1)
            connection.close()
        return True
        