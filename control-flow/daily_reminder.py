# Prompt for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process task based on priority and time sensitivity
match priority:
    case "high":
        if time_bound == "yes":
            reminder = f"'{task}' is a high priority task that requires immediate attention today!"
        else:
            reminder = f"Note: '{task}' is a high priority task. Try to complete it soon."
    case "medium":
        if time_bound == "yes":
            reminder = f"'{task}' is a medium priority task that needs attention today."
        else:
            reminder = f"Note: '{task}' is a medium priority task. Consider completing it this week."
    case "low":
        if time_bound == "yes":
            reminder = f"'{task}' is a low priority task, but it's time-bound. Complete it today."
        else:
            reminder = f"Note: '{task}' is a low priority task. Consider completing it when you have free time."
    case _:
        reminder = "Invalid priority. Please enter high, medium, or low."

# Provide customized reminder
print("Reminder:", reminder)
