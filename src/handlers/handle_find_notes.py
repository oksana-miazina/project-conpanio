from typing import List, Tuple
from book import AddressBook, Record
from ui import print_title, print_line, print_error

def handle_find_notes(args: List[str], book: AddressBook) -> None:
    if not args:
        print_error("Error: Please provide the text to search for in notes. Usage: find-notes <text>")
        return

    search_query = " ".join(args)
    lower_query = search_query.lower()
    results: List[Tuple[Record, List[str]]] = []

    for record in book.get_all():
        matching_notes_for_record = []
        for note in record.notes:
            if lower_query in note.value.lower():
                matching_notes_for_record.append(str(note))

        if matching_notes_for_record:
            results.append((record, matching_notes_for_record))

    if not results:
        print_line(f"No contacts found with notes containing '{search_query}'.")
        return

    print_title(f"Found notes containing '{search_query}':")
    for record, notes in results:
        full_name = record.name.value
        if record.last_name:
            full_name += f" {record.last_name.value}"

        print("")
        print_line(f"Contact: {full_name}")
        for note_text in notes:
            print(f"  - {note_text}")