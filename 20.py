import sqlite3

connection = sqlite3.connect('films.sqlite')
cursor = connection.cursor()

result = cursor.execute('''
SELECT title FROM films 
WHERE title LIKE '%Астерикс%' AND title not LIKE '%Обеликс%'
''')

for i in result:
    print(*i)