from .task import Task  

class TaskManager:
    def __init__(self):
        self.tasks = {}
        self.next_id = 1

    def add_task(self, title, description, due_date=None, priority="низкий"):
        if not title:
            raise ValueError("Название задачи не может быть пустым.")
        task = Task(self.next_id, title, description, due_date=due_date, priority=priority)
        self.tasks[self.next_id] = task
        self.next_id += 1

    def get_all_tasks(self):
        return list(self.tasks.values())

    def update_task(self, task_id, status):
        if task_id in self.tasks:
            self.tasks[task_id].status = status
        else:
            raise ValueError("Задача с таким ID не найдена.")

    def delete_task(self, task_id):
        if task_id in self.tasks:
            del self.tasks[task_id]
        else:
            raise ValueError("Задача с таким ID не найдена.")

    def search_tasks(self, keyword):
        return [task for task in self.tasks.values() if keyword in task.title or keyword in task.description]

    def filter_tasks_by_status(self, status):
        return [task for task in self.tasks.values() if task.status == status]