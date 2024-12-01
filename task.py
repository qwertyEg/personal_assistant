import json
import csv
from datetime import datetime

class Task:
    def __init__(self):
        self.tasks = []

    def load_tasks(self, filename="tasks.json"):
        try:
            with open(filename, "r", encoding="utf-8") as file:
                self.tasks = json.load(file)
        except FileNotFoundError:
            print(f"File {filename} not found. Starting with an empty tasks list.")
        except json.JSONDecodeError:
            print(f"Error decoding JSON from {filename}. Starting with an empty tasks list.")

    def save_tasks(self, filename="tasks.json"):
        try:
            with open(filename, "w", encoding="utf-8") as file:
                json.dump(self.tasks, file, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"Error saving tasks to {filename}: {e}")

    def add_task(self, title, description="", priority="Средний", due_date=""):
        task_id = max([task['id'] for task in self.tasks], default=0) + 1
        new_task = {
            "id": task_id,
            "title": title,
            "description": description,
            "done": False,
            "priority": priority,
            "due_date": due_date
        }
        self.tasks.append(new_task)
        print(f"Task with ID {task_id} added.")

    def list_tasks(self):
        print("Tasks list:")
        for task in self.tasks:
            status = "Done" if task["done"] else "Not Done"
            print(f"ID: {task['id']}, Title: {task['title']}, Status: {status}, Priority: {task['priority']}, Due Date: {task['due_date']}")

    def mark_task_as_done(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                task["done"] = True
                print(f"Task with ID {task_id} marked as done.")
                return
        print(f"No task found with ID {task_id}.")

    def edit_task(self, task_id, new_title=None, new_description=None, new_priority=None, new_due_date=None):
        for task in self.tasks:
            if task["id"] == task_id:
                if new_title:
                    task["title"] = new_title
                if new_description:
                    task["description"] = new_description
                if new_priority:
                    task["priority"] = new_priority
                if new_due_date:
                    task["due_date"] = new_due_date
                print(f"Task with ID {task_id} updated.")
                return
        print(f"No task found with ID {task_id}.")

    def delete_task(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                self.tasks.remove(task)
                print(f"Task with ID {task_id} deleted.")
                return
        print(f"No task found with ID {task_id}.")

    def export_tasks_to_csv(self, filename="tasks.csv"):
        try:
            with open(filename, "w", encoding="utf-8", newline='') as file:
                writer = csv.DictWriter(file, fieldnames=["id", "title", "description", "done", "priority", "due_date"])
                writer.writeheader()
                writer.writerows(self.tasks)
            print(f"Tasks exported to {filename}.")
        except Exception as e:
            print(f"Error exporting tasks to CSV: {e}")

    def import_tasks_from_csv(self, filename="tasks.csv"):
        try:
            with open(filename, "r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    row["id"] = int(row["id"])
                    row["done"] = row["done"].lower() == "true"
                    self.tasks.append(row)
            print(f"Tasks imported from {filename}.")
        except FileNotFoundError:
            print(f"File {filename} not found.")
        except Exception as e:
            print(f"Error importing tasks from CSV: {e}")

    def filter_tasks(self, status=None, priority=None, due_date=None):
        filtered_tasks = self.tasks
        if status is not None:
            filtered_tasks = [task for task in filtered_tasks if task["done"] == status]
        if priority is not None:
            filtered_tasks = [task for task in filtered_tasks if task["priority"] == priority]
        if due_date is not None:
            filtered_tasks = [task for task in filtered_tasks if task["due_date"] == due_date]
        print("Filtered tasks:")
        for task in filtered_tasks:
            status = "Done" if task["done"] else "Not Done"
            print(f"ID: {task['id']}, Title: {task['title']}, Status: {status}, Priority: {task['priority']}, Due Date: {task['due_date']}")