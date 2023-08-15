# Taks list array
tasks = []

# Add task function
def add_task(task_name):
    tasks.append({'task_name': task_name, 'completed': False})

# Delete task function
def delete_task(task_index):
    if 0 <= task_index < len(tasks): # Check if task index is valid
        del tasks[task_index]
    else:
        print("Invalid task index!")

# Mark task as completed function
def mark_completed(task_index):
    if 0 <= task_index < len(tasks): # Check if task index is valid
        tasks[task_index]['completed'] = True
    else:
        print("Invalid task index!")

# List tasks function
def list_tasks():
    for index, task in enumerate(tasks): # Enumerate tasks list
        status = "✓" if task['completed'] else " " # Check if task is completed
        print(f"{index + 1}. [{status}] {task['task_name']}") # Print task

# Main function
def main():
    while True:
        print("\nConsole Task List\n")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Mark Task as Completed")
        print("4. List Tasks")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == '1':
            task_name = input("Enter task name: ")
            add_task(task_name)
        elif choice == '2':
            list_tasks()
            task_index = int(input("Enter task index to delete: ")) - 1
            delete_task(task_index)
        elif choice == '3':
            list_tasks()
            task_index = int(input("Enter task index to mark as completed: ")) - 1
            mark_completed(task_index)
        elif choice == '4':
            list_tasks()
        elif choice == '5':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice! Please select a valid option.")

# Run main function
if __name__ == "__main__":
    main()
