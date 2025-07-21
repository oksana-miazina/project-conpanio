from typing import List
from book import AddressBook, Record
from ui import print_error
from handlers.search_utils import search_records, print_search_results

def _phones_predicate(record: Record, query: str) -> List[str]:
    return [phone.value for phone in record.phones if query in phone.value]

def handle_find_phonenumber(args: List[str], book: AddressBook) -> None:
    if not args:
        print_error("Error: Please provide a phone number or part of it to search for. Usage: find-phonenumber <number>")
        return

    search_query = "".join(args).strip()
    results = search_records(book, search_query, _phones_predicate)
    
    title = f"Found contacts with phone number '{search_query}':"
    not_found_msg = f"No contacts found with phone number containing '{search_query}'."
    print_search_results(results, title, not_found_msg)

