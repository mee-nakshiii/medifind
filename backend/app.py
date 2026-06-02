from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "MediFind Backend Running!"

@app.route("/api/search")
def search_medicine():
    medicine = request.args.get("medicine")

    sample_results = [
        {
            "pharmacy": "ABC Medicals",
            "distance": "1.2 km",
            "stock": 25
        },
        {
            "pharmacy": "City Pharmacy",
            "distance": "2.4 km",
            "stock": 10
        }
    ]

    return jsonify({
        "medicine": medicine,
        "results": sample_results
    })

if __name__ == "__main__":
    app.run(debug=True)