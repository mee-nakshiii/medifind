import sqlite3

connection = sqlite3.connect("medifind.db")
cursor = connection.cursor()

cursor.execute("PRAGMA table_info(medicines)")
print("MEDICINES")
for row in cursor.fetchall():
    print(row)

print("\nPHARMACIES")
cursor.execute("PRAGMA table_info(pharmacies)")
for row in cursor.fetchall():
    print(row)

print("\nINVENTORY")
cursor.execute("PRAGMA table_info(inventory)")
for row in cursor.fetchall():
    print(row)

connection.close()