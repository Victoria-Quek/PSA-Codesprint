from flask import Flask, jsonify, request
from flask_cors import CORS
import os, ShipYard
from ShipYard import Ship, Container

app = Flask(__name__)
CORS(app)

@app.route('/submit', methods=['POST'])
def submit():
    data = request.getjson()
    ship_schedule = data['ship_schedule']
    ship_schedule = [Ship(ship_schedule[x][0],ship_schedule[x][1]) for x in len(ship_schedule)]

    shipyard = ShipYard(x,y)

    return jsonify(ShipYard.loadingAlgorithm(shipyard,containers))

if __name__ == '__main__':
    print("This is flask for " + os.path.basename(__file__) + ": manage staff ...")
    app.run(host='0.0.0.0', port=5200, debug=True)