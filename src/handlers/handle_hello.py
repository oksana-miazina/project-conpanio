from book import AddressBook
from typing import List
from ui import print_line

def handle_hello(args: List[str], book: AddressBook) -> None:
    print_line("Hello! How can I assist you today?")
    print_line("Type 'help' to see the list of available commands.")