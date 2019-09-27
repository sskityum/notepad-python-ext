class Todo:
    def __init__(self, description=None, status='open'):
        self.description = description
        self.status = status

class TodoService:
    def __init__(self):
        self.todos = [
            Todo('Купить хлеба'),
            Todo('Выучить стих'),
            Todo('Покататься на велосипеде'),
            Todo('Подготовиться к зиме')
        ]

    def add_todo(self, todo):
        self.todos.append(todo)
        return self.todos

    def remove_todo(self, todo):
        self.todos.remove(todo)
        return self.todos

    def change_todo(self, id, status, description=None):
        self.todos[id].status = status

        if description:
            self.todos[id].description = description

        return self.todos