import sqlite3
conn = sqlite3.connect("my1.db")
c = conn.cursor()
c.execute("CREATE TABLE friends (fist_name TEXT, last_name TEXT, closeness INTEGER);")
conn.commit()
conn.close()


