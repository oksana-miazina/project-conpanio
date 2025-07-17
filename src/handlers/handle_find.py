import difflib
from book.AddressBook import AddressBook

def handle_find(args:list[str], book: AddressBook) -> str:
    if len(args) < 1:
        return "Error: Please provide a name to search for.Like this:=> 'find Jon'"
    
    input_name = args[0].capitalize()
    exact_match = book.find(input_name)

    if exact_match:
        return format_record(exact_match)
    
    all_names = [rec.name.value for rec in book.get_all()]
    close_matches = difflib.get_close_matches(input_name, all_names, n=5, cutoff = 0.6 )

    if close_matches:
        print(f"No exact match for '{input_name}'. Did you mean:")
        for idx, name in enumerate(close_matches, 1):
            print(f"{idx}. {name}")

        while True:
            choice = input(f"Enter the number of the correct name (or 'exit' to cancel): ").strip()
            if choice.lower() == 'exit':
                return "Search cancelled."
            if choice.isdigit() and 1 <= int(choice) <= len(close_matches):
                selected_name = close_matches[int(choice) - 1]
                record = book.find(selected_name)
                return format_record(record)
            print("Invalid input. Please enter a valid number or 'exit'.")
    else:
        # Додатковий гнучкий пошук за префіксом
        prefix_matches = [rec for rec in book.get_all() if rec.name.value.lower().startswith(input_name.lower())]

        if not prefix_matches:
            return f"No contacts found matching '{input_name}'"
        
        print(f"No close matches. Showing contacts starting with '{input_name}':")
        for idx, rec in enumerate(prefix_matches, 1):
            print(f"{idx}. {rec.name.value}")

        while True:
            choice = input(f"Enter the number of the correct name (or 'exit' to cancel): ").strip()
            if choice.lower() == 'exit':
                return "Search cancelled."
            if choice.isdigit() and 1 <= int(choice) <= len(prefix_matches):
                selected_record = prefix_matches[int(choice) - 1]
                return format_record(selected_record)
            print("Invalid input. Please enter a valid number or 'exit'.")

def format_record(record):
    last_name = record.last_name[0].value if record.last_name else ""
    phones = ", ".join(p.value for p in record.phones) if record.phones else ""
    emails = ", ".join(e.value for e in record.emails) if record.emails else ""
    birthday = record.birthday.value if record.birthday else ""
    notes = ", ".join(n.value for n in record.notes) if record.notes else ""
    tags = ", ".join(t.value for t in record.tags) if record.tags else ""
    return (
        f"Name: {record.name.value} {last_name}\n"
        f"Phones: {phones}\n"
        f"Emails: {emails}\n"
        f"Birthday: {birthday}\n"
        f"Notes: {notes}\n"
        f"Tags: {tags}"
    )
