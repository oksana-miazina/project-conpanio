from typing import List
from book import AddressBook
from .contact_finder import find_contact_interactive
from .yes_no_prompt import yes_no_prompt
from ui import print_error, print_line, prompt_user

def handle_add_note(args: List[str], book: AddressBook) -> None:
    if len(args) < 2:
        print_error("Error: Please provide a contact name and the note text. Usage: add-note <name> <note text>")
        return

    name_query = args[0].capitalize()
    note_text = " ".join(args[1:])
    record = find_contact_interactive(book, name_query)
    
    if not record:
        print_error("Operation cancelled.")
        return
    
    new_note = record.add_note(note_text)
    print_line(f"Note added to contact '{record.name.value}'.")

    if yes_no_prompt("Do you want to add tags to this note? (y/n): "):
        while True:
            tag_text = prompt_user("Enter tag (or leave empty to finish): ").strip()
            if not tag_text:
                break
            new_note.add_tag(tag_text)
            print_line(f"Tag '{tag_text}' added to the note.")