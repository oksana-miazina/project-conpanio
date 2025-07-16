from datetime import datetime
from book.Fields import Name, LastName, Phone, Email, Birthday, Note, Tag

class Record:
    
    def __init__(self, name: Name):
        self.name = Name
        self.last_name = None
        self.phone = None
        self.email = None
        self.birthday = None
        self.notes = []
        self.tags = None

    def add_LastName(self,last_name):
        self.last_name.append(LastName(last_name))

    def add_phone(self,phone):
        self.phone.append(Phone(phone))

    def add_email(self,email):
        self.email.append(Email(email))

    def add_birthday(self,birthday):
        self.birthday.append(Birthday(birthday))
        
    def add_note(self, note):
        self.notes.append(Note(note))

    def add_tag(self, tag):
        self.tags.append(Tag(tag))
