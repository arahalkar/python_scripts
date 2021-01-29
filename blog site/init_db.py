import sqlite3

connection = sqlite3.connect('database.db')

with open('C:\\Users\\araha\\Documents\\Python Scripts\\schema.sql') as f: 
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute(" INSERT INTO posts (title, content) VALUES (?,?)", ('First Post', 'Content for the first post') )

cur.execute(" INSERT INTO posts (title, content) VALUES (?,?)", ('Second Post', 'Content for the second post') )
postings = cur.execute('SELECT * FROM posts').fetchall()
print(postings)
connection.commit()
connection.close()
