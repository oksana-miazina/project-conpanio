from book import AddressBook
from typing import List
from formatter import format_records_as_table
from ui import print_line

def handle_all(args: List[str], book: AddressBook) -> None:
  contacts = list(book.get_all())
  if not contacts:
    print_line("No contacts found.")
    return
  print(format_records_as_table(contacts))