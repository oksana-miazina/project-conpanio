import difflib
from typing import Optional
from book import AddressBook, Record
from ui import print_line, print_title, print_error, prompt_user

def find_contact_interactive(book: AddressBook, name_query: str) -> Optional[Record]:

    exact_matches = book.find_by_name(name_query)

    if not exact_matches:
        prefix_matches = [rec for rec in book.get_all() if rec.name.value.lower().startswith(name_query.lower())]
        exact_matches = prefix_matches

    if len(exact_matches) == 1:
        return exact_matches[0]
    
    if len(exact_matches) > 1:
        print_title(f"Found multiple contacts named '{name_query.capitalize()}'. Please choose one:")
        for i, record in enumerate(exact_matches, 1):
            parts = [f"{record.name.value}"]
        
            if record.phones:
                parts.append(f"Phone: {', '.join(p.value for p in record.phones)}")
            if record.emails:
                parts.append(f"Email: {', '.join(e.value for e in record.emails)}")
            if record.birthday:
                parts.append(f"Birthday: {record.birthday.value}")
            if record.notes:
                notes_text = "; ".join(n.value for n in record.notes)
                parts.append(f"Notes: {notes_text}")

            info_str = ", ".join(parts)
            print_line(f"  {i}. {info_str}")

        # Запит вибору
        while True:
            sel = prompt_user("Enter the number of the correct contact or 'exit' to cancel: ").strip()
            if sel.lower() == 'exit':
                return None
            if sel.isdigit() and 1 <= int(sel) <= len(exact_matches):
                return exact_matches[int(sel) - 1]
            print_error("Invalid input. Try again.")

    # 2. If no exact or prefix matches, try close matches (typos)
    all_names = sorted(list(set(rec.name.value for rec in book.get_all()))) 
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
            return find_contact_interactive(book, close_matches[int(sel) - 1])
        print_error("Invalid input. Try again.")
