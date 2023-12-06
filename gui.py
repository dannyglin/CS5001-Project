"""
Final Project    
=======================
Course:   CS 5001
Semester: FALL 2023
Student:  Danny Lin

To-Do-List Application:

The To-Do List application simplifies task management by providing users with a convenient interface to add, organize, prioritize, and track tasks, ensuring efficient planning and completion of activities.
It offers a user-friendly platform for individuals to systematically manage their daily, weekly, or long-term tasks, enhancing productivity and organization in both personal and professional contexts.
"""
import tkinter as tk
from tkinter import ttk, messagebox
from task_manager import TaskManager
import datetime


def update_task_list():
    """
    Updates the displayed task list in the GUI based on the tasks retrieved from TaskManager.
    """
    tree.delete(*tree.get_children())
    tasks = task_manager.get_tasks()
    if tasks:
        for i, task in enumerate(tasks, start=1):
            task_desc = task['task']
            priority_stars = '*' * min(max(task['priority'], 1), 5)
            due_date_str = task['due_date'].strftime("%m-%d-%Y %H:%M") if isinstance(task['due_date'], datetime.datetime) else ""
            tree.insert("", tk.END, values=(task_desc, priority_stars, due_date_str))
    else:
        tree.insert("", tk.END, values=("No tasks in your to-do list.", "", ""))


def add_task():
    """
    Adds a new task to the task list based on user input.
    """
    task = entry_task.get().strip()
    priority = entry_priority.get().strip()
    due_date_str = entry_due_date.get().strip()
    
    if not (task and priority and due_date_str):
        messagebox.showinfo("Error", "Please fill in all fields.")
        return
    if not priority.isdigit() or not (1 <= int(priority) <= 5):
        messagebox.showinfo("Error", "Priority should be a number between 1 and 5.")
        return
    if not isValidDateTimeFormat(due_date_str):
        messagebox.showinfo("Error", "Invalid date format. Please use MM-DD-YYYY HH:MM.")
        return
    try:
        task_manager.add_task(task, int(priority), due_date_str)
        update_task_list()
        entry_task.delete(0, tk.END)
        entry_priority.delete(0, tk.END)
        entry_due_date.delete(0, tk.END)
    except ValueError:
        messagebox.showinfo("Error", "Invalid input for date or time.")


def isValidDateTimeFormat(date_str):
    """
    Checks if the provided date string matches the specified date format.

    Arguments:
    date_str (str): The date string to be validated.

    Returns:
    bool: True if the date string is in the correct format, False otherwise.
    """
    try:
        datetime.datetime.strptime(date_str, "%m-%d-%Y %H:%M")
        return True
    except ValueError:
        return False


def remove_task():
    """
    Removes the selected task from the task list.
    """
    selected_task = tree.selection()
    if selected_task:
        try:
            task_index = tree.index(selected_task[0])
            task_manager.remove_task_by_index(task_index)
            update_task_list()
        except ValueError as e:
            messagebox.showinfo("Error", f"Error removing task: {e}")
    else:
        messagebox.showinfo("Error", "Please select a task to remove.")


def sort_column(column, reverse_flags):
    """
    Sorts the Treeview columns alphabetically when the column header is clicked.
    """
    data = [(tree.set(child, column), child) for child in tree.get_children('')]
    data.sort(reverse=reverse_flags[column])
    for index, (val, child) in enumerate(data):
        tree.move(child, '', index)
    reverse_flags[column] = not reverse_flags[column]
    tree.heading(column, command=lambda: sort_column(column, reverse_flags))


if __name__ == "__main__":
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
    label_due_date = tk.Label(root, text="Due Date (MM-DD-YYYY HH:MM):")
    label_due_date.grid(row=2, column=0, padx=10, pady=5)
    entry_due_date = tk.Entry(root)
    entry_due_date.grid(row=2, column=1, padx=10, pady=5)
    button_add_task = tk.Button(root, text="Add Task", command=add_task)
    button_add_task.grid(row=3, column=0, columnspan=2, padx=10, pady=5)
    tree = ttk.Treeview(root, columns=("Task", "Priority", "Due Date"), show="headings")
    tree.heading("Task", text="Task", command=lambda: sort_column("Task"))
    tree.heading("Priority", text="Priority", command=lambda: sort_column("Priority"))
    tree.heading("Due Date", text="Due Date", command=lambda: sort_column("Due Date"))
    tree.grid(row=4, column=0, columnspan=2, padx=10, pady=5)
    reverse_flags = {"Task": False, "Priority": False, "Due Date": False}
    for col in ("Task", "Priority", "Due Date"):
        tree.heading(col, text=col, command=lambda c=col: sort_column(c, reverse_flags))
    button_remove_task = tk.Button(root, text="Remove Task", command=remove_task)
    button_remove_task.grid(row=5, column=0, columnspan=2, padx=10, pady=5)
    
    task_manager = TaskManager()
    update_task_list()

    root.mainloop()
