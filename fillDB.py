import sqlite3
import pandas as pd
con = sqlite3.connect("db.sqlite3")
books_data_url = f"https://www.googleapis.com/drive/v3/files/1TQY4BV6h8nVDcMd8EvzL3M_TU4K5RXvn?alt=media&key=AIzaSyAYoL3_dwzxfmdYcNrTmaux8umwwdxYyfM"

cur = con.cursor()
cur.execute("""DROP TABLE IF EXISTS books""")
cur.execute("""CREATE TABLE IF NOT EXISTS books (`title` VARCHAR(100), `ISBN` VARCHAR(24), `author` VARCHAR(64),`description` VARCHAR(3600), `link` VARCHAR(300))""")

df = pd.read_json(books_data_url)

for data in df['books']:
    book_id = data['id']
    book_author = data['author']
    book_title = data['title']
    book_description = data['description']
    book_link = data['link']
    cur.execute("""INSERT INTO books VALUES (?,?,?,?,?)""", (book_title, book_id, book_author, book_description,book_link))

con.commit()