task = str(input("Enter your task: "))

priority = str(input("Priority (high/medium/low): "))

time_bound = str(input("Is it time-bound? (yes/no): "))


match priority:
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
        else:
            print(f"Note: '{task}' is a {priority} priority task.  Consider completing soon.")
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
        else:
            print(f"Note: '{task}' is a {priority} priority task. Complete it now.")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
        else:
            print(f"Note: '{task}' is a {priority} priority task. Consider completing it when you have free time.")
    case _:
        print("An error occured")
