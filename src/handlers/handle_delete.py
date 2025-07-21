from book import AddressBook
from handlers.yes_no_prompt import yes_no_prompt
from handlers.contact_finder import find_contact_interactive
from ui import print_error, print_line, print_title

def handle_delete(args: list[str], book: AddressBook) -> None:
    if len(args) < 1:
        print_error("Error: Please provide a name to delete. Example: delete John")
        return

    name_query = args[0]
    record_to_delete = find_contact_interactive(book, name_query)

    if record_to_delete:
        print_title("\nThis contact will be deleted:")
        print(record_to_delete)
        if yes_no_prompt("Are you sure you want to delete this contact? (y/n): "):
            book.delete_record(record_to_delete)
            print_line(f"Contact '{record_to_delete.name.value}' deleted successfully.")
        else:
            print_error("Delete cancelled.")
    else:
        print_error("Operation cancelled.")
