from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/week/<id>")
@app.route("/week/")
def weekly_data(id="68109ee4-d724-4589-aca4-c3f2c03af754"):
    some_data = {
        "app_name": "OmahaAPI",
        "player_data": {
            "name": "Peyton Manning",
            "id": id,
            "position": "QB",
            "week": "1",
            "year": "1999",
            "team": "IND"
        }
    }

    return jsonify(some_data)

@app.route("/")
def hello():
    some_data = {
        "app_name": "OmahaAPI",
        "message": "Welcome to OmahaAPI!"
    }
    return jsonify(some_data)