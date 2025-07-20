from colorama import Fore, Style

COLOR_COMMAND = Fore.CYAN
COLOR_DESCRIPTION = Fore.GREEN
COLOR_WELCOME = Fore.MAGENTA + Style.BRIGHT
COLOR_ERROR = Fore.RED
COLOR_RESPONSE = Fore.YELLOW

def color_text(text: str, color: str) -> str:
    return f"{color}{text}{Style.RESET_ALL}"

def prompt_user(message: str) -> str:
    return input(color_text(message, COLOR_WELCOME))

def color_print(text: str, color: str) -> None:
    print(color_text(text, color))

def print_error(text: str) -> None:
    color_print(text, COLOR_ERROR)

def print_title(text: str) -> None:
    color_print(text, COLOR_WELCOME)

def print_line(text: str) -> None:
    color_print(text, COLOR_COMMAND)

def print_menu() -> None:
    print_title("Available commands:")

    print_line("  hello                 - Greet the assistant.")
    print_line("  birthdays [days]      - Show upcoming birthdays (default: 7 days).")

    color_print("\n--- Contact Management ---", COLOR_DESCRIPTION)
    print_line("  all                   - Show all contacts.")
    print_line("  add <name> <phone>    - Add a new contact.")
    print_line("  change <name>         - Interactively edit a contact.")
    print_line("  delete <name>         - Delete a contact.")
    print_line("  find <name>           - Find a contact by name.")

    color_print("\n--- Note & Tag Management ---", COLOR_DESCRIPTION)
    print_line("  add-note <name> <text>- Add a note to a contact.")
    print_line("  edit-note <name>      - Edit a note's text or tags.")
    print_line("  find-notes <text>     - Search for contacts by note content.")
    print_line("  find-tag <tag>        - Search for contacts by a tag in notes.")
    print_line("  tags                  - Show all tags and list contacts for a selected tag.")

    color_print("\n--- Other Commands ---", COLOR_DESCRIPTION)
    print_line("  help                  - Print all commands")
    print_line("  exit, close           - Exit the assistant.")
