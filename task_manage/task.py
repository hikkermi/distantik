from datetime import datetime

class Task:
    def __init__(self, task_id, title, description, status="не выполнено", due_date=None, priority="низкий"):
        self.id = task_id
        self.title = title
        self.description = description
        self.status = status
        self.due_date = due_date
        self.priority = priority

    def __str__(self):
        return (f"ID: {self.id}, Title: {self.title}, Description: {self.description}, "
                f"Status: {self.status}, Due Date: {self.due_date}, Priority: {self.priority}")