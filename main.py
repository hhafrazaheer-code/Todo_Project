tasks = []

while True:

    print("\n===== TO DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        task = input("Enter task: ")
        tasks.append(task)
        print("Task Added Successfully!")

    elif choice == "2":

        print("\nYour Tasks")

        if len(tasks) == 0:
            print("No Tasks Found")

        else:
            count = 1
            for task in tasks:
                print(f"{count}. {task}")
                count += 1

    elif choice == "3":

        print("Thank You!")
        break

    else:

        print("Invalid Choice")