from flask import Blueprint, jsonify
todo_app = Blueprint('todo_v1', __name__, url_prefix='/')


@todo_app.route('/health-check', methods=['GET'])
def health_check():
    return jsonify(
        message='Service working'
    )
