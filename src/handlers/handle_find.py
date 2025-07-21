from typing import List
from book import AddressBook
from handlers.contact_finder import find_contact_interactive
from ui import print_error

def handle_find(args: List[str], book: AddressBook) -> None:
    if len(args) < 1:
        print_error("Error: Please provide a name to search for. Usage: find <name>")
        return
    
    name_query = args[0]
    record = find_contact_interactive(book, name_query)

    if record:
        print(record)
