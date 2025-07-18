from book.Record import Record


class AddressBook:
  def __init__(self):
    self.dict = {}

  def add_record(self, record: Record):
    self.dict[record.name.value] = record

  def get_all(self):
    return self.dict.values()

  def find(self, name: str):
    return self.dict.get(name.capitalize())
  
  def delete(self, name: str) -> bool:
        key = name.capitalize()
        if key in self.dict:
            del self.dict[key]
            return True
        return False

