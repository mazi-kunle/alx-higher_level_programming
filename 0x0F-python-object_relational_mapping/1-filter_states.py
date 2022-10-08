#!/usr/bin/python3
'''This is a module'''

if __name__ == '__main__':

    import MySQLdb
    import sys

    db = MySQLdb.connect('localhost', port=3306, sys.argv[1],
                         sys.argv[2], sys.argv[3])
    cursor = db.cursor()
    cursor.execute('''SELECT * FROM states WHERE name
                   LIKE BINARY "N%" ORDER BY id''')
    for i in cursor.fetchall():
        print(i)
