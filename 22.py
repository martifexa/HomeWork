import sqlite3

connection = sqlite3.connect('films.sqlite')
cursor = connection.cursor()


result2 = cursor.execute('''
SELECT title FROM genres
WHERE id in (SELECT genre FROM films WHERE year IN(2010,2011))
''')

for i in result2:
    print(*i)