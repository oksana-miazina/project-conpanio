from typing import List, Callable, Tuple
from book import AddressBook, Record
from ui import print_line, print_title

SearchPredicate = Callable[[Record, str], List[str]]

def search_records(book: AddressBook, query: str, predicate: SearchPredicate) -> List[Tuple[Record, List[str]]]:
    results = []
    for record in book.get_all():
        matches = predicate(record, query)
        if matches:
            results.append((record, matches))
    return results

def print_search_results(results: List[Tuple[Record, List[str]]], title: str, not_found_msg: str):
    if not results:
        print_line(not_found_msg)
        return

    print_title(title)
    for record, matches in results:
        full_name = record.name.value + (f" {record.last_name.value}" if record.last_name else "")
        print(f"\nContact: {full_name}")
        for match_item in matches:
            print(f"  - {match_item}")
