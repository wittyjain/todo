

from app.to_do_app.models import TaskItem
from app import db
session = db.session


class TaskItemDAO:
    def __init__(self, model):
        self.model = model

    def get_all(self):
        return session.query(self.model).filter(is_deleted=False).all()

    def get_by_task_id(self, task_id: str):
        return (
            session.query(self.model).
            filter_by(id=task_id, is_deleted=False).first()
        )


task_item_dao = TaskItemDAO(TaskItem)
