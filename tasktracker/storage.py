import sqlite3
from typing import List, Optional
from tasktracker.models import Task

class Storage:
    def __init__(self, db_name: str = ":memory:"):
        self.conn = sqlite3.connect(db_name)
        self._init_db()

    def _init_db(self):
        with self.conn:
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    description TEXT,
                    status TEXT NOT NULL,
                    created_at TEXT NOT NULL
                )
            """)

    def add_task(self, task: Task) -> Task:
        with self.conn:
            cursor = self.conn.execute(
                "INSERT INTO tasks (title, description, status, created_at) VALUES (?, ?, ?, ?)",
                (task.title, task.description, task.status, task.created_at)
            )
            task.id = cursor.lastrowid
        return task

    def get_all_tasks(self) -> List[Task]:
        cursor = self.conn.cursor()
        cursor.execute("SELECT id, title, description, status, created_at FROM tasks")
        rows = cursor.fetchall()
        return [Task(id=row[0], title=row[1], description=row[2], status=row[3], created_at=row[4]) for row in rows]

    def update_task_status(self, task_id: int, status: str) -> bool:
        with self.conn:
            cursor = self.conn.execute("UPDATE tasks SET status = ? WHERE id = ?", (status, task_id))
            return cursor.rowcount > 0

    def delete_task(self, task_id: int) -> bool:
        with self.conn:
            cursor = self.conn.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
            return cursor.rowcount > 0