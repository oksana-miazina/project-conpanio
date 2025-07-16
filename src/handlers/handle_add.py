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
    name = Name(args[0])
    phone = Phone(args[1])
  except ValueError as e:
    return f"Error: {e}" 
  
  existing_record = book.get(name.value)

  if existing_record:
    try:
      existing_record.add_phone(phone_str)
      return f"Phone added to exiting contact '{name.value}'."
    except ValueError as e:
      return f"Error: {e}"
  else:
      
      record = Record(name)
      try:
        record.add_phone(phone_str)
      except ValueError as e:
         return f"Error: {e}"
      book.add_record(record)
      response = f"Contact '{name.value}' added successfully." 
      if yes_no_prompt("Do you want to add email? (y/n): "):
          email_str = input("Enter email: ").strip()
          try:
              record.add_email(email_str)
              response += f"Email '{email_str}' added.\n"
          except ValueError as e:
              response += f"Invalid email: {e}\n"


      if yes_no_prompt("Do you want to add birthday? (y/n): "):
          bday_str = input("Enter birthday (DD.MM.YYYY): ").strip()
          try:
              record.add_birthday(bday_str)
              response += f"Birthday '{bday_str}' added.\n"
          except ValueError as e:
              response += f"Invalid birthday: {e}\n"

      return response.strip()






