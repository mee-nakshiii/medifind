import sqlite3

connection = sqlite3.connect("medifind.db")
cursor = connection.cursor()

cursor.execute("""
SELECT
    pharmacies.name,
    pharmacies.address,
    inventory.stock
FROM inventory
JOIN medicines
    ON inventory.medicine_id = medicines.id
JOIN pharmacies
    ON inventory.pharmacy_id = pharmacies.id
WHERE medicines.name = 'Paracetamol'
""")

results = cursor.fetchall()

for row in results:
    print(row)

connection.close()