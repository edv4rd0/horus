from flask import (Flask, request, g, jsonify, session)

app = Flask(__name__)



@app.route('/api/')
def horus_api():
    result = {"code": 200,
              "message": "Horus Blog API",
              }
    return jsonify(result), 200
