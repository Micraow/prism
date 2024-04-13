import sqlite3
from flask import g
import os
import api
current_file_dir = os.path.dirname(__file__)

DATABASE = current_file_dir + '/database.db'

app = api.app


def init_db(db):
    '''
    检测如果数据库为空，则初始化数据库，ID是必须的，从1递增

    TYPE： LIVE或PIC或CUOTI

    ORI：当TYPE为LIVE或PIC时保存原文

    RES：当TYPE为LIVE或PIC时保存译文
    
    PATH：当TYPE为CUOTI时保存图片路径

    '''
    c = db.cursor()
    empty = False
    try:
        c.execute("SELECT * FROM PRISM")
    except sqlite3.OperationalError:
        empty = True

    if empty is True:
        c.execute('''CREATE TABLE PRISM
        (ID INT PRIMARY KEY  NOT NULL,
        TYPE           TEXT    NOT NULL,
        ORI            TEXT     ,
        RES            TEXT,
        PATH           TEXT);''')


def get_db():
    db = getattr(g, '_database', None)

    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db = init_db(db)

    return db


def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
