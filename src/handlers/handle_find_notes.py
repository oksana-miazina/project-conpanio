from typing import List
from book import AddressBook, Record
from ui import print_error
from handlers.search_utils import search_records, print_search_results

def _notes_predicate(record: Record, query: str) -> List[str]:
    lower_query = query.lower()
    return [str(note) for note in record.notes if lower_query in note.value.lower()]

def handle_find_notes(args: List[str], book: AddressBook) -> None:
    if not args:
        print_error("Error: Please provide the text to search for in notes. Usage: find-notes <text>")
        return

    search_query = " ".join(args)
    results = search_records(book, search_query, _notes_predicate)
    
    title = f"Found notes containing '{search_query}':"
    not_found_msg = f"No contacts found with notes containing '{search_query}'."
    print_search_results(results, title, not_found_msg)
