import difflib
from typing import List, Tuple

from handlers import COMMAND_HANDLERS
from book import AddressBook
from ui import print_error, print_menu, print_title

def __parse_input(user_input: str) -> Tuple[str, List[str]]:
    cmd, *args = user_input.strip().split()
    return cmd.lower(), args

class ExitException(Exception):
    pass

def start_nav(book: AddressBook) -> None:
    print_title("Welcome to the assistant bot!")
    print_menu()

    commands_list = list(COMMAND_HANDLERS.keys()) + ["exit", "close"]

    while True:
        user_input = input("Enter a command: ").strip()
        if not user_input:
            continue

        command, args = __parse_input(user_input)
        handler = COMMAND_HANDLERS.get(command)
       
        if handler:
            print(handler(args, book))
        elif command in ("exit", "close"):
            print_title("Good bye!")
            raise ExitException    
        else:
            # Пошук схожих команд
            close_matches = difflib.get_close_matches(command, commands_list, n=3, cutoff=0.5)
            if close_matches:
                print_error(f"Invalid command. Did you mean: {', '.join(close_matches)}?")
            else:
                print_error("Invalid command.")