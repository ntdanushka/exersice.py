from datetime import datetime

# Define your daily tasks
tasks = {
    '08:00': 'Check emails',
    '09:00': 'Meeting with team',
    '10:00': 'Work on project',
    '12:00': 'Lunch break',
    '13:00': 'Client call',
    '15:00': 'Review code',
    '16:00': 'Prepare report',
    '17:00': 'Wrap up for the day'
}

# Get the current date and time
current_time = datetime.now().strftime("%H:%M")

# Find the next task
next_task_time = None
next_task = None

for task_time in sorted(tasks.keys()):
    if task_time > current_time:
        next_task_time = task_time
        next_task = tasks[task_time]
        break

# Print the schedule
print("Today's Schedule:")
print("=================")

for task_time in sorted(tasks.keys()):
    task = tasks[task_time]
    status = " [Next Task]" if task == next_task else ""
    print(f"{task_time}: {task}{status}")
