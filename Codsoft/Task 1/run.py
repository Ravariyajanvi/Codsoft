import os
from datetime import datetime

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task, due_date=None):
        task_dict = {
            'task': task,
            'completed': False,
            'created_date': datetime.now().strftime("%Y-%m-%d %H:%M"),
            'due_date': due_date
        }
        self.tasks.append(task_dict)
        print("Task added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("\nNo tasks in the list!")
            return
        
        print("\nYour To-Do List:")
        print("-" * 60)
        for idx, task in enumerate(self.tasks, 1):
            status = "✓" if task['completed'] else " "
            due_date = f"(Due: {task['due_date']})" if task['due_date'] else ""
            print(f"{idx}. [{status}] {task['task']} {due_date}")
        print("-" * 60)

    def mark_completed(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            self.tasks[task_index-1]['completed'] = True
            print("Task marked as completed!")
        else:
            print("Invalid task number!")

    def delete_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            removed_task = self.tasks.pop(task_index-1)
            print(f"Task '{removed_task['task']}' deleted successfully!")
        else:
            print("Invalid task number!")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    todo = TodoList()
    
    while True:
        clear_screen()
        print("\n=== To-Do List Application ===")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == '1':
            task = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD) or press Enter to skip: ")
            due_date = due_date if due_date.strip() else None
            todo.add_task(task, due_date)
        
        elif choice == '2':
            todo.view_tasks()
        
        elif choice == '3':
            todo.view_tasks()
            task_num = input("\nEnter task number to mark as completed: ")
            if task_num.isdigit():
                todo.mark_completed(int(task_num))
        
        elif choice == '4':
            todo.view_tasks()
            task_num = input("\nEnter task number to delete: ")
            if task_num.isdigit():
                todo.delete_task(int(task_num))
        
        elif choice == '5':
            print("\nThank you for using the To-Do List Application!")
            break
        
        else:
            print("Invalid choice! Please try again.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()