#!/usr/bin/python3
'''A python module'''

if __name__ == '__main__':
    import MySQLdb
    import sys

    db = MySQLdb.connect('localhost', sys.argv[1], sys.argv[2], sys.argv[3])
    cursor = db.cursor()
    cmd = "SELECT * FROM states WHERE name  = BINARY '{}' ORDER BY id".format(
                                                                sys.argv[4])
    cursor.execute(cmd)
    results = cursor.fetchall()
    for i in results:
        print(i)
