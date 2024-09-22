def main():
    # Prompt for a single task
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    # Customized reminder based on priority
    match priority:
        case "high":
            reminder = f"'{task}' is a high priority task"
            if time_bound == "yes":
                reminder += " that requires immediate attention today!"
            else:
                reminder += "."
        case "medium":
            reminder = f"'{task}' is a medium priority task."
            if time_bound == "yes":
                reminder += " Please try to get it done today!"
            else:
                reminder += " You can do it when you have some time."
        case "low":
            reminder = f"'{task}' is a low priority task."
            if time_bound == "yes":
                reminder += " It would be good to get it done soon."
            else:
                reminder += " Consider completing it when you have free time."
        case _:
            reminder = "Invalid priority level. Please enter high, medium, or low."

    # Print the reminder with "Reminder:" prefix
    print(f"Reminder: {reminder}")

if __name__ == "__main__":
    main()
