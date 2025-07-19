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
    if len(text) <= width:
        return text
    return text[:width - 3] + "..." if width > 3 else text[:width]

def _format_record_to_rows(record: Record) -> list[str]:
    name_col = [_truncate(record.name.value, TABLE_CONFIG["name"]["width"])]
    last_name_col = [_truncate(record.last_name.value if record.last_name else "", TABLE_CONFIG["last_name"]["width"])]
    phones_col = [_truncate(p.value, TABLE_CONFIG["phones"]["width"]) for p in record.phones] or [""]
    emails_col = [_truncate(e.value, TABLE_CONFIG["emails"]["width"]) for e in record.emails] or [""]
    birthday_col = [_truncate(record.birthday.value if record.birthday else "", TABLE_CONFIG["birthday"]["width"])]
    notes_col = [_truncate(n.value, TABLE_CONFIG["notes"]["width"]) for n in record.notes] or [""]
    tags_col = [_truncate(t.value, TABLE_CONFIG["tags"]["width"]) for t in record.tags] or [""]

    columns = [name_col, last_name_col, phones_col, emails_col, birthday_col, notes_col, tags_col]
    num_rows = max(len(col) for col in columns)

    for col in columns:
        col.extend([""] * (num_rows - len(col)))

    output_rows = []
    for i in range(num_rows):
        row_data = [col[i] for col in columns]
        output_rows.append(
            f"{row_data[0]:<{TABLE_CONFIG['name']['width']}} "
            f"{row_data[1]:<{TABLE_CONFIG['last_name']['width']}} "
            f"{row_data[2]:<{TABLE_CONFIG['phones']['width']}} "
            f"{row_data[3]:<{TABLE_CONFIG['emails']['width']}} "
            f"{row_data[4]:<{TABLE_CONFIG['birthday']['width']}} "
            f"{row_data[5]:<{TABLE_CONFIG['notes']['width']}} "
            f"{row_data[6]:<{TABLE_CONFIG['tags']['width']}}"
        )
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
