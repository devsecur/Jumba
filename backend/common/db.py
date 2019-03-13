import os
import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def connect_db(app=current_app):
    con = sqlite3.connect(
        app.config['DATABASE'],
        detect_types=sqlite3.PARSE_DECLTYPES
    )

    con.row_factory = dict_factory

    return con

def get_db(app=current_app):
    if not os.path.isfile(app.config['DATABASE']):
        init_db()
    if 'db' not in g:
        g.db = connect_db()
    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()


def init_db(app=current_app):
    if not os.path.isfile(app.config['DATABASE']):
        db = connect_db(app)

        with current_app.open_resource('boot/schema.sql') as f:
            db.executescript(f.read().decode('utf8'))
    else:
        db = connect_db(app)

    return db

def init_app(app=current_app):
    app.teardown_appcontext(close_db)
    with app.app_context():
        db = init_db(app)

def query_db(query, arguments=()):
    database = get_db()
    cur = database.cursor()
    print(query)
    print(arguments)
    cur = cur.execute(query, arguments)
    database.commit()

    return cur
