#!/usr/bin/python3
""" Script: lists all states with a name starting with N """
import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) == 4:
        conn = MySQLdb.connect(
                host="localhost",
                port=3306,
                user=sys.argv[1],
                passwd=sys.argv[2],
                db=sys.argv[3],
                charset="utf8")
        cur = conn.cursor()
        cur.execute(
                "SELECT *\
                        FROM states\
                        WHERE BINARY states.name\
                        LIKE 'N%'\
                        ORDER BY states.id ASC")
        query_rows = cur.fetchall()
        for row in query_rows:
            print(row)
        cur.close()
        conn.close()
    else:
        print("Usage: USER, PASSWD, DB_NAME")
