from common.db import db

db = db.getDB()

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    question = db.Column(db.String(80), unique=True, nullable=False)
    dataset = db.Column(db.String(120), nullable=False)
    procedures = db.relationship('Procedure', backref='new_question', lazy=True)

class Procedure(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    status = db.Column(db.String(10), nullable=False)
    accurancy = db.Column(db.Float, nullable=True)
    model_path = db.Column(db.String(160), nullable=True)

class Input(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    procedure = db.Column(db.Integer, db.ForeignKey('procedure.id'),
        nullable=False)
    name = db.Column(db.String(160), nullable=False)

class Output(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    procedure = db.Column(db.Integer, db.ForeignKey('procedure.id'),
        nullable=False)
    name = db.Column(db.String(160), nullable=False)
