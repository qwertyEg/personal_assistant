import json
import csv
from datetime import datetime

class Note:
    def __init__(self):
        self.notes = []

    def load_notes(self, filename="notes.json"):
        try:
            with open(filename, "r", encoding="utf-8") as file:
                self.notes = json.load(file)
        except FileNotFoundError:
            print(f"File {filename} not found. Starting with an empty notes list.")
        except json.JSONDecodeError:
            print(f"Error decoding JSON from {filename}. Starting with an empty notes list.")

    def save_notes(self, filename="notes.json"):
        try:
            with open(filename, "w", encoding="utf-8") as file:
                json.dump(self.notes, file, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"Error saving notes to {filename}: {e}")

    def create_note(self, title, content):
        note_id = max([note['id'] for note in self.notes], default=0) + 1
        timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        new_note = {"id": note_id, "title": title, "content": content, "timestamp": timestamp}
        self.notes.append(new_note)
        print(f"Note with ID {note_id} created.")

    def list_notes(self):
        print("Notes list:")
        for note in self.notes:
            print(f"ID: {note['id']}, Title: {note['title']}, Timestamp: {note['timestamp']}")

    def view_note_details(self, note_id):
        for note in self.notes:
            if note["id"] == note_id:
                print(f"ID: {note['id']}\nTitle: {note['title']}\nContent: {note['content']}\nTimestamp: {note['timestamp']}")
                return
        print(f"No note found with ID {note_id}.")

    def edit_note(self, note_id, new_title=None, new_content=None):
        for note in self.notes:
            if note["id"] == note_id:
                if new_title:
                    note["title"] = new_title
                if new_content:
                    note["content"] = new_content
                note["timestamp"] = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                print(f"Note with ID {note_id} updated.")
                return
        print(f"No note found with ID {note_id}.")

    def delete_note(self, note_id):
        for note in self.notes:
            if note["id"] == note_id:
                self.notes.remove(note)
                print(f"Note with ID {note_id} deleted.")
                return
        print(f"No note found with ID {note_id}.")

    def export_notes_to_csv(self, filename="notes.csv"):
        try:
            with open(filename, "w", encoding="utf-8", newline='') as file:
                writer = csv.DictWriter(file, fieldnames=["id", "title", "content", "timestamp"])
                writer.writeheader()
                writer.writerows(self.notes)
            print(f"Notes exported to {filename}.")
        except Exception as e:
            print(f"Error exporting notes to CSV: {e}")

    def import_notes_from_csv(self, filename="notes.csv"):
        try:
            with open(filename, "r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    row["id"] = int(row["id"])
                    self.notes.append(row)
            print(f"Notes imported from {filename}.")
        except FileNotFoundError:
            print(f"File {filename} not found.")
        except Exception as e:
            print(f"Error importing notes from CSV: {e}")


