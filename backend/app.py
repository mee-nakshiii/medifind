from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3

app = Flask(__name__)

CORS(app)


@app.route("/")
def home():
    return "MediFind Backend Running!"


@app.route("/api/medicines")
def get_medicines():

    connection = sqlite3.connect("medifind.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM medicines")

    medicines = cursor.fetchall()

    connection.close()

    result = []

    for medicine in medicines:
        result.append({
            "id": medicine[0],
            "name": medicine[1],
            "generic_name": medicine[2]
        })

    return jsonify(result)


@app.route("/api/search")
def search_medicine():

    medicine_name = request.args.get("medicine")

    if not medicine_name:
        return jsonify({
            "error": "Please provide a medicine name"
        }), 400

    connection = sqlite3.connect("medifind.db")
    cursor = connection.cursor()

    cursor.execute("""
    SELECT
    pharmacies.name,
    pharmacies.address,
    pharmacies.latitude,
    pharmacies.longitude,
    inventory.stock
    FROM inventory
    JOIN medicines
        ON inventory.medicine_id = medicines.id
    JOIN pharmacies
        ON inventory.pharmacy_id = pharmacies.id
    WHERE medicines.name LIKE ?
    """, ('%' + medicine_name + '%',))

    results = cursor.fetchall()

    connection.close()

    pharmacies = []

    for row in results:
        pharmacies.append({
       "pharmacy": row[0],
       "address": row[1],
       "latitude": row[2],
       "longitude": row[3],
       "stock": row[4]
       }) 
        
    return jsonify(pharmacies)


if __name__ == "__main__":
    app.run(debug=True)