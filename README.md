# productivity_log
A simple code to show a scheduled list of activities and times. 

def productivity_log(tasks, times): 
 schedule = [] 
 
 index = 0 
 while index < len(tasks): 
 scheduled_task = tasks[index] + ": " + times[index] 
 schedule.append(scheduled_task) 
 index += 1 
 
 return schedule 

tasks = ["walk dog", "do yoga", "make coffee", "check emails, "code"] 
times = ["6 a.m.", "6:45 a.m.", "7:30 a.m.", "7:45 a.m.", "8 a.m."] 
schedule = productivity_log(tasks, times) 
print (f"Tuesday's schedule: {schedule}")
