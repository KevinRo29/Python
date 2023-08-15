# Tasks array
tasks = []

# Add task function
def add_task(task_name):
    tasks.append({'task_name': task_name, 'completed': False}) # Append task to tasks array

# Delete task function
def delete_task(task_index):
    if 0 <= task_index < len(tasks): # Check if task index is valid
        del tasks[task_index]
    else:
        print("Invalid task index!")

# Mark task completed function
def mark_completed(task_index):
    if 0 <= task_index < len(tasks): # Check if task index is valid
        tasks[task_index]['completed'] = True
    else:
        print("Invalid task index!")

# List tasks function
def list_tasks():
    for index, task in enumerate(tasks):
        status = '✓' if task['completed'] else '✗'
        print(f"{index + 1}. [{status}] {task['task_name']}")

# Main function
def main():
    while True:
        print("\nTask List\n")
        print("1. Add task")
        print("2. Delete task")
        print("3. Mark task completed")
        print("4. List tasks")
        print("5. Exit")

        choice = input("\nWhat would you like to do? ")

        if choice == '1': # Add task
            tasks_name = input("Enter task name: ")
            add_task(tasks_name)
        elif choice == '2': # Delete task
            list_tasks()
            task_index = int(input("Enter task index: ")) - 1
            delete_task(task_index)
        elif choice == '3': # Mark task completed
            list_tasks()
            task_index = int(input("Enter task index to mark completed: ")) - 1
            mark_completed(task_index)
        elif choice == '4': # List tasks
            list_tasks()
        elif choice == '5': # Exit
            print("Exiting the program...")
            break
        else:
            print("Invalid choice! Please select a valid choice.")

if __name__ == '__main__':
    main()