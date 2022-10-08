#!/usr/bin/python3
'''A python module'''

if __name__ == '__main__':
    import MySQLdb
    import sys

    db = MySQLdb.connect('localhost', sys.argv[1], sys.argv[2], sys.argv[3])
    cursor = db.cursor()
    cursor.execute('SELECT * FROM states WHERE name = %s ORDER BY id',
                   (sys.argv[4],))
    for i in cursor.fetchall():
        print(i)
