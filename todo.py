import tkinter as tk
from tkinter import messagebox
import os

TASKS_FILE = "tasks.txt"

def add_task():
    task = entry.get().strip()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Enter a task!")

def delete_task():
    try:
        selected = listbox.curselection()[0]
        listbox.delete(selected)
    except IndexError:
        messagebox.showwarning("Selection Error", "Select a task to delete.")

def toggle_complete(event):
    try:
        selected = listbox.curselection()[0]
        task = listbox.get(selected)

        if task.startswith("✅ "):
            task = task[2:]  # remove check
        else:
            task = "✅ " + task  # add check

        listbox.delete(selected)
        listbox.insert(selected, task)
    except IndexError:
        pass  # No item selected

def save_tasks():
    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        tasks = listbox.get(0, listbox.size())
        for task in tasks:
            f.write(task + "\n")
    messagebox.showinfo("Saved", "Tasks saved successfully.")


def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            for line in f:
                listbox.insert(tk.END, line.strip())

# GUI Setup
root = tk.Tk()
root.title("To-Do List App with Completion")

entry = tk.Entry(root, width=40)
entry.pack(pady=10)

add_btn = tk.Button(root, text="Add Task", command=add_task)
add_btn.pack()

listbox = tk.Listbox(root, width=50, height=10)
listbox.pack(pady=10)

# Bind double-click to toggle complete/incomplete
listbox.bind('<Double-Button-1>', toggle_complete)

delete_btn = tk.Button(root, text="Delete Selected", command=delete_task)
delete_btn.pack()

save_btn = tk.Button(root, text="Save Tasks", command=save_tasks)
save_btn.pack()

load_btn = tk.Button(root, text="Load Tasks", command=load_tasks)
load_btn.pack()

load_tasks()
root.mainloop()
