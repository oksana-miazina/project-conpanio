from typing import List

from book import AddressBook, Name, Phone, Record
from handlers.yes_no_prompt import yes_no_prompt
from ui import print_error, prompt_user, print_title

def handle_add(args: List[str], book: AddressBook) -> None:
    if len(args) < 2:
        print_error("Error: Please provide a name and a phone number, like this ==> add John 0123456789")
        return

    name_str = args[0]
    phone_str = args[1]

    try:
        name = Name(name_str)
        phone = Phone(phone_str)
    except ValueError as e:
        print_error(f"Error: {e}")
        return

    for rec in book.get_all():
        rec: Record
        phone_values = [p.value for p in getattr(rec, 'phones', [])]
        if phone_str in phone_values:
            print_error(f"Phone number {phone_str} is already assigned to another contact '{rec.name.value}'.")
            return

    record = Record(name)
    try:
        record.add_phone(phone_str)
    except ValueError as e:
        print_error(f"Error: {e}")
        return

    if yes_no_prompt("Do you want to add a last name? (y/n): "):
        while True:
            last_name_str = prompt_user("Enter last name (or leave empty to skip): ").strip()
            if not last_name_str:
                break
            try:
                record.add_last_name(last_name_str)
                break
            except ValueError as e:
                print_error(f"Invalid last name: {e}. Please try again.")

    if yes_no_prompt("Do you want to add an email? (y/n): "):
        while True:
            email_str = prompt_user("Enter email (or leave empty to skip): ").strip()
            if not email_str:
                break
            try:
                record.add_email(email_str)
                break
            except ValueError as e:
                print_error(f"Invalid email: {e}. Please try again.")

    if yes_no_prompt("Do you want to add a birthday? (y/n): "):
        while True:
            bday_str = prompt_user("Enter birthday (DD.MM.YYYY) (or leave empty to skip): ").strip()
            if not bday_str:
                break
            try:
                record.add_birthday(bday_str)
                break
            except ValueError as e:
                print_error(f"Invalid birthday: {e}. Please try again.")

    book.add_record(record)

    print_title(f"Contact '{record.name.value}' was successfully added:")
    print(record)
