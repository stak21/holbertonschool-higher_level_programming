#!/usr/bin/python3
""" Script: lists all cities  """
import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) == 5:
        state_name = sys.argv[4]
        cmd = "SELECT cities.name\
                FROM states \
                JOIN cities on cities.state_id = states.id\
                WHERE states.name = %s\
                ORDER BY cities.id ASC;"
        conn = MySQLdb.connect(
                host="localhost",
                port=3306,
                user=sys.argv[1],
                passwd=sys.argv[2],
                db=sys.argv[3],
                charset="utf8")
        cur = conn.cursor()
        cur.execute(cmd, (state_name,))
        query_rows = cur.fetchall()
        if (query_rows):
            for row in query_rows[0:-1]:
                print(row[0], end=', ')
            print(query_rows[-1][0])
        cur.close()
        conn.close()
    else:
        print("Usage: USER, PASSWD, DB_NAME Search")
