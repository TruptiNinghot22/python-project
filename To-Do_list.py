'''To-Do list application 
Create a command line or GUI-based to do list application where users can add, remove, and mark tasks as completed'''
tasks=[]
def add_task(task):
    tasks.append({"task":task, "completed":False})
    print("Task added")
def remove_task(task_index):
    if 0 <= task_index < len(tasks):
        del tasks[task_index]
        print("Task removed successfully.")
    else:
        print("Invalid task index.")
def list_tasks():
    print("\nTo-Do List")
    for index, task in enumerate(tasks,start=1):
        if task["completed"]:
            status="✓"
        else:
            status=" "
        print(f"{index}.[{status}]{task['task']}")
    print()
def mark_completed(index):
    if 1<=index <=len(tasks):
        tasks[index-1]["completed"]=True
        print("Task marked as Completed")
    else:
        print("Invalid task Index")
while True:
    print("\n Options")
    print("1. Add a task")
    print("2. Remove task")
    print("3. Show task")
    print("4. Mark as complete")
    print("5. Exit")
    choice=input("Enter your choice(1/2/3/4/5)")
    if choice=="1":
        task=input("Enter the task:")
        add_task(task)
    elif choice == "2":
        task_index = int(input("Enter the task index to remove: ")) - 1
        remove_task(task_index)
    elif choice=="3":
        list_tasks()
    elif choice=="4":
        list_tasks()
        index=int(input("Enter the task number"))
        mark_completed(index)
    elif choice=="5":
        print("GoodBye")
        break
    else:
        print("Invalid choice. Please choose 1,2,3,4,5")