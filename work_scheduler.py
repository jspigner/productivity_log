# Create a work-scheduler

# Define schedule_work
def schedule_work(tasks, times):
  schedule = []

  index = 0
  while index < len(tasks):
    scheduled_task = tasks[index] + ": " + times[index]
    schedule.append(scheduled_task)
    index += 1

  return schedule

# Create and list classes and times
tasks = ["Check emails", "Meet with Ava Lovelace", "Call Grace Hopper", "Go for lunch with Code Girls"]
times = ["9 a.m.", "10 a.m.", "11 a.m.", "12 p.m."]
schedule = schedule_work(tasks, times)

# Compute a message to show schedule
print(f"Today's schedule: {schedule}")