from flask import jsonify
from flask.views import MethodView
from app.to_do_app.models import TaskItem


class TaskList(MethodView):
    def get(self, task_id):
        if (not task_id):
            return jsonify(
                message="All tasks were fetched"
            )
        else:
            return jsonify(
                message="Single task info was fetched"
            )
