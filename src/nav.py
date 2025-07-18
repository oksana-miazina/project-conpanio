import difflib
from typing import List, Tuple
from handlers.handle_add import handle_add
from ui import print_error, print_title, print_line
from handlers.handle_all import handle_all
from handlers.handle_help import handle_help
from handlers.handle_hello import handle_hello 
from handlers.handle_find import handle_find
from handlers.handle_change import handle_change
from handlers.handle_delete import handle_delete
from handlers.handle_birthdays import handle_birthdays

__command_handlers = {
    "hello": handle_hello,
    "help": handle_help,
    "add": handle_add,
    "find": handle_find,
    "change": handle_change,
    "delete": handle_delete,
    # "phone": handle_phone,
    "all": handle_all,
    # "add-birthday": add_birthday,
    # "show-birthday": show_birthday,
    "birthdays": handle_birthdays,
}

def __print_menu() -> None:
    print_title("Available commands:")
    print_line("  hello                 - Greet the assistant.")
    print_line("  help                  - Print all commands")
    print_line("  add [name] [phone]    - Add a new contact.")
    print_line("  change [name]         - Change contact.")
    print_line("  delete [name]         - Delete contact.")
    print_line("  phone [name]          - Show phone number of a contact.")
    print_line("  all                   - Show all contacts.")
    print_line("  find [name]           - Find  contacts and show.")
    print_line("  exit, close           - Exit the assistant.")
    print_line("  add-birthday [name] [DD.MM.YYYY] - Add birthday to a contact.")
    print_line("  show-birthday [name]             - Show birthday of a contact.")
    print_line("  birthdays                        - Show upcoming birthdays.")

def __parse_input(user_input: str) -> Tuple[str, List[str]]:
    cmd, *args = user_input.strip().split()
    return cmd.lower(), args

class ExitException(Exception):
    pass

def start_nav(book) -> None:
    print_title("Welcome to the assistant bot!")
    __print_menu()

    commands_list = list(__command_handlers.keys())+ ["exit", "close"]

    while True:
        user_input = input("Enter a command: ").strip()
        if not user_input:
            continue

        command, args = __parse_input(user_input)
        handler = __command_handlers.get(command)
       
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