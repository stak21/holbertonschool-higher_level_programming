#!/usr/bin/python3
""" Script: lists all cities  """
import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) == 4:
        cmd = "SELECT cities.id, cities.name, states.name\
                FROM states \
                JOIN cities on cities.state_id = states.id;"
        conn = MySQLdb.connect(
                host="localhost",
                port=3306,
                user=sys.argv[1],
                passwd=sys.argv[2],
                db=sys.argv[3],
                charset="utf8")
        cur = conn.cursor()
        cur.execute(cmd)
        query_rows = cur.fetchall()
        for row in query_rows:
            print(row)
        cur.close()
        conn.close()
    else:
        print("Usage: USER, PASSWD, DB_NAME")
