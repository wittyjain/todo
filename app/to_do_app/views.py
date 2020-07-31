from flask import jsonify, request
from flask.views import MethodView
from app.to_do_app.daos import task_item_dao
from app.to_do_app.services import task_item_service
from app.to_do_app.task_serialiser import TaskItemSchema
from app.auth import authorize


class TaskItem(MethodView):
    @authorize
    def get(self, task_id):
        if (not task_id):
            schema = TaskItemSchema(many=True)
            result = schema.dump(task_item_dao.get_all())
            print(result)
            return jsonify(
                data=result,
                message="All tasks were fetched"
            )
        else:
            schema = TaskItemSchema()
            result = schema.dump(task_item_dao.get_by_task_id(task_id))
            return jsonify(
                data=result,
                message="Single task info was fetched"
            )

    @authorize
    def post(self):
        data = request.get_json()
        status, data = task_item_service.create_task(data)
        if status:
            schema = TaskItemSchema()
            result = schema.dump(data)
            return jsonify(
                data=result,
                message='Task successfully created'
            ), 201
        else:
            return jsonify(
                code=data,
                message='Task creation failed'
            ), 400

    @authorize
    def put(self, task_id):
        data = request.get_json()
        status, data = task_item_service.update_task(task_id, data)
        if (status):
            schema = TaskItemSchema()
            result = schema.dump(data)
            return jsonify(
                data=result,
                message='Task successfully updated'
            ), 201
        else:
            return jsonify(
                code=data,
                message='Task updation failed'
            ), 400

    @authorize
    def delete(self, task_id):
        status = task_item_service.delete_task(task_id)
        if (status == 'TASK_DELETED'):
            return jsonify(
                message='Task succesfully deleted'
            )
        else:
            return jsonify(
                code=status,
                message='Task doesnot exist'
            )
