from tasktracker.storage import Storage
from tasktracker.service import TaskService
from tasktracker.cli import run_cli

def main():
    storage = Storage("tasks.db")
    service = TaskService(storage)
    run_cli(service)

if __name__ == "__main__":
    main()