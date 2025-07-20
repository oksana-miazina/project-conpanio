import difflib
from typing import Optional
from book import AddressBook, Record
from ui import print_line, print_title, print_error, prompt_user

def find_contact_interactive(book: AddressBook, name_query: str) -> Optional[Record]:
    """
    Interactively finds a contact. Handles cases where multiple contacts
    have the same name, and suggests close matches for typos.
    """
    # 1. Try for exact matches
    exact_matches = book.find_by_name(name_query)

    if len(exact_matches) == 1:
        return exact_matches[0]
    
    if len(exact_matches) > 1:
        print_title(f"Found multiple contacts named '{name_query.capitalize()}'. Please choose one:")
        for i, record in enumerate(exact_matches, 1):
            phone_info = record.phones[0].value if record.phones else "No phone"
            print_line(f"  {i}. {record.name.value} ({phone_info})")
        
        while True:
            sel = prompt_user("Enter the number of the correct contact or 'exit' to cancel: ").strip()
            if sel.lower() == 'exit': return None
            if sel.isdigit() and 1 <= int(sel) <= len(exact_matches):
                return exact_matches[int(sel) - 1]
            print_error("Invalid input. Try again.")

    # 2. If no exact matches, try for close matches (typos)
    all_names = sorted(list(set(rec.name.value for rec in book.get_all()))) # Unique names
    close_matches = difflib.get_close_matches(name_query.capitalize(), all_names, n=3, cutoff=0.6)

    if not close_matches:
        print_line(f"Contact '{name_query.capitalize()}' not found.")
        return None

    print_title(f"No contact named '{name_query.capitalize()}'. Did you mean:")
    for i, name in enumerate(close_matches, 1):
        print_line(f"  {i}. {name}")

    while True:
        sel = prompt_user("Enter number of the correct name or 'exit' to cancel: ").strip()
        if sel.lower() == 'exit':
            return None
        if sel.isdigit() and 1 <= int(sel) <= len(close_matches):
            # Search again with the corrected name, which might again yield multiple results
            return find_contact_interactive(book, close_matches[int(sel) - 1])
        print_error("Invalid input. Try again.")