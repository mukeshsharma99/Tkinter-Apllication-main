from tkinter import *

def add_task():
    task = task_entry.get()
    if task != "":
        listbox.insert(END, task)
        task_entry.delete(0, END)
