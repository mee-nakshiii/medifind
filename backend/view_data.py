import sqlite3

conn = sqlite3.connect("medifind.db")
cur = conn.cursor()

cur.execute("SELECT * FROM pharmacies")

for row in cur.fetchall():
    print(row)

conn.close()