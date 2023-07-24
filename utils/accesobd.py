
from flask import g
from flask_mysqldb import MySQL


def get_bd():
    if 'db' not in g:
        g.db=MySQL()
    return g.db

def actualizarbd(sql, result= None):
    try:
        db = get_bd()
        cur = db.connection.cursor()
        if result:
            cur.execute(sql, result)
        else:
            cur.execute(sql)
            
        db.connection.commit()
        cur.close()
    except Exception as e:
        raise e
    
def consultarbd(sql):
    try:
        db = get_bd()
        cur = db.connection.cursor()
        cur.execute(sql)
        result = cur.fetchall()
        cur.close()
        return result
    except Exception as e:
        raise e