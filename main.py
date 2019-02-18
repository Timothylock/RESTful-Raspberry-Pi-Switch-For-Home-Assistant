from flask import Flask
from flask import request
app = Flask(__name__)

# Variables
curState = "off"

# App routes
@app.route("/")
def index():
    return "It Works! Try interacting with /states instead"


@app.route("/state", methods=['GET', 'POST'])
def state():
    if request.method == 'POST':
        return setState()
    elif request.method == "GET":
        return fetchState()
    else:
        return "OOPS", 400

# Helper Functions
def setState():
    c = request.json

    if "active" not in c:
        return "missing \"active\" field", 400

    if c["active"] == "true":
        turnOn()
        return "turned on", 200

    if c["active"] == "false":
        turnOff()
        return "turned off", 200

    return "Invalid payload", 400

def fetchState():
    return curState, 200

def turnOn():
    global curState
    curState = "on"

    # Implement this
    pass

def turnOff():
    global curState
    curState = "off"

    # Implement this
    pass

if __name__ == "__main__":
    app.run()