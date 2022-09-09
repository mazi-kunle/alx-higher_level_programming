-- a script that lists all the cities of California that can be found in the database hbtn_0d_usa.

SELECT id, name FROM cities
WHERE cities.id=(SELECT states.id FROM states
WHERE name='california')
ORDER BY cities.id;
