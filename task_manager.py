import datetime


class TaskManager:
    """
    A class to manage tasks in a to-do list application.
    """

    def __init__(self):
        """
        Initializes a TaskManager object with an empty list to store tasks.
        """
        self.tasks = []

    def add_task(self, task, priority, due_date_str):
        """
        Adds a new task to the task list with the given details.

        Arguments:
        task (str): The description of the task.
        priority (int): The priority level of the task (between 1 and 5).
        due_date_str (str): The due date of the task in the format "MM-DD-YYYY HH:MM".
        """
        due_date = datetime.datetime.strptime(due_date_str, "%m-%d-%Y %H:%M")
        self.tasks.append(
            {"task": task, "priority": priority, "due_date": due_date})

    def remove_task_by_index(self, index):
        """
        Removes a task from the task list based on the provided index.

        Arguments:
        index (int): The index of the task to be removed from the task list.
        """
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
        else:
            print(f"Invalid index '{index}' for task removal.")

    def get_tasks(self):
        """
        Retrieves the list of tasks stored in the TaskManager.

        Arguments:
        None
        """
        return self.tasks
