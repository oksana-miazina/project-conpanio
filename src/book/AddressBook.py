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