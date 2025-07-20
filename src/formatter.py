from typing import List
from book import Record


TABLE_CONFIG = {
    "name": {"display": "First Name", "width": 15},
    "last_name": {"display": "Last Name", "width": 15},
    "phones": {"display": "Phones", "width": 20},
    "emails": {"display": "Emails", "width": 25},
    "birthday": {"display": "Birthday", "width": 12},
    "notes": {"display": "Notes", "width": 25},
    "tags": {"display": "Tags", "width": 15},
}

def _truncate(text: str, width: int) -> str:
    """Truncates text to a given width, adding '...' if necessary."""
    if len(text) <= width:
        return text
    return text[:width - 3] + "..." if width > 3 else text[:width]

def _format_record_to_rows(record: Record) -> list[str]:
    """
    Форматує один запис у вигляд списку рядків для таблиці.
    Код написаний просто, щоб його було легко зрозуміти.
    """
    # 1. Готуємо дані для кожної колонки як списки рядків
    name_lines = [record.name.value]
    last_name_lines = [record.last_name.value if record.last_name else ""]
    phone_lines = [p.value for p in record.phones]
    email_lines = [e.value for e in record.emails]
    birthday_lines = [record.birthday.value if record.birthday else ""]
    note_lines = [n.value for n in record.notes]
    tag_lines = [", ".join(t.value for t in n.tags) for n in record.notes]

    # 2. Визначаємо, скільки рядків займе цей запис
    all_field_lines = [
        name_lines, last_name_lines, phone_lines, email_lines, birthday_lines, note_lines, tag_lines
    ]
    num_rows = max(len(field) for field in all_field_lines) if all_field_lines else 1

    # 3. Створюємо кожен рядок для таблиці
    output_rows = []
    for i in range(num_rows):
        # Для полів з одним значенням (ім'я, прізвище, д.н.) беремо дані тільки для першого рядка
        name = name_lines[0] if i == 0 else ""
        last_name = last_name_lines[0] if i == 0 else ""
        birthday = birthday_lines[0] if i == 0 else ""

        # Для полів-списків (телефони, email) беремо i-й елемент
        phone = phone_lines[i] if i < len(phone_lines) else ""
        email = email_lines[i] if i < len(email_lines) else ""
        note = note_lines[i] if i < len(note_lines) else ""
        tag = tag_lines[i] if i < len(tag_lines) else ""

        # 4. Форматуємо рядок, обрізаючи текст, якщо він задовгий
        row_parts = [
            f"{_truncate(name, TABLE_CONFIG['name']['width']):<{TABLE_CONFIG['name']['width']}}",
            f"{_truncate(last_name, TABLE_CONFIG['last_name']['width']):<{TABLE_CONFIG['last_name']['width']}}",
            f"{_truncate(phone, TABLE_CONFIG['phones']['width']):<{TABLE_CONFIG['phones']['width']}}",
            f"{_truncate(email, TABLE_CONFIG['emails']['width']):<{TABLE_CONFIG['emails']['width']}}",
            f"{_truncate(birthday, TABLE_CONFIG['birthday']['width']):<{TABLE_CONFIG['birthday']['width']}}",
            f"{_truncate(note, TABLE_CONFIG['notes']['width']):<{TABLE_CONFIG['notes']['width']}}",
            f"{_truncate(tag, TABLE_CONFIG['tags']['width']):<{TABLE_CONFIG['tags']['width']}}",
        ]
        output_rows.append(" ".join(row_parts))
    return output_rows

def format_records_as_table(records: List[Record]) -> str:
    header = " ".join([f"{v['display']:<{v['width']}}" for v in TABLE_CONFIG.values()])
    separator = "-" * len(header)
    lines = [header, separator]
    for i, record in enumerate(records):
        lines.extend(_format_record_to_rows(record))
        if i < len(records) - 1:
            lines.append(separator)
    return "\n".join(lines)
