#!/usr/bin/python3
'''
This is a module.
'''
if __name__ == '__main__':

    import sys
    import MySQLdb

    # open database connection
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    # prepare cursor
    cursor = db.cursor()

    cursor.execute('SELECT * FROM states ORDER BY id')
    results = cursor.fetchall()
    for i in results:
        print(i)
