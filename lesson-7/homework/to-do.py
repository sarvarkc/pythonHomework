class TodoManager:
    def __init__(self):
        self.todos = []
        self.file_path = 'todos.txt'
        self.loadTodos()

    def loadTodos(self):
        try:
            with open(self.file_path, 'r') as f:
                for line in f:
                    data = line.strip().split(',')
                    if len(data) == 5:
                        self.todos.append({
                            'ID': int(data[0]),
                            'Title': data[1],
                            'Description': data[2],
                            'Due-Date': data[3],
                            'Status': data[4]
                        })
        except FileNotFoundError:
            pass

    def saveTodos(self):
        with open(self.file_path, 'w') as f:
            for x in self.todos:
                f.write(f"{x['ID']},{x['Title']},{x['Description']},{x['Due-Date']},{x['Status']}\n")

    def addTodos(self, id, title, desc, due, status):
        if status == "completed" or status == "pending":
            self.todos.append({'ID': id, 'Title': title, 'Description': desc, 'Due-Date': due, 'Status': status})
            self.saveTodos()
            print("Task added successfully.")
            return
        print("Wrong Status")

    def viewTodos(self):
        if not self.todos:
            print("No tasks found.")
        else:
            for x in self.todos:
                print(f"{x['ID']}, {x['Title']}, {x['Description']}, {x['Due-Date']}, {x['Status']}")

    def searchTodo(self, status):
        toggle = 1
        for x in self.todos:
            if x['Status'] == status:
                print(f"{x['ID']}, {x['Title']}, {x['Description']}, {x['Due-Date']}, {x['Status']}")
                toggle = 0
        if toggle == 1:
            print("Tasks not found.")

    def updateTodo(self, id):
        toggle = 1
        for x in self.todos:
            if x['ID'] == id:
                new_title = input("Write new title: ")
                new_desc = input("Write new description: ")
                new_due = input("Write new due-date: ")
                new_status = input("Write new status: ")
                if new_status == "completed" or new_status == "pending":
                    x['Title'] = new_title
                    x['Description'] = new_desc
                    x['Due-Date'] = new_due
                    x['Status'] = new_status
                    self.saveTodos()
                    print("Task information updated.")
                    toggle = 0
                else:
                    toggle = 0
                    print("Wrong Status")
        if toggle == 1:
            print("Task not found.")

    def delTodo(self, id):
        for x in self.todos:
            if x['ID'] == id:
                self.todos.remove(x)
                self.saveTodos()
                print("Task deleted.")
                return
        print("Task not found.")


manager = TodoManager()
while True:
    choice = input("1. Add a new task\n2. View all tasks\n3. Update a task\n4. Delete a task\n5. Filter tasks by status\n6. Exit\n")

    if choice == '1':
        id = int(input("Enter ID: "))
        title = input("Enter title: ")
        description = input("Enter description: ")
        due = input("Enter due-date: ")
        status = input("Enter status: ")
        manager.addTodos(id, title, description, due, status)
    elif choice == '2':
        manager.viewTodos()
    elif choice == '3':
        id = int(input("Enter Task ID to update: "))
        manager.updateTodo(id)
    elif choice == '4':
        id = int(input("Enter Task ID to delete: "))
        manager.delTodo(id)
    elif choice == '5':
        status = input("Enter Task status to search: ")
        manager.searchTodo(status)
        pass
    elif choice == '6':
        break
    else:
        print("Invalid option. Please try again.")
