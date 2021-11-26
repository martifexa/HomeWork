import sqlite3

connection = sqlite3.connect('films.sqlite')
cursor = connection.cursor()


result2 = cursor.execute('''
SELECT title FROM films
WHERE duration <= 85
''')

for i in result2:
    print(*i)

