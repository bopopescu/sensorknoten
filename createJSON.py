import sqlite3
import json
import sys

def queryDB(table, col, value, limit):
    DBconn = sqlite3.connect('node1.db')
    # This enables column access by name: row['column_name']
    DBconn.row_factory = sqlite3.Row
    queryCurs = DBconn.cursor()

    queryCurs.execute('SELECT * FROM {SQLtable} WHERE {SQLcol}={SQLvalue} ORDER BY timestamp DESC LIMIT {SQLlimit}'. \
                      format(SQLtable=table, SQLcol=col, SQLvalue=value, SQLlimit=limit))

    row = queryCurs.fetchall()
    row_json = [ dict(rec) for rec in row ]

    DBconn.close()
    return row_json

#SELECT MAX(timestamp),originAddr, unit, id, value from messwerte WHERE originAddr = 400 GROUP BY unit