from book.AddressBook import AddressBook
from typing import List

def handle_help(args, book):
    # просто виклик функції допомоги, яка виводить меню 
    from nav import __print_menu
    __print_menu()
    return ""  # потрібно перевірити як працює