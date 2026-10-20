from typing import List
from tasktracker.models import Task
from tasktracker.storage import Storage
from tasktracker.validators import validate_task_title, validate_status

class TaskService:
    def __init__(self, storage: Storage):
        self.storage = storage

    def create_task(self, title: str, description: str = "") -> Task:
        clean_title = validate_task_title(title)
        task = Task(id=None, title=clean_title, description=description)
        return self.storage.add_task(task)

    def list_tasks(self) -> List[Task]:
        return self.storage.get_all_tasks()

    def mark_completed(self, task_id: int) -> bool:
        return self.storage.update_task_status(task_id, "COMPLETED")

    def remove_task(self, task_id: int) -> bool:
        return self.storage.delete_task(task_id)