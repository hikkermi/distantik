import sqlite3
from task_manage.task import Task

class Database:
    def __init__(self, db_name="tasks.db"):
        self.connection = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        with self.connection:
            self.connection.execute("""
                CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY,
                    title TEXT NOT NULL,
                    description TEXT,
                    status TEXT NOT NULL
                )
            """)

    def save_task(self, task):
        with self.connection:
            self.connection.execute("INSERT INTO tasks (title, description, status) VALUES (?, ?, ?)",
                                    (task.title, task.description, task.status))

    def load_tasks(self):
        with self.connection:
            cursor = self.connection.execute("SELECT * FROM tasks")
            return [Task(row[0], row[1], row[2], row[3]) for row in cursor.fetchall()]

    def close(self):
        self.connection.close()