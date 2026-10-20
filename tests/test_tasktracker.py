import pytest
from tasktracker.storage import Storage
from tasktracker.service import TaskService
from tasktracker.validators import ValidationError

def test_create_task_success():
    storage = Storage(":memory:")
    service = TaskService(storage)
    task = service.create_task("Belajar DevSecOps", "Integrasi SAST")
    assert task.id == 1
    assert task.title == "Belajar DevSecOps"

def test_create_task_empty_title():
    storage = Storage(":memory:")
    service = TaskService(storage)
    with pytest.raises(ValidationError):
        service.create_task("   ")