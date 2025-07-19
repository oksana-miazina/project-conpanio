from .handle_add import handle_add
from .handle_all import handle_all
from .handle_birthdays import handle_birthdays
from .handle_change import handle_change
from .handle_delete import handle_delete
from .handle_find import handle_find
from .handle_hello import handle_hello
from .handle_help import handle_help

COMMAND_HANDLERS = {
    # CRUD operations
    "add": handle_add,
    "all": handle_all,
    "change": handle_change,
    "delete": handle_delete,
    "find": handle_find,
    # Other commands
    "birthdays": handle_birthdays,
    "hello": handle_hello,
    "help": handle_help,
}

__all__ = [
    "COMMAND_HANDLERS",
]