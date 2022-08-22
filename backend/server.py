import json
from urllib import request
from flask import Flask, request, jsonify
import main_predict
from config import *
from flask_cors import CORS, cross_origin


x = "Some variable"
list_selected = []

app = Flask(__name__)
CORS(app, resources={r"*": {"origins": "*"}})

# Route for seeing a data
@app.route('/predictions', methods=["GET"])
def nn_output():

    print("prediction start")
  
    ans = f"symptoms: {list_selected}"
    pred = "\n"

    if len(list_selected)!=0 :
        X_test = symps_to_test(list_selected)
        print("server",X_test)
        predictions = main_predict.main(X_test)
        pred += f"Predictions: {predictions}"
        list_selected.clear()
        return np.ndarray.tolist(predictions[0])

    return []

@app.route('/sys', methods=["GET"])
def symptoms():
    symptoms_list = list_features()
    # symptoms_list = np.ndarray.tolist(features)
    symptoms_list.sort()
    # Enable Access-Control-Allow-Origin
    # symptoms_list.headers.add("Access-Control-Allow-Origin", "*")
    return symptoms_list

@app.route("/diag", methods=["GET","POST"])
def get_syms():
    
    data = jsonify(request.get_json())

    for key, value in data.json.items():
        if key == "selected":
            print(f"SELECTED -- value: {value}")
            list_selected.append(value)
        elif key == "unselected":
            print(f"UNSELECTED -- value: {value}")
            list_selected.remove(value)
            #catch value not found error
    
    return jsonify({"name":"me"})


# Running app
if __name__ == '__main__':
    app.run(debug=True)