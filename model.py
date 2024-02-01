from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()


user_sequences = db.Table('user_sequences',
                          db.Column('seqanalysis_id', db.Integer, db.ForeignKey('seqanalysis.id')),
                          db.Column('user_id', db.Integer, db.ForeignKey('user.id'))
                          )


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    email = db.Column(db.String(40), nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)
    user_data = db.relationship('Userdata', backref='User')
    sequences = db.relationship('Seqanalysis', secondary=user_sequences, backref='users')


class Userdata(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(40), nullable=False)
    surname = db.Column(db.String(40), nullable=False)
    institution = db.Column(db.String(40), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


class Seqanalysis(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    uniprot = db.Column(db.String(10), nullable=False)
    sequence = db.Column(db.String, nullable=False)
    mol_weight = db.Column(db.Float, nullable=False)
