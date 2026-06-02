from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)


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

    search_term = request.args.get("medicine")

    if not search_term:
        return jsonify({
            "error": "Please provide a medicine name"
        }), 400

    connection = sqlite3.connect("medifind.db")
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT * FROM medicines
        WHERE name LIKE ?
        """,
        ('%' + search_term + '%',)
    )

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


if __name__ == "__main__":
    app.run(debug=True)