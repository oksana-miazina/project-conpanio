from typing import Iterable, Optional
from .Record import Record
from .Fields import Name

class AddressBook:
  def __init__(self) -> None:
    self.dict = {}

  def add_record(self, record: Record) -> None:
    self.dict[record.name.value] = record

  def get_all(self) -> Iterable[Record]:
    return self.dict.values()

  def find(self, name: str) -> Optional[Record]:
    return self.dict.get(name.capitalize())
  
  def delete(self, name: str) -> bool:
        key = name.capitalize()
        if key in self.dict:
            del self.dict[key]
            return True
        return False

  def rename_contact(self, record: Record, new_name_str: str) -> None:
      old_name_key = record.name.value
      new_name_obj = Name(new_name_str)
      new_name_key = new_name_obj.value

      if old_name_key == new_name_key:
          return # No change needed

      if new_name_key in self.dict:
          raise ValueError(f"Contact with name '{new_name_key}' already exists.")

      del self.dict[old_name_key]
      record.name = new_name_obj
      self.dict[new_name_key] = record
