import uuid
from app.to_do_app.daos import task_item_dao
from app.to_do_app.models import TaskItem
from app import db


class TaskItemService:
    def update_task(self, task_id: str, data: dict):
        task = task_item_dao.get_by_task_id(task_id)
        if (task):
            is_completed = data.get('is_completed')
            title = data.get('title')
            description = data.get('description')
            if title:
                task.title = title
            if is_completed:
                task.is_completed = is_completed
            if description:
                task.description = description
            db.session.commit()
            return True, task
        else:
            return False, 'TASK_DOES_NOT_EXIST'

    def create_task(self, data: dict):
        if (data.get('name')):
            task = TaskItem(
                id=str(uuid.uuid4()),
                title=data['title'],
                description=data.get('description')
            )
            db.session.add(task)
            db.session.commit()
            return True, task
        else:
            return False, 'TASK_NAME_REQUIRED'

    def delete_task(self, task_id):
        task = task_item_dao.get_by_task_id(task_id)
        if (task):
            task.is_deleted = True
            db.session.commit()
            return 'TASK_DELETED'
        else:
            return 'TASK_DOESNOT_EXIST'


task_item_service = TaskItemService()
