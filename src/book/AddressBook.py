from typing import Iterable, List
from .Record import Record

class AddressBook:
  def __init__(self) -> None:
    self.data = []

  def add_record(self, record: Record) -> None:
    self.data.append(record)

  def get_all(self) -> Iterable[Record]:
    return self.data

  def find_by_name(self, name: str) -> List[Record]:
    capitalized_name = name.capitalize()
    return [rec for rec in self.data if rec.name.value == capitalized_name]
  
  def delete_record(self, record_to_delete: Record) -> bool:
    try:
        self.data.remove(record_to_delete)
        return True
    except ValueError: # The record was not in the list
        return False
