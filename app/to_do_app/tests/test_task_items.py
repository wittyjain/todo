import unittest
from app.to_do_app.daos import task_item_dao
from app.to_do_app.services import task_item_service


class TestTaskItems(unittest.TestCase):

    task = {
        "title": "Task 1",
        "description": "Completing Task 1"
    }


    def test_get_by_task_id_blank(self):
        task_details = task_item_dao.get_by_task_id("a-1234")
        self.assertEqual(task_details, None)

    def test_create_task(self):
        status, task = task_item_service.create_task(self.task)
        self.assertEqual(status, True)

    def test_get_all_task(self):
        tasks = task_item_dao.get_all()
        assert tasks != []
