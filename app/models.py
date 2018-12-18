from app import db

class post(db.Model):
    __tablename__ = 'post'

    id = db.Column(db.Integer, primary_key=True)
    post = db.Column(db.String())

    def __init__(self, post):
        self.post = post

    def __repr__(self):
        return '<id {}>'.format(self.id)