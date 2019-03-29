#!/usr/bin/python3
""" Script: lists all states with a name that matches the name argument """
import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) == 5:
        search = sys.argv[4]
        cmd = "SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC;"
        conn = MySQLdb.connect(
                host="localhost",
                port=3306,
                user=sys.argv[1],
                passwd=sys.argv[2],
                db=sys.argv[3],
                charset="utf8")
        cur = conn.cursor()
        cur.execute(cmd, (search,))
        query_rows = cur.fetchall()
        for row in query_rows:
            print(row)
        cur.close()
        conn.close()
    else:
        print("Usage: USER PASSWORD DB_NAME SEARCH")
