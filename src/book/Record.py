from datetime import datetime
from book.Fields import Name, LastName, Phone, Email, Birthday, Note, Tag

class Record:
    
    def __init__(self, name: Name):
        self.name = name
        self.last_name = []
        self.phones = []
        self.emails = []
        self.birthday = None
        self.notes = []
        self.tags = []

    def add_LastName(self,last_name):
        self.last_name.append(LastName(last_name))

    def add_phone(self,phones):
        self.phones.append(Phone(phones))

    def add_email(self,emails):
        self.emails.append(Email(emails))

    def add_birthday(self,birthday):
        self.birthday = Birthday(birthday)
        
    def add_note(self, note):
        self.notes.append(Note(note))

    def add_tag(self, tag):
        self.tags.append(Tag(tag))
