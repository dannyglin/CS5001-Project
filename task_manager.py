import datetime

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task, priority, due_date_str):
        due_date = datetime.datetime.strptime(due_date_str, "%m-%d-%Y %H:%M")
        self.tasks.append({"task": task, "priority": priority, "due_date": due_date})

    def remove_task(self, index):
        del self.tasks[index]

    def get_tasks(self):
        return self.tasks
