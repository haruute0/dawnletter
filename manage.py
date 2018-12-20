from app import migrate, manager
from flask_migrate import MigrateCommand
from app import app, db
from app.models import User

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
        email="admin@admin.com",
        confirmed=True
        )
    user.set_uuid()
    user.set_password(
        password="admin"
        )
    user.get_time_stamp()
    user.get_confirmed()
    db.session.add(user)
    db.session.commit()

if __name__ == '__main__':
    manager.run()