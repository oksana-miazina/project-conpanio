from datetime import datetime

class Field:
    def __init__(self,value):
        self.value = value
    def __str__(self):
        return str(self.value)

class Name(Field):
     def __init__(self, value):
         formatted = value.strip().capitalize()
         super().__init__(formatted)

class LastName(Field):
     def __init__(self, value):
         formatted = value.strip().capitalize()
         super().__init__(formatted)

class Phone(Field):
    def __init__(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Phone must be 10 digits, like this: 0123456789")
        super().__init__(value)  
        
class Email(Field):
    def __init__(self, value):
        if "@" not in value:
            raise ValueError("Invalid email format")
        super().__init__(value)
        
class Birthday(Field):
    def __init__(self, value):
        try:
            datetime.strptime(value, "%d.%m.%Y")
        except ValueError:
            raise ValueError("Birthday must be in DD.MM.YYYY format")
        super().__init__(value)

class Note(Field):
    pass

class Tag(Field):
    pass