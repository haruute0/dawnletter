from app import migrate, manager
from flask_migrate import MigrateCommand
from app import app, db
from app.models import User
from config import Config

import unittest
import coverage

manager.add_command('db', MigrateCommand)

@manager.command
def create_db():
    db.create_all()

@manager.command
def drop_db():
    db.drop_all()

@manager.command
def create_admin():
    user = User(
        username="admin",
        email="admin@admin.com"
        )
    user.set_uuid()
    user.set_password(
        password="admin"
        )
    user.get_time_stamp()
    user.get_confirmed()
    db.session.add(user)
    db.session.commit()

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
    """Runs the unit tests with coverage."""
    cov = coverage.coverage(branch=True, include='app/*')
    cov.start()
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
    cov.stop()
    cov.save()
    print('Coverage Summary:')
    cov.report()
    cov.html_report()

if __name__ == '__main__':
    manager.run()