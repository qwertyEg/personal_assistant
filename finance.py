import json
import csv
from datetime import datetime

class FinanceRecord:
    def __init__(self):
        self.records = []

    def load_records(self, filename="finance.json"):
        try:
            with open(filename, "r", encoding="utf-8") as file:
                self.records = json.load(file)
        except FileNotFoundError:
            print(f"File {filename} not found. Starting with an empty records list.")
        except json.JSONDecodeError:
            print(f"Error decoding JSON from {filename}. Starting with an empty records list.")

    def save_records(self, filename="finance.json"):
        try:
            with open(filename, "w", encoding="utf-8") as file:
                json.dump(self.records, file, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"Error saving records to {filename}: {e}")

    def add_record(self, amount, category, date, description=""):
        record_id = max([record['id'] for record in self.records], default=0) + 1
        new_record = {
            "id": record_id,
            "amount": amount,
            "category": category,
            "date": date,
            "description": description
        }
        self.records.append(new_record)
        print(f"Record with ID {record_id} added.")

    def list_records(self, category=None, date=None):
        filtered_records = self.records
        if category:
            filtered_records = [record for record in filtered_records if record["category"] == category]
        if date:
            filtered_records = [record for record in filtered_records if record["date"] == date]
        print("Financial records:")
        for record in filtered_records:
            print(f"ID: {record['id']}, Amount: {record['amount']}, Category: {record['category']}, Date: {record['date']}, Description: {record['description']}")

    def generate_report(self, start_date, end_date):
        start_date_obj = datetime.strptime(start_date, "%d-%m-%Y")
        end_date_obj = datetime.strptime(end_date, "%d-%m-%Y")
        filtered_records = [
            record for record in self.records
            if start_date_obj <= datetime.strptime(record["date"], "%d-%m-%Y") <= end_date_obj
        ]
        print(f"Report from {start_date} to {end_date}:")
        total_income = sum(record["amount"] for record in filtered_records if record["amount"] > 0)
        total_expenses = sum(record["amount"] for record in filtered_records if record["amount"] < 0)
        print(f"Total Income: {total_income}")
        print(f"Total Expenses: {total_expenses}")
        print(f"Net Balance: {total_income + total_expenses}")

    def calculate_balance(self):
        balance = sum(record["amount"] for record in self.records)
        print(f"Current Balance: {balance}")

    def group_by_category(self):
        grouped = {}
        for record in self.records:
            if record["category"] not in grouped:
                grouped[record["category"]] = 0
            grouped[record["category"]] += record["amount"]
        print("Grouped by category:")
        for category, total in grouped.items():
            print(f"{category}: {total}")

    def export_records_to_csv(self, filename="finance.csv"):
        try:
            with open(filename, "w", encoding="utf-8", newline='') as file:
                writer = csv.DictWriter(file, fieldnames=["id", "amount", "category", "date", "description"])
                writer.writeheader()
                writer.writerows(self.records)
            print(f"Records exported to {filename}.")
        except Exception as e:
            print(f"Error exporting records to CSV: {e}")

    def import_records_from_csv(self, filename="finance.csv"):
        try:
            with open(filename, "r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    row["id"] = int(row["id"])
                    row["amount"] = float(row["amount"])
                    self.records.append(row)
            print(f"Records imported from {filename}.")
        except FileNotFoundError:
            print(f"File {filename} not found.")
        except Exception as e:
            print(f"Error importing records from CSV: {e}")