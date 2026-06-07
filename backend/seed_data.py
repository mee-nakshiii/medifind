import sqlite3
import random

connection = sqlite3.connect("medifind.db")
cursor = connection.cursor()

# -----------------------------
# Medicines
# -----------------------------

medicines = [

    ("Paracetamol", "Acetaminophen"),
    ("Dolo 650", "Acetaminophen"),
    ("Crocin", "Acetaminophen"),
    ("Azithromycin", "Azithromycin"),
    ("Amoxicillin", "Amoxicillin"),
    ("Augmentin 625", "Amoxicillin + Clavulanate"),
    ("Cetirizine", "Cetirizine"),
    ("Levocetirizine", "Levocetirizine"),
    ("Pantoprazole", "Pantoprazole"),
    ("Omeprazole", "Omeprazole"),
    ("Metformin", "Metformin"),
    ("Glimepiride", "Glimepiride"),
    ("Aspirin", "Aspirin"),
    ("Ibuprofen", "Ibuprofen"),
    ("Diclofenac", "Diclofenac"),
    ("ORS", "Oral Rehydration Salts"),
    ("Insulin", "Insulin"),
    ("Vitamin D3", "Cholecalciferol"),
    ("Zincovit", "Multivitamin"),
    ("Benadryl", "Diphenhydramine"),
    ("Allegra", "Fexofenadine"),
    ("Montair", "Montelukast"),
    ("Atorvastatin", "Atorvastatin"),
    ("Rosuvastatin", "Rosuvastatin"),
    ("Amlodipine", "Amlodipine"),
    ("Telmisartan", "Telmisartan"),
    ("Losartan", "Losartan"),
    ("Rantac", "Ranitidine"),
    ("Norflox", "Norfloxacin"),
    ("Ciplox", "Ciprofloxacin")

]

# -----------------------------
# Pharmacies
# -----------------------------

pharmacies = [

    ("ABC Medicals", "Thrissur", 10.5276, 76.2144),
    ("City Pharmacy", "Thrissur", 10.5310, 76.2180),
    ("Apollo Pharmacy", "Thrissur", 10.5345, 76.2200),
    ("Care Medicals", "Thrissur", 10.5200, 76.2100),
    ("MediPlus", "Thrissur", 10.5400, 76.2250),
    ("Health Hub", "Thrissur", 10.5230, 76.2170),
    ("WellCare Pharmacy", "Thrissur", 10.5290, 76.2280),
    ("Life Medicals", "Thrissur", 10.5360, 76.2130),
    ("Trust Pharmacy", "Thrissur", 10.5190, 76.2220),
    ("Green Cross Medicals", "Thrissur", 10.5410, 76.2190)

]

# -----------------------------
# Insert Medicines
# -----------------------------

for medicine in medicines:

    cursor.execute(
        """
        INSERT INTO medicines(name, generic_name)
        VALUES (?, ?)
        """,
        medicine
    )

# -----------------------------
# Insert Pharmacies
# -----------------------------

for pharmacy in pharmacies:

    cursor.execute(
        """
        INSERT INTO pharmacies(
            name,
            address,
            latitude,
            longitude
        )
        VALUES (?, ?, ?, ?)
        """,
        pharmacy
    )

connection.commit()

# -----------------------------
# Create Inventory
# -----------------------------

cursor.execute("SELECT id FROM medicines")
medicine_ids = cursor.fetchall()

cursor.execute("SELECT id FROM pharmacies")
pharmacy_ids = cursor.fetchall()

for pharmacy in pharmacy_ids:

    for medicine in medicine_ids:

        stock = random.randint(0, 100)

        cursor.execute(
            """
            INSERT INTO inventory(
                pharmacy_id,
                medicine_id,
                stock
            )
            VALUES (?, ?, ?)
            """,
            (
                pharmacy[0],
                medicine[0],
                stock
            )
        )

connection.commit()

connection.close()

print("Database seeded successfully!")