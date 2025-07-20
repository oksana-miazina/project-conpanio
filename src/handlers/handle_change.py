from typing import List
from book import AddressBook, Name, Phone, Email
from .contact_finder import find_contact_interactive
from ui import print_error, print_line, print_title, prompt_user

def handle_change(args: List[str], book: AddressBook) -> None:
    if not args:
        print_error("Error: Please provide a name to change. Usage: change <name>")
        return

    record = find_contact_interactive(book, args[0])
    if not record:
        print_error("Change cancelled.")
        return

    print_title("Found this contact:")
    print(record)
    change_confirm = prompt_user("Do you want to change this contact? (y/n): ").strip().lower()
    if change_confirm not in ('y', 'yes'):
        print_error("Change cancelled.")
        return

    # Редагування полів:    
    # Ім'я (Критична секція: оновлення ключа в словнику)
    while True:
        new_name = prompt_user(f"Name [{record.name.value}] (leave empty to keep current): ").strip()
        if not new_name or new_name.capitalize() == record.name.value:
            break
        try:
            record.name = Name(new_name)
            print_line("Name updated.")
            break
        except ValueError as e:
            print_error(f"Error: {e}. Please try again.")

    # Прізвище
    while True:
        current_last_name = record.last_name.value if record.last_name else ""
        new_last_name = prompt_user(f"Last Name [{current_last_name}] (space to clear, empty to keep): ").strip()
        if not new_last_name:
            break
        try:
            if new_last_name == " ":
                record.remove_last_name()
            else:
                record.add_last_name(new_last_name)
            print_line("Last name updated.")
            break
        except ValueError as e:
            print_error(f"Error: {e}. Please try again.")

    # Телефони
    if record.phones:
        print_title("\nCurrent phones:")
        for i, p in enumerate(record.phones, 1):
            print_line(f"  {i}. {p.value}")
    else:
        print_line("\nNo phones.")

    while True:
        action = prompt_user("Phones: (a)dd, (r)emove, (c)hange, or (s)kip? ").strip().lower()
        if action == "s":
            break
        elif action == "a":
            while True:
                new_phone = prompt_user("Enter new phone (or leave empty to cancel): ").strip()
                if not new_phone:
                    break
                try:
                    record.add_phone(new_phone)
                    print_line("Phone added.")
                    break
                except ValueError as e:
                    print_error(f"Error: {e}. Please try again.")
        elif action == "r":
            if not record.phones:
                print_line("No phones to remove.")
                continue
            rem_index = prompt_user("Enter phone number to remove (index): ").strip()
            if rem_index.isdigit() and 1 <= int(rem_index) <= len(record.phones):
                record.phones.pop(int(rem_index) - 1)
                print_line("Phone removed.")
            else:
                print_error("Invalid index.")
        elif action == "c":
            if not record.phones:
                print_line("No phones to change.")
                continue
            ch_index = prompt_user("Enter phone number to change (index): ").strip()
            if ch_index.isdigit() and 1 <= int(ch_index) <= len(record.phones):
                while True:
                    new_phone = prompt_user("Enter new phone value (or leave empty to cancel): ").strip()
                    if not new_phone:
                        break
                    try:
                        # Validate before assigning
                        Phone(new_phone)
                        record.phones[int(ch_index) - 1].value = new_phone
                        print_line("Phone updated.")
                        break
                    except ValueError as e:
                        print_error(f"Error: {e}")
        else:
            print_error("Invalid action.")

    # Емейли (аналогічно)
    if record.emails:
        print_title("\nCurrent emails:")
        for i, e in enumerate(record.emails, 1):
            print_line(f"  {i}. {e.value}")
    else:
        print_line("\nNo emails.")

    while True:
        action = prompt_user("Emails: (a)dd, (r)emove, (c)hange, or (s)kip? ").strip().lower()
        if action == "s":
            break
        elif action == "a":
            while True:
                new_email = prompt_user("Enter new email (or leave empty to cancel): ").strip()
                if not new_email:
                    break
                try:
                    record.add_email(new_email)
                    print_line("Email added.")
                    break
                except ValueError as e:
                    print_error(f"Error: {e}. Please try again.")
        elif action == "r":
            if not record.emails:
                print_line("No emails to remove.")
                continue
            rem_index = prompt_user("Enter email number to remove (index): ").strip()
            if rem_index.isdigit() and 1 <= int(rem_index) <= len(record.emails):
                record.emails.pop(int(rem_index) - 1)
                print_line("Email removed.")
            else:
                print_error("Invalid index.")
        elif action == "c":
            if not record.emails:
                print_line("No emails to change.")
                continue
            ch_index = prompt_user("Enter email number to change (index): ").strip()
            if ch_index.isdigit() and 1 <= int(ch_index) <= len(record.emails):
                while True:
                    new_email = prompt_user("Enter new email value (or leave empty to cancel): ").strip()
                    if not new_email:
                        break
                    try:
                        # Validate before assigning
                        Email(new_email)
                        record.emails[int(ch_index) - 1].value = new_email
                        print_line("Email updated.")
                        break
                    except ValueError as e:
                        print_error(f"Error: {e}")
        else:
            print_error("Invalid action.")

    # День народження
    while True:
        current_bday = record.birthday.value if record.birthday else ""
        new_bday = prompt_user(f"Birthday [{current_bday}] (DD.MM.YYYY, space to clear, empty to keep): ").strip()
        if not new_bday:
            break
        try:
            if new_bday == " ":
                record.birthday = None
            else:
                record.add_birthday(new_bday)
            print_line("Birthday updated.")
            break
        except ValueError as e:
            print_error(f"Invalid birthday format: {e}. Please try again.")

    print_line("Contact updated successfully.")
