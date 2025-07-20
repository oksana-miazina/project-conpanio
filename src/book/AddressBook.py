from typing import Iterable, List
from .Record import Record
from .Fields import Name

class AddressBook:
  def __init__(self) -> None:
    self.data: List[Record] = []

  def __setstate__(self, state):
    """Handles unpickling of old AddressBook objects that used a dict."""
    if 'dict' in state:
        self.data = list(state['dict'].values())
    else:
        self.data = state.get('data', [])

  def add_record(self, record: Record) -> None:
    self.data.append(record)

  def get_all(self) -> Iterable[Record]:
    return self.data

  def find_by_name(self, name: str) -> List[Record]:
    """Finds all records with a matching name, case-insensitive."""
    capitalized_name = name.capitalize()
    return [rec for rec in self.data if rec.name.value == capitalized_name]
  
  def delete_record(self, record_to_delete: Record) -> bool:
    """Deletes a specific record object from the address book."""
    try:
        self.data.remove(record_to_delete)
        return True
    except ValueError: # The record was not in the list
        return False
