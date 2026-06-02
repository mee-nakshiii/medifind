import sqlite3

connection = sqlite3.connect("medifind.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE medicines (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    generic_name TEXT NOT NULL
)
""")

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

connection.commit()

print("Database created successfully!")

connection.close()