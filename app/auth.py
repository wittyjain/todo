from functools import wraps
from flask import abort, request
from config import API_TOKEN


def authorize(f):
    @wraps(f)
    def decorated_function(*args, **kws):
        if 'Authorization' not in request.headers:
            print("Not authorised")
            abort(401)
        token = request.headers['Authorization']
        if token != API_TOKEN:
            abort(401)

        return f(*args, **kws)
    return decorated_function
