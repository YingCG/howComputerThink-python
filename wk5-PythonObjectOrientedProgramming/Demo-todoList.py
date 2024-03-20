todos = [{1: "if else"}, {2: "loop"}, {3: "function"}]


class TodoList:
    def __init__(self, todos):
        self.todos = todos

    def addTodo(self, newTask):
        id = len(todos) + 1
        newTask = input("Enter a new task: ")
        todos.append(newTask)
        return todos

    def displayTasks(self, todos):
        print(todos)

    def __str__(self):
        return f"Our tasks: {todos}"


def main():
    while True:
        homework = TodoList(todos)
        menu = input("Press 1 for display task, Press 2 to add task")
        if menu == "1":
            homework.displayTasks(todos)
        if menu == "2":
            homework.addTodo("")


main()
