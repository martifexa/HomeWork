import sqlite3

name_of_genre = input('Введите жанр')
connection =sqlite3.connect('music_db.sqlite')
cursor = connection.cursor()
result = cursor.execute(f'''
SELECT Title FROM Album
WHERE AlbumId IN (SELECT DISTINCT AlbumId FROM Track
WHERE GenreId = (SELECT GenreId FROM Genre
WHERE name = '{name_of_genre}'))''').fetchall()
print(result)
result1 = []
for i in result:
    result1.append(*i)

print(result1)
artists = cursor.execute(f'''
SELECT ArtistId FROM Album
WHERE AlbumId IN (SELECT DISTINCT AlbumId FROM Track
WHERE GenreId = (SELECT GenreId FROM Genre
WHERE name = '{name_of_genre}'))''').fetchall()
print(artists)
artists1 = []
for i in artists:
    artists1.append(*i)
print(artists1)
lst = sorted([(artists[i], result1[i]) for i in range(0, len(artists))], key=lambda x: (x[0], x[1].lower()))
for elem in lst:
    print(elem[1])