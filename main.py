import tkinter as tk
from todo_form import TodoForm

root = tk.Tk()
root.geometry('400x300')
root.title('Todo list')

todoForm = TodoForm(root)

todoForm.mainloop()