#!/usr/bin/python3
'''A python module'''

if __name__ == '__main__':
    import MySQLdb
    import sys

    db = MySQLdb.connect('localhost', sys.argv[1], sys.argv[2], sys.argv[3])
    cursor = db.cursor()

    if ';' not in sys.argv[4]:
        cmd = "SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY id"
        cursor.execute(cmd, (sys.argv[4],))
        results = cursor.fetchall()
        for i in results:
            print(i)
