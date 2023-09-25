todo_list={}

def add_task():
    task=input("Enter the task you want to save in your list: ")
    priority=input("Enter the priority of the entered task: ")
    todo_list[task]=priority
    print(f"The task'{task}' is added with '{priority}' priority.")



def remove_task():
    task=input("Enter the task you want to delet from to do list: ")

    if task in todo_list:
        del todo_list[task]
        print(f" The task '{task}' is deleted from to do list")
    else:
        print("The task you have entered is not found in todo list. If you want to delet the task please entre the correct task.")



def view_task():
    if not todo_list:
        print("You haven't any work.\nYour to do list is empty")
        print("\n")
    else:
        for task, prirority in todo_list.items():
            print(f"Your have a task name called '{task}' which priority is '{prirority}'.")


while True:
    print("What do yo want to do in To Do app")
    print("Enter 1 for adding your task in to do list.")
    print("Enter 2 for remove your task from to do list.")
    print("Enter 3 to view your task in to do list.")
    print("Enter 4 to exit the app.")

    choice=input("Enter your choice as per your need: ")

    if choice=='1':
        add_task()
        print("\n")

    elif choice =='2':
            remove_task()
            print("\n")

    elif choice=='3':
                view_task()
                print("\n")

    elif choice=='4':
                    print("Thank you for using to do app.")
                    break
    else:
        print("Your choice is invalid. Please enter the write option to use to do app.\nThank you!")
        print("\n")

    


