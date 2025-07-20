from typing import List
from book import AddressBook
from ui import print_error, print_line, print_title, prompt_user

def handle_tags(args: List[str], book: AddressBook) -> None:
    all_tags = set()
    for record in book.get_all():
        for note in record.notes:
            for tag in note.tags:
                all_tags.add(tag.value.lower())

    if not all_tags:
        print_line("No tags found in the address book.")
        return

    sorted_tags = sorted(list(all_tags))

    print_title("Available tags:")
    for i, tag in enumerate(sorted_tags, 1):
        print_line(f"  {i}. {tag}")

    while True:
        sel = prompt_user("\nEnter the number of the tag to see contacts, or 'exit' to cancel: ").strip()
        if sel.lower() == 'exit':
            print_line("Operation cancelled.")
            return
        
        if sel.isdigit() and 1 <= int(sel) <= len(sorted_tags):
            selected_tag = sorted_tags[int(sel) - 1]
            break
        else:
            print_error("Invalid input. Please try again.")

    results = []
    for record in book.get_all():
        matching_notes = []
        for note in record.notes:
            if any(selected_tag == tag.value.lower() for tag in note.tags):
                matching_notes.append(str(note))
        
        if matching_notes:
            results.append((record, matching_notes))

    print_title(f"\nNotes with tag '{selected_tag}':")
    for record, notes in results:
        full_name = record.name.value
        if record.last_name:
            full_name += f" {record.last_name.value}"
            
        print("")
        print_line(f"Contact: {full_name}")
        for note_text in notes:
            print(f"  - {note_text}")