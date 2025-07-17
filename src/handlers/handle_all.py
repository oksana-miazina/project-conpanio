from book.AddressBook import AddressBook
from typing import List
from book.Record import Record

def handle_all(args: List[str], book: AddressBook) -> str:
  contacts = book.get_all()
  if not contacts:
    return "No contactc found."
  
  header = f"{'First Name':<15} {'Last Name':<15} {'Phones':<20} {'Emails':<25} {'Birthday':<12} {'Notes':<25} {'Tags':<15}"
  lines = [header]
  lines.append("-" * len(header))
    
  for record in contacts:
      phones = ", ".join(p.value for p in getattr(record, 'phones', [])) if getattr(record, 'phones', None) else ""
      emails = ", ".join(e.value for e in getattr(record, 'emails', [])) if getattr(record, 'emails', None) else ""
      notes = ", ".join(n.value for n in getattr(record, 'notes', [])) if getattr(record, 'notes', None) else ""
      tags = ", ".join(t.value for t in getattr(record, 'tags', [])) if getattr(record, 'tags', None) else ""
      birthday = record.birthday.value if record.birthday else ""
      last_name = ""
      if record.last_name:
          if isinstance(record.last_name, list):
              last_name = record.last_name[0].value if record.last_name else ""
          else:
              last_name = record.last_name.value
        
      line = f"{record.name.value:<15} {last_name:<15} {phones:<20} {emails:<25} {birthday:<12} {notes:<25} {tags:<15}"
      lines.append(line)
    
  return "\n".join(lines)
  