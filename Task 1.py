import json

class Task:
    def __init__(self, description, status=False):
        self.description = description
        self.status = status

    def __repr__(self):
        return f"{'[X]' if self.status else '[ ]'} {self.description}"

class ToDoList:
    def __init__(self, filename="tasks.json"):
        self.tasks = []
        self.filename = filename
        self.load_tasks()

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)
        self.save_tasks()

    def update_task(self, index, new_description=None, status=None):
        if 0 <= index < len(self.tasks):
            if new_description:
                self.tasks[index].description = new_description
            if status is not None:
                self.tasks[index].status = status
            self.save_tasks()
        else:
            print("Task not found!")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            self.save_tasks()
        else:
            print("Task not found!")

    def view_tasks(self):
        for idx, task in enumerate(self.tasks):
            print(f"{idx}: {task}")

    def save_tasks(self):
        with open(self.filename, 'w') as file:
            json.dump([task.__dict__ for task in self.tasks], file)

    def load_tasks(self):
        try:
            with open(self.filename, 'r') as file:
                tasks_data = json.load(file)
                self.tasks = [Task(**task) for task in tasks_data]
        except FileNotFoundError:
            self.tasks = []

if __name__ == "__main__":
    todo_list = ToDoList()

    while True:
        print("\nOptions: 1. Add Task  2. Update Task  3. Delete Task  4. View Tasks  5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            task_desc = input("Enter task description: ")
            todo_list.add_task(task_desc)
        elif choice == '2':
            task_idx = int(input("Enter task index to update: "))
            task_desc = input("Enter new description (or leave blank): ")
            task_status = input("Mark as complete? (yes/no): ").lower() == 'yes'
            todo_list.update_task(task_idx, new_description=task_desc, status=task_status)
        elif choice == '3':
            task_idx = int(input("Enter task index to delete: "))
            todo_list.delete_task(task_idx)
        elif choice == '4':
            todo_list.view_tasks()
        elif choice == '5':
            break
        else:
            print("Invalid option. Please try again.")
