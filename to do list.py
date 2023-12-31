class Task:
    def __init__(self, task_name, priority):
        self.task_name = task_name
        self.priority = priority
        self.completed = False

    def mark_as_complete(self):
        self.completed = True

    def display_task_info(self):
        status = "Completed" if self.completed else "Not Completed"
        print(f"Task Name: {self.task_name}\nPriority: {self.priority}\nStatus: {status}\n")


# Create an object of the Task class and perform the actions
task = Task(task_name="Complete Project", priority="High")
task.mark_as_complete()
task.display_task_info()





