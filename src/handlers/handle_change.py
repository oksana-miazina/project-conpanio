from typing import List
from book import AddressBook, Record

def handle_change(args: List[str], book: AddressBook) -> str:
    if not args:
        return "Error: Please provide a name to change. Usage: change <name>"

    input_name = args[0].lower()
    all_records = book.get_all()

    # Знаходимо всі записи, імена яких починаються з input_name (регістронечутливо)
    matching_records = [rec for rec in all_records if rec.name.value.lower().startswith(input_name)]

    if len(matching_records) == 1:
        record = matching_records[0]
    elif len(matching_records) == 0:
        while True:
            print(f"No contacts found matching '{args[0]}'. Try again or type 'exit' to cancel.")
            choice = input("Enter name or 'exit': ").strip()
            if choice.lower() == 'exit':
                return "Change cancelled."

            close_results = _search_close(book, choice)
            if len(close_results) == 1:
                record = close_results[0]
                break
            elif len(close_results) > 1:
                print("Did you mean:")
                for i, rec in enumerate(close_results, 1):
                    print(f"{i}. {rec.name.value}")
                while True:
                    sel = input("Enter number of correct name or 'exit': ").strip()
                    if sel.lower() == 'exit':
                        return "Change cancelled."
                    if sel.isdigit() and 1 <= int(sel) <= len(close_results):
                        record = close_results[int(sel) - 1]
                        break
                    print("Invalid input. Try again.")
                break
            else:
                print("No contacts found. Try again or type 'exit'.")
    else:
        print("Multiple contacts found:")
        for i, rec in enumerate(matching_records, 1):
            print(f"{i}. {rec.name.value}")
        while True:
            sel = input("Enter number of correct name or 'exit': ").strip()
            if sel.lower() == 'exit':
                return "Change cancelled."
            if sel.isdigit() and 1 <= int(sel) <= len(matching_records):
                record = matching_records[int(sel) - 1]
                break
            print("Invalid input. Try again.")

    print("Found this contact:")
    print(record)
    change_confirm = input("Do you want to change this contact? (y/n): ").strip().lower()
    if change_confirm not in ('y', 'yes'):
        return "Change cancelled. Returning to main menu."

    print("Leave empty to keep current value, enter a single space to clear the value.")

    # Редагування полів:    
    # Ім'я (Критична секція: оновлення ключа в словнику)
    new_name = input(f"Name [{record.name.value}]: ").strip()
    if new_name and new_name.capitalize() != record.name.value:
        try:
            book.rename_contact(record, new_name)
        except ValueError as e:
            print(f"Error: {e}. Name was not changed.")

    # Прізвище
    current_last_name = record.last_name.value if record.last_name else ""
    new_last_name = input(f"Last Name [{current_last_name}]: ").strip()
    if new_last_name == " ":
        record.remove_last_name()
    elif new_last_name:
        try:
            record.add_last_name(new_last_name)
        except ValueError as e:
            print(f"Error: {e}")

    # Телефони
    if record.phones:
        print("Current phones:")
        for i, p in enumerate(record.phones, 1):
            print(f"{i}. {p.value}")
    else:
        print("No phones.")

    while True:
        action = input("Do you want to (a)dd, (r)emove, or (c)hange phones? (enter to skip): ").strip().lower()
        if action == "":
            break
        elif action == "a":
            new_phone = input("Enter new phone: ").strip()
            if new_phone:
                record.add_phone(new_phone)
        elif action == "r":
            if not record.phones:
                print("No phones to remove.")
                continue
            rem_index = input("Enter phone number to remove (index): ").strip()
            if rem_index.isdigit() and 1 <= int(rem_index) <= len(record.phones):
                record.phones.pop(int(rem_index) - 1)
                print("Phone removed.")
            else:
                print("Invalid index.")
        elif action == "c":
            if not record.phones:
                print("No phones to change.")
                continue
            ch_index = input("Enter phone number to change (index): ").strip()
            if ch_index.isdigit() and 1 <= int(ch_index) <= len(record.phones):
                new_phone = input("Enter new phone value: ").strip()
                if new_phone:
                    record.phones[int(ch_index) - 1].value = new_phone
                    print("Phone updated.")
            else:
                print("Invalid index.")
        else:
            print("Invalid action.")

    # Емейли (аналогічно)
    if record.emails:
        print("Current emails:")
        for i, e in enumerate(record.emails, 1):
            print(f"{i}. {e.value}")
    else:
        print("No emails.")

    while True:
        action = input("Do you want to (a)dd, (r)emove, or (c)hange emails? (enter to skip): ").strip().lower()
        if action == "":
            break
        elif action == "a":
            new_email = input("Enter new email: ").strip()
            if new_email:
                record.add_email(new_email)
        elif action == "r":
            if not record.emails:
                print("No emails to remove.")
                continue
            rem_index = input("Enter email number to remove (index): ").strip()
            if rem_index.isdigit() and 1 <= int(rem_index) <= len(record.emails):
                record.emails.pop(int(rem_index) - 1)
                print("Email removed.")
            else:
                print("Invalid index.")
        elif action == "c":
            if not record.emails:
                print("No emails to change.")
                continue
            ch_index = input("Enter email number to change (index): ").strip()
            if ch_index.isdigit() and 1 <= int(ch_index) <= len(record.emails):
                new_email = input("Enter new email value: ").strip()
                if new_email:
                    record.emails[int(ch_index) - 1].value = new_email
                    print("Email updated.")
            else:
                print("Invalid index.")
        else:
            print("Invalid action.")

    # День народження
    current_bday = record.birthday.value if record.birthday else ""
    new_bday = input(f"Birthday [{current_bday}] (DD.MM.YYYY): ").strip()
    if new_bday == " ":
        record.birthday = None
    elif new_bday:
        try:
            record.add_birthday(new_bday)
        except Exception as e:
            print(f"Invalid birthday format: {e}")

    # Нотатки
    if record.notes:
        print("Current notes:")
        for i, n in enumerate(record.notes, 1):
            print(f"{i}. {n.value}")
    else:
        print("No notes.")

    while True:
        action = input("Do you want to (a)dd, (r)emove notes? (enter to skip): ").strip().lower()
        if action == "":
            break
        elif action == "a":
            new_note = input("Enter new note: ").strip()
            if new_note:
                record.add_note(new_note)
        elif action == "r":
            if not record.notes:
                print("No notes to remove.")
                continue
            rem_index = input("Enter note number to remove (index): ").strip()
            if rem_index.isdigit() and 1 <= int(rem_index) <= len(record.notes):
                record.notes.pop(int(rem_index) - 1)
                print("Note removed.")
            else:
                print("Invalid index.")
        else:
            print("Invalid action.")

    # Теги
    if record.tags:
        print("Current tags:")
        for i, t in enumerate(record.tags, 1):
            print(f"{i}. {t.value}")
    else:
        print("No tags.")

    while True:
        action = input("Do you want to (a)dd, (r)emove tags? (enter to skip): ").strip().lower()
        if action == "":
            break
        elif action == "a":
            new_tag = input("Enter new tag: ").strip()
            if new_tag:
                record.add_tag(new_tag)
        elif action == "r":
            if not record.tags:
                print("No tags to remove.")
                continue
            rem_index = input("Enter tag number to remove (index): ").strip()
            if rem_index.isdigit() and 1 <= int(rem_index) <= len(record.tags):
                record.tags.pop(int(rem_index) - 1)
                print("Tag removed.")
            else:
                print("Invalid index.")
        else:
            print("Invalid action.")

    return "Contact updated successfully."


def _search_close(book: AddressBook, name: str) -> List[Record]:
    import difflib
    all_records = book.get_all()
    all_names = [rec.name.value for rec in all_records]
    close_names = difflib.get_close_matches(name.capitalize(), all_names, n=5, cutoff=0.6)
    return [rec for rec in all_records if rec.name.value in close_names]


def _find_case_insensitive(book: AddressBook, name: str) -> Record | None:
    all_records = book.get_all()
    lowered = name.lower()
    for rec in all_records:
        if rec.name.value.lower() == lowered:
            return rec
    return None
