import tkinter as tk
from todo_list import Todo, TodoService

#https://docs.python.org/3/library/tkinter.ttk.html

class TodoForm(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack(fill=tk.BOTH, expand=tk.TRUE)
        self.todo_service = TodoService()

        self.render_form()
        self.todosFrame = self.render_todos()

    def render_todos(self):
        listFrame = tk.Frame(self)
        listFrame.pack(fill=tk.BOTH, expand=tk.TRUE)

        for todo in self.todo_service.todos:
            todo_row = tk.Frame(listFrame, bd=1, bg='silver')
            todo_row.pack(fill=tk.BOTH)

            lbl = tk.Label(todo_row, text=todo.description, font="arial 12 bold")
            lbl.pack(side=tk.RIGHT, fill=tk.BOTH, expand=tk.TRUE)

            btnRemove = tk.Button(todo_row, text="Удалить", width=7, fg="brown", activebackground = "brown", font="arial 12 bold", command=lambda :self.remove_todo(todo))
            btnRemove.pack(side=tk.LEFT)

        return listFrame

    def render_form(self):
        form = tk.Frame(self, bd=3, bg='silver')
        form.pack(fill=tk.BOTH)

        input = tk.Entry(form, font="arial 12 bold")
        input.pack(fill=tk.BOTH)

        btnAdd = tk.Button(form, text="add", fg="red", activebackground = "red", font="arial 12 bold")
        btnAdd.pack(fill=tk.BOTH)
        btnAdd['command'] = lambda : self.add_todo(input)

    def add_todo(self, input):
        self.todo_service.add_todo(Todo(input.get()))
        input.delete(0, len(input.get()))

        self.todosFrame.destroy()
        self.todosFrame = self.render_todos()

    def remove_todo(self, todo):
        self.todo_service.remove_todo(todo)

        self.todosFrame.destroy()
        self.todosFrame = self.render_todos()