#!/usr/bin/python3
'''A python module'''

if __name__ == '__main__':
    import MySQLdb
    import sys

    db = MySQLdb.connect('localhost', sys.argv[1], sys.argv[2], sys.argv[3])
    cursor = db.cursor()

    cmd = '''SELECT c.id, c.name, s.name FROM cities AS c
             INNER JOIN states AS s
             ON s.id = c.state_id
             ORDER BY c.id'''
    cursor.execute(cmd)
    results = cursor.fetchall()
    for i in results:
        print(i)
