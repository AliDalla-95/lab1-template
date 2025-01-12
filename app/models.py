from . import db

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer)
    address = db.Column(db.String(200))
    work = db.Column(db.String(100))