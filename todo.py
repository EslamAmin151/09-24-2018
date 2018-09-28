
class Task:
    def __init__(self,title,priority):
        self.title = title
        self.priority = priority
        self.tasks =[]


class Task:
    def __init__(self,title,priority):
        self.title = title
        self.priority = priority
tasks = []
while True:
    title = input ("Enter your task title or q to quit:")
    if(title =="q"):
        break
priority = input("Enter your priority: ")

task = Task(title, priority)
tasks.append(task)
print (len(tasks))
for task in tasks:
    print(task.title)
    print(task.priority)
print ("Thanks for your using the app")
