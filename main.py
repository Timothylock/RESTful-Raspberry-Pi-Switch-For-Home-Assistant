from flask import Flask
from flask import request
import json
app = Flask(__name__)

# Variables
isOn = False

# App routes
@app.route("/")
def index():
    return "It Works! Try interacting with /state instead"


@app.route("/state", methods=['GET', 'POST'])
def state():
    if request.method == 'POST':
        return setState()
    elif request.method == "GET":
        return fetchState()

# Helper Functions
def setState():
    c = request.json

    if "active" not in c:
        return "missing \"active\" field", 400

    if c["active"]:
        if turnOn():
            return "turned on", 200
        else:
            return "failed to turn on", 500

    if not c["active"]:
        if turnOff():
            return "turned off", 200
        else:
            return "failed to turn off", 500

    return "Invalid payload", 400

def fetchState():
    return json.dumps({"is_active": isOn}), 200

def turnOn():
    global isOn
    isOn = True

    # Implement this. Return False on any error
    return True

def turnOff():
    global isOn
    isOn = False

    # Implement this. Return False on any error
    return True

if __name__ == "__main__":
    app.run(host="0.0.0.0")
