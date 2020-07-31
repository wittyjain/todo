# Module to fetch all TaskItem model Entity

from app.to_do_app.models import TaskItem
from app import db
session = db.session


class TaskItemDAO:
    def __init__(self, model):
        self.model = model

    def get_all(self):
        """
            Method fetches all the un deleted tasks
        """
        # TODO: Add support for fetching based on filter
        return session.query(self.model).filter_by(is_deleted=False).all()

    def get_by_task_id(self, task_id: str):
        """
            Method fetches task by id assigned while creating
        """
        return (
            session.query(self.model).
            filter_by(id=task_id, is_deleted=False).first()
        )


task_item_dao = TaskItemDAO(TaskItem)
