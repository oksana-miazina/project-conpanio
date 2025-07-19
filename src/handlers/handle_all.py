from book import AddressBook
from typing import List
from formatter import format_records_as_table

def handle_all(args: List[str], book: AddressBook) -> str:
  contacts = list(book.get_all())
  if not contacts:
    return "No contacts found."
  return format_records_as_table(contacts)