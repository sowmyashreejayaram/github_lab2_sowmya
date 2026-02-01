"""Todo Manager - Task management system"""

class TodoManager:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, task_name, description=""):
        task = {
            "id": len(self.tasks) + 1,
            "name": task_name,
            "description": description,
            "completed": False
        }
        self.tasks.append(task)
        return task
    
    def get_task(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                return task
        return None
    
    def complete_task(self, task_id):
        task = self.get_task(task_id)
        if task:
            task["completed"] = True
            return True
        return False
    
    def get_all_tasks(self):
        return self.tasks
    
    def get_pending_tasks(self):
        return [task for task in self.tasks if not task["completed"]]

    def set_due_date(self, task_id, due_date):
        """Set due date for task"""
        task = self.get_task(task_id)
        if task:
            task["due_date"] = due_date
            return True
        return False
    
    def get_overdue_tasks(self):
        """Get overdue tasks - MY MODIFICATION!"""
        from datetime import datetime
        today = str(datetime.now().date())
        overdue = []
        for task in self.tasks:
            if "due_date" in task and not task["completed"]:
                if task["due_date"] < today:
                    overdue.append(task)
        return overdue
