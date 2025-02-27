import unittest
from task_manage.task import Task
from task_manage.task_manager import TaskManager

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.manager = TaskManager()

    def test_add_task(self):
        self.manager.add_task("hikkermi hikkermi", "hikkermi hikkermi")
        self.assertEqual(len(self.manager.tasks), 1)
        self.assertEqual(self.manager.tasks[1].title, "hikkermi hikkermi")

    def test_update_task(self):
        self.manager.add_task("hikkermi hikkermi", "hikkermi hikkermi")
        self.manager.update_task(1, "выполнено")
        self.assertEqual(self.manager.tasks[1].status, "выполнено")

    def test_delete_task(self):
        self.manager.add_task("hikkermi hikkermi", "hikkermi hikkermi")
        self.manager.delete_task(1)
        self.assertEqual(len(self.manager.tasks), 0)

if __name__ == "__main__":
    unittest.main()