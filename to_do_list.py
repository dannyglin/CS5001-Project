import tkinter as tk
from tkinter import ttk, messagebox
import datetime

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task, priority, due_date_str):
        """
        Add a task to the task list.

        Args:
        - task: The task description (string).
        - priority: The priority of the task (integer).
        - due_date_str: Due date of the task in the format "YYYY-MM-DD HH:MM" (string).
        """
        due_date = datetime.datetime.strptime(due_date_str, "%Y-%m-%d %H:%M")
        self.tasks.append({"task": task, "priority": priority, "due_date": due_date})

    def remove_task(self, index):
        """
        Remove a task from the task list.

        Args:
        - index: Index of the task to be removed (integer).
        """
        del self.tasks[index]

    def get_tasks(self):
        """
        Get the list of tasks.

        Returns:
        - List of tasks.
        """
        return self.tasks

def update_task_list():
    """
    Update the task list display.
    """
    tree.delete(*tree.get_children())
    tasks = task_manager.get_tasks()
    if tasks:
        for i, task in enumerate(tasks, start=1):
            tree.insert("", tk.END, values=(task['task'], '*' * task['priority'], task['due_date'].strftime("%Y-%m-%d %H:%M")))
    else:
        tree.insert("", tk.END, values=("No tasks in your to-do list.", "", ""))

def add_task():
    """
    Function to add a task.
    """
    task = entry_task.get()
    priority = int(entry_priority.get())
    due_date_str = entry_due_date.get()
    task_manager.add_task(task, priority, due_date_str)
    update_task_list()

def remove_task():
    """
    Function to remove a task.
    """
    selected_task = tree.selection()
    if selected_task:
        task_manager.remove_task(int(selected_task[0]))
        update_task_list()
    else:
        messagebox.showinfo("Error", "Please select a task to remove.")

root = tk.Tk()
root.title("To-Do List")

label_task = tk.Label(root, text="Task:")
label_task.grid(row=0, column=0, padx=10, pady=5)
entry_task = tk.Entry(root)
entry_task.grid(row=0, column=1, padx=10, pady=5)

label_priority = tk.Label(root, text="Priority (1-5):")
label_priority.grid(row=1, column=0, padx=10, pady=5)
entry_priority = tk.Entry(root)
entry_priority.grid(row=1, column=1, padx=10, pady=5)

label_due_date = tk.Label(root, text="Due Date (YYYY-MM-DD HH:MM):")
label_due_date.grid(row=2, column=0, padx=10, pady=5)
entry_due_date = tk.Entry(root)
entry_due_date.grid(row=2, column=1, padx=10, pady=5)

button_add_task = tk.Button(root, text="Add Task", command=add_task)
button_add_task.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

tree = ttk.Treeview(root, columns=("Task", "Priority", "Due Date"), show="headings")
tree.heading("Task", text="Task")
tree.heading("Priority", text="Priority")
tree.heading("Due Date", text="Due Date")
tree.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

button_remove_task = tk.Button(root, text="Remove Task", command=remove_task)
button_remove_task.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

task_manager = TaskManager()

root.mainloop()
