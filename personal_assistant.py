from notes import Note
from task import Task
from contact import Contact
from finance import FinanceRecord
from calculate import Calculator

def main():
    while True:
        print('''\nДобро пожаловать в Персональный помощник!
Выберите действие:
1. Управление заметками
2. Управление задачами
3. Управление контактами
4. Управление финансовыми записями
5. Калькулятор
6. Выход''')

        action = input("Введите номер действия: ")

        if action == "1":
            manage_notes()
        elif action == "2":
            manage_tasks()
        elif action == "3":
            manage_contacts()
        elif action == "4":
            manage_finances()
        elif action == "5":
            use_calculator()
        elif action == "6":
            print("До свидания!")
            break
        else:
            print("Неверный ввод. Пожалуйста, выберите действие из списка. У вас получится!")

def manage_notes():
    note_app = Note()
    note_app.load_notes()
    while True:
        print('''\nУправление заметками:
1. Создать новую заметку
2. Просмотреть список заметок
3. Просмотреть подробности заметки
4. Редактировать заметку
5. Удалить заметку
6. Назад''')

        choice = input("Выберите действие: ")

        if choice == "1":
            title = input("Введите заголовок заметки: ")
            content = input("Введите содержимое заметки: ")
            note_app.create_note(title, content)
            note_app.save_notes()
        elif choice == "2":
            note_app.list_notes()
        elif choice == "3":
            note_id = int(input("Введите ID заметки: "))
            note_app.view_note_details(note_id)
        elif choice == "4":
            note_id = int(input("Введите ID заметки для редактирования: "))
            new_title = input("Введите новый заголовок (оставьте пустым для пропуска): ")
            new_content = input("Введите новое содержимое (оставьте пустым для пропуска): ")
            note_app.edit_note(note_id, new_title or None, new_content or None)
            note_app.save_notes()
        elif choice == "5":
            note_id = int(input("Введите ID заметки для удаления: "))
            note_app.delete_note(note_id)
            note_app.save_notes()
        elif choice == "6":
            break
        else:
            print("Неверный ввод. Попробуйте снова.")

def manage_tasks():
    task_app = Task()
    task_app.load_tasks()
    while True:
        print('''\nУправление задачами:
1. Добавить новую задачу
2. Просмотреть список задач
3. Отметить задачу как выполненную
4. Редактировать задачу
5. Удалить задачу
6. Назад''')

        choice = input("Выберите действие: ")

        if choice == "1":
            title = input("Введите заголовок задачи: ")
            description = input("Введите описание задачи: ")
            priority = input("Введите приоритет задачи (Высокий, Средний, Низкий): ")
            due_date = input("Введите срок выполнения задачи (ДД-ММ-ГГГГ): ")
            task_app.add_task(title, description, priority, due_date)
            task_app.save_tasks()
        elif choice == "2":
            task_app.list_tasks()
        elif choice == "3":
            task_id = int(input("Введите ID задачи для отметки как выполненной: "))
            task_app.mark_task_as_done(task_id)
            task_app.save_tasks()
        elif choice == "4":
            task_id = int(input("Введите ID задачи для редактирования: "))
            new_title = input("Введите новый заголовок (оставьте пустым для пропуска): ")
            new_description = input("Введите новое описание (оставьте пустым для пропуска): ")
            new_priority = input("Введите новый приоритет (оставьте пустым для пропуска): ")
            new_due_date = input("Введите новый срок (оставьте пустым для пропуска): ")
            task_app.edit_task(task_id, new_title or None, new_description or None, new_priority or None, new_due_date or None)
            task_app.save_tasks()
        elif choice == "5":
            task_id = int(input("Введите ID задачи для удаления: "))
            task_app.delete_task(task_id)
            task_app.save_tasks()
        elif choice == "6":
            break
        else:
            print("Неверный ввод. Попробуйте снова.")

def manage_contacts():
    contact_app = Contact()
    contact_app.load_contacts()
    while True:
        print('''\nУправление контактами:
1. Добавить новый контакт
2. Найти контакт
3. Редактировать контакт
4. Удалить контакт
5. Назад''')

        choice = input("Выберите действие: ")

        if choice == "1":
            name = input("Введите имя контакта: ")
            phone = input("Введите номер телефона: ")
            email = input("Введите email: ")
            contact_app.add_contact(name, phone, email)
            contact_app.save_contacts()
        elif choice == "2":
            query = input("Введите имя или номер телефона для поиска: ")
            contact_app.search_contact(query)
        elif choice == "3":
            contact_id = int(input("Введите ID контакта для редактирования: "))
            new_name = input("Введите новое имя (оставьте пустым для пропуска): ")
            new_phone = input("Введите новый телефон (оставьте пустым для пропуска): ")
            new_email = input("Введите новый email (оставьте пустым для пропуска): ")
            contact_app.edit_contact(contact_id, new_name or None, new_phone or None, new_email or None)
            contact_app.save_contacts()
        elif choice == "4":
            contact_id = int(input("Введите ID контакта для удаления: "))
            contact_app.delete_contact(contact_id)
            contact_app.save_contacts()
        elif choice == "5":
            break
        else:
            print("Неверный ввод. Попробуйте снова.")

def manage_finances():
    finance_app = FinanceRecord()
    finance_app.load_records()
    while True:
        print('''\nУправление финансовыми записями:
1. Добавить новую запись
2. Просмотреть все записи
3. Генерировать отчёт
4. Подсчитать баланс
5. Группировка по категориям
6. Назад''')

        choice = input("Выберите действие: ")

        if choice == "1":
            amount = float(input("Введите сумму (положительное для дохода, отрицательное для расхода): "))
            category = input("Введите категорию: ")
            date = input("Введите дату (ДД-ММ-ГГГГ): ")
            description = input("Введите описание: ")
            finance_app.add_record(amount, category, date, description)
            finance_app.save_records()
        elif choice == "2":
            finance_app.list_records()
        elif choice == "3":
            start_date = input("Введите начальную дату (ДД-ММ-ГГГГ): ")
            end_date = input("Введите конечную дату (ДД-ММ-ГГГГ): ")
            finance_app.generate_report(start_date, end_date)
        elif choice == "4":
            finance_app.calculate_balance()
        elif choice == "5":
            finance_app.group_by_category()
        elif choice == "6":
            break
        else:
            print("Неверный ввод. Попробуйте снова.")

def use_calculator():
    calc = Calculator()
    while True:
        print('''\nКалькулятор:
1. Выполнить арифметическую операцию
2. Назад''')

        choice = input("Выберите действие: ")

        if choice == "1":
            expression = input("Введите арифметическое выражение: ")
            try:
                result = calc.evaluate_expression(expression)
                print(f"Результат: {result}")
            except ValueError as e:
                print(f"Ошибка: {e}")
        elif choice == "2":
            break
        else:
            print("Неверный ввод. Попробуйте снова.")

if __name__ == "__main__":
    main()

