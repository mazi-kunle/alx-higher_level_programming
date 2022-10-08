#!/usr/bin/python3
'''A python module'''

if __name__ == '__main__':
    import MySQLdb
    import sys

    db = MySQLdb.connect('localhost', sys.argv[1], sys.argv[2], sys.argv[3])
    cursor = db.cursor()

    cmd = '''SELECT name FROM cities
             WHERE state_id = (SELECT id FROM states
             WHERE name = %s)'''
    cursor.execute(cmd, (sys.argv[4],))
    results = cursor.fetchall()
    flag = 0
    for i in results:
        if (flag == 1):
            print(', ', end='')
        flag = 1
        print(i[0], end='')
    print()
