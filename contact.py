import json
import csv

class Contact:
    def __init__(self):
        self.contacts = []

    def load_contacts(self, filename="contacts.json"):
        try:
            with open(filename, "r", encoding="utf-8") as file:
                self.contacts = json.load(file)
        except FileNotFoundError:
            print(f"File {filename} not found. Starting with an empty contacts list.")
        except json.JSONDecodeError:
            print(f"Error decoding JSON from {filename}. Starting with an empty contacts list.")

    def save_contacts(self, filename="contacts.json"):
        try:
            with open(filename, "w", encoding="utf-8") as file:
                json.dump(self.contacts, file, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"Error saving contacts to {filename}: {e}")

    def add_contact(self, name, phone=None, email=None):
        contact_id = max([contact['id'] for contact in self.contacts], default=0) + 1
        new_contact = {
            "id": contact_id,
            "name": name,
            "phone": phone,
            "email": email
        }
        self.contacts.append(new_contact)
        print(f"Contact with ID {contact_id} added.")

    def search_contact(self, query):
        results = [
            contact for contact in self.contacts
            if query.lower() in contact["name"].lower() or query in (contact["phone"] or "")
        ]
        if results:
            print("Search results:")
            for contact in results:
                print(f"ID: {contact['id']}, Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
        else:
            print("No contacts found.")

    def edit_contact(self, contact_id, new_name=None, new_phone=None, new_email=None):
        for contact in self.contacts:
            if contact["id"] == contact_id:
                if new_name:
                    contact["name"] = new_name
                if new_phone:
                    contact["phone"] = new_phone
                if new_email:
                    contact["email"] = new_email
                print(f"Contact with ID {contact_id} updated.")
                return
        print(f"No contact found with ID {contact_id}.")

    def delete_contact(self, contact_id):
        for contact in self.contacts:
            if contact["id"] == contact_id:
                self.contacts.remove(contact)
                print(f"Contact with ID {contact_id} deleted.")
                return
        print(f"No contact found with ID {contact_id}.")

    def export_contacts_to_csv(self, filename="contacts.csv"):
        try:
            with open(filename, "w", encoding="utf-8", newline='') as file:
                writer = csv.DictWriter(file, fieldnames=["id", "name", "phone", "email"])
                writer.writeheader()
                writer.writerows(self.contacts)
            print(f"Contacts exported to {filename}.")
        except Exception as e:
            print(f"Error exporting contacts to CSV: {e}")

    def import_contacts_from_csv(self, filename="contacts.csv"):
        try:
            with open(filename, "r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    row["id"] = int(row["id"])
                    self.contacts.append(row)
            print(f"Contacts imported from {filename}.")
        except FileNotFoundError:
            print(f"File {filename} not found.")
        except Exception as e:
            print(f"Error importing contacts from CSV: {e}")