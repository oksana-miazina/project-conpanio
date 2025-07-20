from datetime import datetime
from typing import List, Optional
from .Fields import Name, LastName, Phone, Email, Birthday, Note, Tag

class Record:
    
    def __init__(self, name: Name) -> None:
        self.name = name
        self.last_name = None
        self.phones = []
        self.emails = []
        self.birthday = None
        self.notes: List[Note] = []

    def add_last_name(self, last_name: str) -> None:
        self.last_name = LastName(last_name)

    def remove_last_name(self) -> None:
        self.last_name = None

    def add_phone(self, phone: str) -> None:
        self.phones.append(Phone(phone))

    def add_email(self, email: str) -> None:
        self.emails.append(Email(email))

    def add_birthday(self, birthday: str) -> None:
        self.birthday = Birthday(birthday)
        
    def add_note(self, note_text: str) -> Note:
        note = Note(note_text)
        self.notes.append(note)
        return note

    @staticmethod
    def _format_list(items: list, default: str = "N/A") -> str:
        if not items:
            return default
        return "\n    " + "\n    ".join(str(item) for item in items)

    def __str__(self) -> str:
        last_name_str = self.last_name.value if self.last_name else ""
        phones_str = self._format_list(self.phones)
        emails_str = self._format_list(self.emails)
        birthday_str = str(self.birthday) if self.birthday else "N/A"
        notes_str = self._format_list(self.notes) # This will now use Note.__str__

        return (
            f"Name: {self.name.value} {last_name_str}\n"
            f"  Phones: {phones_str}\n"
            f"  Emails: {emails_str}\n"
            f"  Birthday: {birthday_str}\n"
            f"  Notes: {notes_str}"
        )
