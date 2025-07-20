from typing import List
from book import AddressBook
from ui import print_error, print_line, print_title

def handle_find_phonenumber(args: List[str], book: AddressBook) -> None:
    if not args:
        print_error("Error: Please provide a phone number or part of it to search for. Usage: find-phonenumber <number>")
        return

    search_query = "".join(args).strip()
    results = []

    for record in book.get_all():
        matching_phones = []
        for phone in record.phones:
            if search_query in phone.value:
                matching_phones.append(phone.value)

        if matching_phones:
            results.append((record, matching_phones))

    if not results:
        print_line(f"No contacts found with phone number containing '{search_query}'.")
        return

    print_title(f"Found contacts with phone number '{search_query}':")
    for record, phones in results:
        full_name = record.name.value
        if record.last_name:
            full_name += f" {record.last_name.value}"
        
        print("")
        print_line(f"Contact: {full_name}")
        for number in phones:
            print(f"  - {number}")
