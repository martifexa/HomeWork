import sqlite3

connection = sqlite3.connect('films.sqlite')
cursor = connection.cursor()

result = cursor.execute('''
SELECT title FROM films 
WHERE genre = 4 AND year BETWEEN 1995 AND 2000
''')

for i in result:
    print(*i)