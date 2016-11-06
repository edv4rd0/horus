from flask import (request, g, jsonify, session, make_response)

from horus import app


@app.route('/api/', methods=["GET"])
def horus_api():
    result = {'code': 200,
              'message': 'Horus Blog API',
              }
    rv = make_response((jsonify(result), 200))
    rv.mimetype='application/json'
    return rv


@app.route('/api/post/<slug>', methods=["GET", "DELETE", "PUT"])
def horus_post(slug):
    """Get existing post, DELETE existing post, update existing post"""
    return 200

@app.route('/api/post', methods=["POST"])
def horus_post_create():
    return 200


@app.route('/api/posts/', methods=["GET"])
def horus_get_posts():
    posts = jsonify([dict(title='Initial Post')])
    rv = make_response((posts, 200))
    rv.mimetype='application/json'
    return rv
