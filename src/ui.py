from colorama import Fore, Style

COLOR_COMMAND = Fore.CYAN
COLOR_DESCRIPTION = Fore.GREEN
COLOR_WELCOME = Fore.MAGENTA + Style.BRIGHT
COLOR_ERROR = Fore.RED
COLOR_RESPONSE = Fore.YELLOW

def color_text(text: str, color: str) -> str:
    return f"{color}{text}{Style.RESET_ALL}"


def color_print(text: str, color: str) -> None:
    print(color_text(text, color))

def print_error(text: str) -> None:
    color_print(text, COLOR_ERROR)

def print_title(text: str) -> None:
    color_print(text, COLOR_WELCOME)

def print_line(text: str) -> None:
    color_print(text, COLOR_COMMAND)
