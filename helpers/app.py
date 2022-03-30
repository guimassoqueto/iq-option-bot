#! /usr/bin/python3

from pymssql import connect
from datetime import datetime

def insert_result_DB():
    conn = connect('localhost', 'SA', 'gJD2608!', "TESTDB")
    cursor = conn.cursor(as_dict=True)

    cursor.execute('INSERT INTO tblTrades(strActive, numProfitLoss, intTry, dtOperation) VALUES(%s, %d, %d, %s);', ('EURUSD', -100, 3, datetime.now().strftime("%Y%m%d %H:%M")))
    conn.commit()

    conn.close()

  