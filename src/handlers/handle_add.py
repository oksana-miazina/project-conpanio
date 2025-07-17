from typing import List

from book.AddressBook import AddressBook
from book.Record import Record
from book.Fields import Name, Phone
from handlers.yes_no_promt_file import yes_no_prompt

def handle_add(args: List[str], book: AddressBook) -> str:
    if len(args) < 2:
        return "Error: Please provide a name and a phone number, like this ==> John 0123456789"

    name_str = args[0]
    phone_str = args[1]

    try:
        name = Name(name_str)
        phone = Phone(phone_str)
    except ValueError as e:
        return f"Error: {e}"

    # Перевірка телефонів у всіх контактах
    for rec in book.get_all():
        rec: Record
        phone_values = [p.value for p in getattr(rec, 'phones', [])]
        if phone_str in phone_values:
            return f"Phone number {phone_str} is already assigned to another contact '{rec.name.value}'."

    # Перевіряємо, чи існує контакт з таким самим ім'ям
    existing_record = book.find(name.value)

    if existing_record:
        return (
            f"Contact with the name '{name.value}' already exists.\n"
            "Please use another name or use the 'change' command to update this contact."
        )

    # Якщо такого контакту немає — створюємо новий
    record = Record(name)
    try:
        record.add_phone(phone_str)
    except ValueError as e:
        return f"Error: {e}"

    # Запит на last name
    if yes_no_prompt("Do you want to add last name? (y/n): "):
        last_name_str = input("Enter last name: ").strip()
        try:
            record.add_LastName(last_name_str)
        except Exception as e:
            return f"Error with last name: {e}"

    book.add_record(record)
    response = f"Contact '{name.value}' added successfully.\n"

    # Запит на email
    if yes_no_prompt("Do you want to add email? (y/n): "):
        email_str = input("Enter email: ").strip()
        try:
            record.add_email(email_str)
            response += f"Email '{email_str}' added.\n"
        except ValueError as e:
            response += f"Invalid email: {e}\n"

    # Запит на день народження
    if yes_no_prompt("Do you want to add birthday? (y/n): "):
        bday_str = input("Enter birthday (DD.MM.YYYY): ").strip()
        try:
            record.add_birthday(bday_str)
            response += f"Birthday '{bday_str}' added.\n"
        except ValueError as e:
            response += f"Invalid birthday: {e}\n"

    return response.strip()
