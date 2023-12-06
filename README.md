# Final Project Report

* Student Name: Danny Lin
* Github Username: dannyglin
* Semester: Fall 2023
* Course: CS 5001



## Description 
Overview: 
The To-Do List application simplifies task management by providing users with a convenient interface to add, organize, prioritize, and track tasks, ensuring efficient planning and completion of activities. It offers a user-friendly platform for individuals to systematically manage their daily, weekly, or long-term tasks, enhancing productivity and organization in both personal and professional contexts.

Execution: 
The execution of the To-Do List involves implementing features like task addition, deletion, and editing within a graphical user interface, enabling users to interact with their task lists seamlessly. It encompasses coding functionalities for data storage, retrieval, and manipulation, ensuring tasks are persistently stored and accessible for efficient task management.

Why? 
The reason for creating the To-Do List was to help people better organize their tasks and improve productivity by offering an easy-to-use tool for managing daily activities. This project aimed to simplify task management and aid in effective time organization, providing a straightforward solution for individuals seeking a more structured approach to handling their to-dos.

## Key Features
User Interface: Built-in Python Interface (I thought it was really cool and learned that Python could have a Built-in Gui interface to use)
Sorting and Filtering: Within the gui there is a functionality that is group by different criteria. I added feature such as giving a number of stars to emphasize the importance and a due date on when the task should be finished.
Task Management: Options to edit, delete, and mark tasks as complete based on different criterias.

## Guide

1. Clone the python code from this repository and run the application by opening your terminal

## Installation Instructions

1. To run the application, be sure to be on the directory of the python files
2. Load up the terminal or command prompt (I usually do it by deleting everything in the path and type in 'cmd')
3. Type in "python gui.py" (Here's how it looks on my screen, could be different from yours "C:\Users\Danny\OneDrive\repos\CS5001-Project>python gui.py")
4. Interact with the gui

## Code Review

### gui.py

The gui.py file is responsible for managing the graphical user interface (GUI) of a to-do list application using the tkinter library in Python. Within this file, essential functions include update_task_list(), which refreshes the displayed task list by communicating with the TaskManager class and updating the treeview widget with task details. Additionally, add_task() facilitates the addition of new tasks to the list, collecting input data from GUI fields, validating it, and using the TaskManager to add the task. Furthermore, remove_task() handles the removal of selected tasks from the list, identifying the chosen task in the GUI and utilizing the TaskManager to remove it. These functions interact with the TaskManager class in task_manager.py, enabling tasks-related operations within the GUI.

1. 
```python
def update_task_list():
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
```
Explanation: This function updates the task list displayed in the GUI (using the treeview widget). It retrieves tasks from the TaskManager object and formats the task details to display in the GUI. The function interacts with the treeview widget (tree) to insert or update the tasks.

2. 
```python
def add_task():
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
```
Explanation: This function handles the addition of a task to the task list. It retrieves task details (task description, priority, due date) from the input fields in the GUI. Validates the input data and uses the TaskManager object to add the task to the list. Clears the input fields after successfully adding the task.

3. 
```python
def isValidDateTimeFormat(date_str):
    try:
        datetime.datetime.strptime(date_str, "%m-%d-%Y %H:%M")
        return True
    except ValueError:
        return False
```
Explanation: This function was used to verify the date when the user adds it to their list.

4. 
```python
def remove_task():
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
```
Explanation: This function handles the removal of a selected task from the task list. It identifies the selected task in the GUI (treeview selection) and removes it using the TaskManager object. If no task is selected, it displays an error message.

### task_manager.py

The task_manager.py file houses the TaskManager class, which manages tasks within the to-do list application. This class features essential methods such as __init__(), initializing an instance of the class by creating an empty list to store tasks. The add_task() method incorporates tasks into the list by converting due date strings into datetime objects and appending task details. Additionally, the remove_task() method facilitates the removal of tasks based on the provided index from the task list using the del statement. Furthermore, the get_tasks() method retrieves the stored list of tasks from the TaskManager. The TaskManager class effectively handles tasks, facilitating their addition, removal, and retrieval within the application.

1. 
```python
class TaskManager:
    def __init__(self):
        self.tasks = []
```
Explanation: The TaskManager class is defined with an __init__ method that initializes a new instance of the class. It initializes an empty list (self.tasks) that will store task details.

2. 
```python
    def add_task(self, task, priority, due_date_str):
            due_date = datetime.datetime.strptime(due_date_str, "%m-%d-%Y %H:%M")
            self.tasks.append({"task": task, "priority": priority, "due_date": due_date})
```
Explanation: The add_task method takes task details (task description, priority, due date as string) and adds a new task to the list. It converts the due date string to a datetime object and appends a dictionary containing task details to self.tasks.

3. 
```python
    def remove_task_by_index(self, index):
            if 0 <= index < len(self.tasks):
                del self.tasks[index]
            else:
                print(f"Invalid index '{index}' for task removal.")
```
Explanation: The remove_task method removes a task from the task list based on the provided index. It uses Python's del statement to delete the task at the specified index from self.tasks.

4. 
```python
    def get_tasks(self):
        return self.tasks
```
Explanation: The get_tasks() method in the TaskManager class serves the purpose of allowing other parts of the code to retrieve the list of tasks stored within a TaskManager instance without directly accessing the underlying tasks attribute, promoting better code organization and encapsulation.

### Major Challenges
The biggest challenge for me was using tkinter, the interface built in Python. It was a new concept built into python that I wanted to learn and have it's function with the python code was tough but relieving once it was finished!


## Example Runs and Testing
 Here is a video of me running the gui and testing edge cases!
 Link:

 https://youtu.be/jtDpeNJxbow

## Missing Features / What's Next
Features I would like to add is to make a better looking interface amd probably have a way to save/load all the task when the application ends.

## Final Reflection
During this course, I've enjoyed exploring its features and learning new things with excitement. It's crucial to have a solid foundation for what's coming next. I've gained essential Python skills and I'm thrilled to use them in software engineering. I'm really looking forward to diving into Object Oriented Programming, Data Structures, and Algorithms in upcoming classes. They'll help me learn and grow even more.

This learning experience has been rewarding and got me excited about what's next. I can't wait to tackle Object Oriented Programming, understand Data Structures, and work on Algorithms. These classes will not only broaden my knowledge but also help me improve in this field.
