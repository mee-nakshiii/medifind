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

# Sample Medicines
medicines = [
    ("Paracetamol", "Acetaminophen"),
    ("Crocin", "Paracetamol"),
    ("Dolo 650", "Paracetamol"),
    ("Augmentin 625", "Amoxicillin"),
    ("Azithromycin", "Azithromycin")
]

cursor.executemany(
    "INSERT INTO medicines(name, generic_name) VALUES (?, ?)",
    medicines
)

# Sample Pharmacies
pharmacies = [
    ("ABC Medicals", "Thrissur", 10.5276, 76.2144),
    ("City Pharmacy", "Thrissur", 10.5310, 76.2180),
    ("Apollo Medicals", "Thrissur", 10.5245, 76.2200)
]

cursor.executemany(
    """
    INSERT INTO pharmacies(name, address, latitude, longitude)
    VALUES (?, ?, ?, ?)
    """,
    pharmacies
)

# Sample Inventory
inventory = [
    (1, 1, 50),   # ABC Medicals -> Paracetamol
    (2, 1, 20),   # City Pharmacy -> Paracetamol
    (3, 4, 15),   # Apollo -> Augmentin
    (1, 3, 30)    # ABC -> Dolo 650
]

cursor.executemany(
    """
    INSERT INTO inventory(pharmacy_id, medicine_id, stock)
    VALUES (?, ?, ?)
    """,
    inventory
)

connection.commit()

print("Database created successfully!")

connection.close()