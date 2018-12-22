from app import manager
from app import app, db
from config import Config

import unittest
import coverage

import os

@manager.command
def test():
    """Runs the unit tests without coverage."""
    tests = unittest.TestLoader().discover('tests')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    else:
        return 1

@manager.command
def cov():

    print ('Running Test and Coverage Test...')

    print ('Running Database Setup...')

    db.initialize_db_conn(Config.POSTGRES_ADMIN_URI)

    print ('Creating user and database...')
    
    res = db.run_script_init(os.path.join(Config.ADMIN_SQL_DIR, 'init_test_database.sql'))
    if not res:
        raise Exception('Falied to create new database and user Exit code: %i' % res)

    db.initialize_db_conn(Config.SQLALCHEMY_TEST_DATABASE_URI)

    print ('Creating tables...')
    db.run_script(os.path.join(Config.ADMIN_SQL_DIR, 'init_table.sql'))

    print ('Creating primary keys...')
    db.run_script(os.path.join(Config.ADMIN_SQL_DIR, 'init_primary_keys.sql'))

    print('Task init_test_db done')

    print ('Running Test...')
    
    cov = coverage.coverage(branch=True, include='app/*')
    cov.start()
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
    cov.stop()
    cov.save()
    
    print ('Deleting tables...')
    db.run_script(os.path.join(Config.ADMIN_SQL_DIR, 'drop_table.sql'))

    db.initialize_db_conn(Config.POSTGRES_ADMIN_URI)

    print ('Deleting user and database...')
    
    res = db.run_script_init(os.path.join(Config.ADMIN_SQL_DIR, 'drop_test_database.sql'))
    if not res:
        raise Exception('Falied to delete database and user Exit code: %i' % res)


    print('Coverage Summary:')
    cov.report()
    cov.html_report()

@manager.command
def init_user_db():
    db.initialize_db_conn(Config.POSTGRES_ADMIN_URI)

    print ('Creating user and database...')
    
    res = db.run_script_init(os.path.join(Config.ADMIN_SQL_DIR, 'init_database.sql'))
    if not res:
        raise Exception('Falied to create new database and user Exit code: %i' % res)

@manager.command
def init_db():
    db.initialize_db_conn(Config.SQLALCHEMY_DATABASE_URI)

    print ('Creating tables...')
    db.run_script(os.path.join(Config.ADMIN_SQL_DIR, 'init_table.sql'))

    print ('Creating primary keys...')
    db.run_script(os.path.join(Config.ADMIN_SQL_DIR, 'init_primary_keys.sql'))

    print('Task init_db done')

if __name__ == '__main__':
    manager.run()