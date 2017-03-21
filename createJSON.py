import sqlite3
from config import *



#TODO: die letzten n messungen
def queryDBLimit(col, value, limit):
    DBconn = sqlite3.connect(SQL_DB)
    # This enables column access by name: row['column_name']
    DBconn.row_factory = sqlite3.Row
    queryCurs = DBconn.cursor()

    # queryCurs.execute('SELECT * FROM {SQLtable} WHERE {SQLcol}={SQLvalue} ORDER BY timestamp DESC LIMIT {SQLlimit}'. \
    #                   format(SQLtable=table, SQLcol=col, SQLvalue=value, SQLlimit=limit))


    queryCurs.execute('SELECT MAX(timestamp) AS timestamp, originAddr, unit, id, value FROM messwerte WHERE {SQLcol}={SQLvalue} GROUP BY unit'. \
                        format(SQLcol=col, SQLvalue=value, SQLlimit=limit))

    queryCurs.execute(
        'SELECT MAX(timestamp) AS timestamp, originAddr, unit,unit_name,id, value FROM messwerte INNER JOIN einheiten ON messwerte.unit = einheiten.unit_id WHERE {SQLcol}={SQLvalue} GROUP BY unit'. \
        format(SQLcol=col, SQLvalue=value, SQLlimit=limit))

    row = queryCurs.fetchall()
    row_json = [ dict(rec) for rec in row ]

    DBconn.close()
    return row_json

def queryDB_id(id):
    DBconn = sqlite3.connect(SQL_DB)
    # This enables column access by name: row['column_name']
    DBconn.row_factory = sqlite3.Row
    queryCurs = DBconn.cursor()
    queryCurs.execute('SELECT * FROM messwerte where id=?', (id,))

    row = queryCurs.fetchall()
    row_json = [ dict(rec) for rec in row ]

    DBconn.close()
    return row_json

def queryDBallStation():
    DBconn = sqlite3.connect(SQL_DB)
    # This enables column access by name: row['column_name']
    DBconn.row_factory = sqlite3.Row
    queryCurs = DBconn.cursor()

    queryCurs.execute('SELECT originAddr, name , location, powerSaving FROM messwerte INNER JOIN stationen ON stationen.station_id = messwerte.originAddr GROUP BY originAddr')

    row = queryCurs.fetchall()
    row_json = [ dict(rec) for rec in row ]

    DBconn.close()
    return row_json
