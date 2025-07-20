from typing import List

from book import AddressBook, Name, Phone, Record
from .yes_no_prompt import yes_no_prompt
from ui import print_error, prompt_user, print_title

def handle_add(args: List[str], book: AddressBook) -> None:
    if len(args) < 2:
        print_error("Error: Please provide a name and a phone number, like this ==> John 0123456789")
        return

    name_str = args[0]
    phone_str = args[1]

    try:
        name = Name(name_str)
        phone = Phone(phone_str)
    except ValueError as e:
        print_error(f"Error: {e}")
        return

    # Перевірка телефонів у всіх контактах
    for rec in book.get_all():
        rec: Record
        phone_values = [p.value for p in getattr(rec, 'phones', [])]
        if phone_str in phone_values:
            print_error(f"Phone number {phone_str} is already assigned to another contact '{rec.name.value}'.")
            return

    # Якщо такого контакту немає — створюємо новий
    record = Record(name)
    try:
        record.add_phone(phone_str)
    except ValueError as e:
        print_error(f"Error: {e}")
        return

    # Запит на last name
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

    # Запит на email
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

    # Запит на день народження
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

    # Додаємо повністю заповнений запис до книги в самому кінці
    book.add_record(record)

    # Виводимо фінальне повідомлення про успіх
    print_title(f"Contact '{record.name.value}' was successfully added:")
    print(record)
