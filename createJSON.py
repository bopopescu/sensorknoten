import sqlite3

#Constants
SQL_DB = 'node1.db'
SQL_TABLE = 'messwerte'

#TODO: die letzten n messungen
def queryDBLimit(col, value, limit):
    DBconn = sqlite3.connect(SQL_DB)
    # This enables column access by name: row['column_name']
    DBconn.row_factory = sqlite3.Row
    queryCurs = DBconn.cursor()

    # queryCurs.execute('SELECT * FROM {SQLtable} WHERE {SQLcol}={SQLvalue} ORDER BY timestamp DESC LIMIT {SQLlimit}'. \
    #                   format(SQLtable=table, SQLcol=col, SQLvalue=value, SQLlimit=limit))


    for i in range(0,limit,1):
        queryCurs.execute('SELECT MAX(timestamp)-{SQLlimit}, originAddr, unit, id, value FROM {SQLtable} WHERE {SQLcol}={SQLvalue} GROUP BY unit'. \
                        format(SQLtable=SQL_TABLE, SQLcol=col, SQLvalue=value, SQLlimit=limit))

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

    queryCurs.execute('SELECT originAddr FROM {SQLtable} GROUP BY originAddr'. \
                      format(SQLtable=SQL_TABLE))

    row = queryCurs.fetchall()
    row_json = [ dict(rec) for rec in row ]

    DBconn.close()
    return row_json
