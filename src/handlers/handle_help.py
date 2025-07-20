from typing import List
from book import AddressBook
from ui import print_menu

def handle_help(args: List[str], book: AddressBook) -> None:
    print_menu()