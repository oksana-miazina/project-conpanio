from datetime import datetime
from book import AddressBook
from typing import List

def handle_birthdays(args: List[str], book: AddressBook, days: int = 7) -> str:
    today = datetime.today().date()
    upcoming_birthdays = []

    for record in book.get_all():
        birthday_obj = record.birthday
        if birthday_obj and hasattr(birthday_obj, "value"):
            try:
                bday = datetime.strptime(birthday_obj.value, "%d.%m.%Y").date()
                bday_this_year = bday.replace(year=today.year)

                delta_days = (bday_this_year - today).days
                if 0 <= delta_days <= days:
                    upcoming_birthdays.append(f"{record.name.value} — {bday.strftime('%Y-%m-%d')}")
            except Exception:
                continue  # пропускаємо якщо дата некоректна

    if not upcoming_birthdays:
        return f"No birthdays in the next {days} days."

    return "Upcoming birthdays:\n" + "\n".join(upcoming_birthdays)
