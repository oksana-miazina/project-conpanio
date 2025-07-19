from book import AddressBook
from typing import List

def handle_hello(args: List[str], book: AddressBook) -> str:
    return ("Hello! How can I assist you today?\n"
            "Type 'help' to see the list of available commands.")