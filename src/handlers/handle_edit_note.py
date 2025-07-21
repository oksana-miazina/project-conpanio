from typing import List
from book import AddressBook, Record, Note
from handlers.contact_finder import find_contact_interactive
from ui import print_error, print_line, print_title, prompt_user

def _select_note_interactive(record: Record) -> Note | None:
    if not record.notes:
        print_line(f"Contact '{record.name.value}' has no notes to edit.")
        return None

    print_title(f"Select a note to edit for {record.name.value}:")
    for i, note in enumerate(record.notes, 1):
        print_line(f"  {i}. {str(note)}")

    while True:
        sel = prompt_user("Enter the number of the note or 'exit' to cancel: ").strip()
        if sel.lower() == 'exit':
            return None
        if sel.isdigit() and 1 <= int(sel) <= len(record.notes):
            return record.notes[int(sel) - 1]
        print_error("Invalid input. Try again.")


def _edit_tags(note: Note):
    while True:
        if note.tags:
            print_title("Current tags:")
            for i, tag in enumerate(note.tags, 1):
                print_line(f"  {i}. {tag.value}")
        else:
            print_line("This note has no tags.")

        action = prompt_user("Tags: (a)dd, (r)emove, or (s)kip? ").strip().lower()
        if action == 's':
            break
        elif action == 'a':
            tag_text = prompt_user("Enter new tag: ").strip()
            if tag_text:
                note.add_tag(tag_text)
                print_line(f"Tag '{tag_text}' added.")
        elif action == 'r':
            if not note.tags:
                print_line("No tags to remove.")
                continue
            idx_str = prompt_user("Enter index of tag to remove: ").strip()
            if idx_str.isdigit() and 1 <= int(idx_str) <= len(note.tags):
                removed = note.tags.pop(int(idx_str) - 1)
                print_line(f"Tag '{removed.value}' removed.")
            else:
                print_error("Invalid index.")
        else:
            print_error("Invalid action.")


def handle_edit_note(args: List[str], book: AddressBook) -> None:
    if not args:
        print_error("Error: Please provide a contact name. Usage: edit-note <name>")
        return

    record = find_contact_interactive(book, args[0])
    if not record:
        print_error("Operation cancelled.")
        return

    note_to_edit = _select_note_interactive(record)
    if not note_to_edit:
        print_line("No note selected. Operation cancelled.")
        return

    print_title("Editing note:")
    print_line(f"  {str(note_to_edit)}")

    new_text = prompt_user(f"New text (leave empty to keep current): ").strip()
    if new_text:
        note_to_edit.value = new_text
        print_line("Note text updated.")

    _edit_tags(note_to_edit)

    print_line("Note editing finished.")
