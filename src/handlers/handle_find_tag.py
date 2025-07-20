from typing import List
from book import AddressBook
from ui import print_error, print_line, print_title

def handle_find_tag(args: List[str], book: AddressBook) -> None:
    if not args:
        print_error("Error: Please provide a tag to search for. Usage: find-tag <tag>")
        return

    search_query = " ".join(args)
    lower_query = search_query.lower()
    results = []

    for record in book.get_all():
        matching_notes_for_record = []
        for note in record.notes:
            if any(lower_query in tag.value.lower() for tag in note.tags):
                matching_notes_for_record.append(str(note))
        
        if matching_notes_for_record:
            results.append((record, matching_notes_for_record))

    if not results:
        print_line(f"No contacts found with notes tagged '{search_query}'.")
        return

    print_title(f"Found notes with tag '{search_query}':")
    for record, notes in results:
        full_name = record.name.value
        if record.last_name:
            full_name += f" {record.last_name.value}"
        
        print("")
        print_line(f"Contact: {full_name}")
        for note_text in notes:
            print(f"  - {note_text}")