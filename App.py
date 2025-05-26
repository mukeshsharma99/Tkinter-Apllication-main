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

heading = Label(win, text='My To-Do List', font=('Helvetica', 18, 'bold'), bg='lightblue')
heading.pack(pady=10)

task_entry = Entry(win, font=('Helvetica', 14), width=30)
task_entry.pack(pady=10)

add_btn = Button(win, text='Add Task', command=add_task, font=('Helvetica', 12))
add_btn.pack(pady=5)
