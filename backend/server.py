import json
from urllib import request
from flask import Flask, request, jsonify
from main import *
from config import *
from flask_cors import CORS, cross_origin


x = "Some variable"
list = []

app = Flask(__name__)
CORS(app, resources={r"*": {"origins": "*"}})

# Route for seeing a data
@app.route('/predictions')
def nn_output():
    print("prediction start")
    # return main()
    return "Predictions here"

@app.route('/sys', methods=["GET"])
def symptoms():
    symptoms_list = np.ndarray.tolist(features)
    symptoms_list.sort()
    # Enable Access-Control-Allow-Origin
    # symptoms_list.headers.add("Access-Control-Allow-Origin", "*")
    return symptoms_list

@app.route("/diag", methods=["GET","POST"])
def get_syms():
    
    data = jsonify(request.get_json())

    list.append(data.data)
    print(list)
    return jsonify({"name":"me"})

# Running app
if __name__ == '__main__':
    app.run(debug=True)