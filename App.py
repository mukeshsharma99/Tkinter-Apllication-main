from tkinter import *

# Function to add tasks
def add_task():
    task = task_entry.get()
    if task != "":
        listbox.insert(END, task)
        task_entry.delete(0, END)

# Function to delete selected task
def delete_task():
    try:
        selected = listbox.curselection()[0]
        listbox.delete(selected)
    except IndexError:
        pass

# GUI window setup
win = Tk()
win.title('To-Do List App')
win.geometry('600x400+100-100')
win.config(bg='lightblue')

# Heading label
heading = Label(win, text='My To-Do List', font=('Helvetica', 18, 'bold'), bg='lightblue')
heading.pack(pady=10)

# Task entry
task_entry = Entry(win, font=('Helvetica', 14), width=30)
task_entry.pack(pady=10)

# Buttons
add_btn = Button(win, text='Add Task', command=add_task, font=('Helvetica', 12))
add_btn.pack(pady=5)

delete_btn = Button(win, text='Delete Selected Task', command=delete_task, font=('Helvetica', 12))
delete_btn.pack(pady=5)

# Listbox to display tasks
listbox = Listbox(win, width=50, height=10, font=('Helvetica', 12))
listbox.pack(pady=20)

win.mainloop()
