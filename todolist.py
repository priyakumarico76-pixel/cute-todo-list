tasks = []

print("🌸 Priya's Cute To-Do List 🌸")

while True:

    print("\n1. Add task")
    print("2. View tasks")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter a new task: ")
        tasks.append(task)

    elif choice == "2":
        print("\n✨ Your Tasks ✨")

        for task in tasks:
            print("☐", task)

    elif choice == "3":
        print("Goodbye 🌸")
        break