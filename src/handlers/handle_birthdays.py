def handle_birthdays(book: AddressBook, days: int = 7) -> str:
    today = datetime.today().date()
    upcoming_birthdays = []

    for record in book.data.values():  # assuming book.data is a dict of records
        if hasattr(record, "birthday") and record.birthday:
            bday = record.birthday
            bday_this_year = bday.replace(year=today.year)
            
            delta_days = (bday_this_year - today).days
            if 0 <= delta_days <= days:
                upcoming_birthdays.append(f"{record.name.value} — {bday.strftime('%Y-%m-%d')}")

    if not upcoming_birthdays:
        return f"No birthdays in the next {days} days."
    
    return "Upcoming birthdays:\n" + "\n".join(upcoming_birthdays)

