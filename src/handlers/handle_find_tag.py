from typing import List
from book import AddressBook, Record
from ui import print_error
from handlers.search_utils import search_records, print_search_results

def _tags_predicate(record: Record, query: str) -> List[str]:
    lower_query = query.lower()
    matching_notes = []
    for note in record.notes:
        if any(lower_query in tag.value.lower() for tag in note.tags):
            matching_notes.append(str(note))
    return matching_notes

def handle_find_tag(args: List[str], book: AddressBook) -> None:
    if not args:
        print_error("Error: Please provide a tag to search for. Usage: find-tag <tag>")
        return

    search_query = " ".join(args)
    results = search_records(book, search_query, _tags_predicate)
    
    title = f"Found notes with tag '{search_query}':"
    not_found_msg = f"No contacts found with notes tagged '{search_query}'."
    print_search_results(results, title, not_found_msg)
