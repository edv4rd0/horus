from flask import (request, g, jsonify, session, Response)

from horus import app


@app.route('/api/')
def horus_api():
    result = {'code': 200,
              'message': 'Horus Blog API',
              }
    return Response(jsonify(result), status=200, mimetype='application/json')
