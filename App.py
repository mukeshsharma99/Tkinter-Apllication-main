from tkinter import *

def add_task():
    task = task_entry.get()
    if task != "":
        listbox.insert(END, task)
        task_entry.delete(0, END)

def delete_task():
    try:
        selected = Listbox.curselection()[0]
        Listbox.delete(selected)
    except IndexError:
        pass

win = Tk()
win.title('To-D0 List App')
win.geometry('600x400+100-100')
win.config(bg='lightblue')

