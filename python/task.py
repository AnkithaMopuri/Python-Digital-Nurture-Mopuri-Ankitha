from datetime import datetime

class Task:
    def __init__(self, name, due_date, priority):
        self.name = name
        self.due_date = datetime.strptime(due_date, "%Y-%m-%d")
        self.priority = priority

class TaskScheduler:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def sort_tasks(self):
        self.tasks.sort(key=lambda x: x.due_date)

    def get_overdue(self):
        now = datetime.now()
        return [t for t in self.tasks if t.due_date < now]

    def print_tasks(self):
        print("\n--- Task Schedule ---")
        for t in self.tasks:
            print(t.name, t.due_date.date(), "Priority:", t.priority)


# Example usage
scheduler = TaskScheduler()

scheduler.add_task(Task("Math Assignment", "2026-06-01", "High"))
scheduler.add_task(Task("Project", "2026-06-10", "Medium"))
scheduler.add_task(Task("Exam Prep", "2026-05-30", "High"))

scheduler.sort_tasks()
scheduler.print_tasks()

print("\n--- Overdue Tasks ---")
for t in scheduler.get_overdue():
    print(t.name, t.due_date.date())