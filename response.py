# Serving a Response
from flask import Flask, make_response, request, jsonify

# Create Flask's `app` object
app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello():
    if request.method != 'GET':
        return make_response('Malformed request', 400)
    my_dict = {'Name': 'Bhushan Mandlik', 'Roll No': '306216', 'Branch': 'CSE'}
    return make_response(jsonify(my_dict), 200)     #jsonify() is a helper method provided by Flask to properly return JSON data.