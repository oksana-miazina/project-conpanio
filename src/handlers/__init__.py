from .handle_add import handle_add
from .handle_all import handle_all
from .handle_birthdays import handle_birthdays
from .handle_change import handle_change
from .handle_delete import handle_delete
from .handle_find import handle_find
from .handle_find_notes import handle_find_notes
from .handle_find_tag import handle_find_tag
from .handle_tags import handle_tags
from .handle_edit_note import handle_edit_note
from .handle_add_note import handle_add_note
from .handle_hello import handle_hello
from .handle_help import handle_help

COMMAND_HANDLERS = {
    "hello": handle_hello,
    "birthdays": handle_birthdays,
    "all": handle_all,
    "add": handle_add,
    "change": handle_change,
    "delete": handle_delete,
    "find": handle_find,
    "add-note": handle_add_note,
    "edit-note": handle_edit_note,
    "find-notes": handle_find_notes,
    "find-tag": handle_find_tag,
    "tags": handle_tags,
    "help": handle_help,
}

__all__ = [
    "COMMAND_HANDLERS",
]