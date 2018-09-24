
class Task:
    def __init__(self,title,priority):
        self.title = title
        self.priority = priority
        self.tasks =[]


def add_task(self,title,priority):
    self.tasks.append(title)
    self.tasks.append(priority)

def view_task(self):
    print(self.tasks)


def remove_task (self,title,priority):
    self.tasks.remove(title)
    self.tasks.remove(priority)

today = Task("","")
while True:
    prompt = input("To add a task please click'A'. To view tasks please click 'V'. To remove click 'R'")
    if (prompt == 'A'):
        task_title = input("Please Enter your task name").lower()
        task_priority = input("Please Enter your task priority").lower()
        today.add_task(task_title,task_priority)
    elif (prompt == 'R'):
        task_title = input("Please Enter your task name")
        task_priority = input("Please Enter your task priority")
        today.remove_task(task_title,task_priority)
    elif (prompt == 'V'):
        today.view_task()
    else:
        print ("please Enter valid option:")
    quit = input("to quit the program , please press q")
    if (quit == "q"):
        import sys
        sys.exit(0)
