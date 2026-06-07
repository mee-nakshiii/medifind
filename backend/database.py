import sqlite3

connection = sqlite3.connect("medifind.db")

cursor = connection.cursor()

# Medicines Table
cursor.execute("""
CREATE TABLE medicines (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    generic_name TEXT NOT NULL
)
""")

# Pharmacies Table
cursor.execute("""
CREATE TABLE pharmacies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    address TEXT NOT NULL,
    latitude REAL,
    longitude REAL
)
""")

# Inventory Table
cursor.execute("""
CREATE TABLE inventory (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    pharmacy_id INTEGER,
    medicine_id INTEGER,
    stock INTEGER,
    FOREIGN KEY(pharmacy_id) REFERENCES pharmacies(id),
    FOREIGN KEY(medicine_id) REFERENCES medicines(id)
)
""")

connection.commit()

print("Database created successfully!")

connection.close()