import difflib
from book.AddressBook import AddressBook
from handlers.handle_find import format_record
from handlers.yes_no_promt_file import yes_no_prompt
# def handle_delete(args: list[str], book: AddressBook) -> str:
#     if len(args) < 1:
#         return "Error: Please provide a name to delete. Example: delete John"

#     input_name = args[0].capitalize()
#     record = book.find(input_name)

#     if record:
#         print("Found contact:")
#         print(format_record(record))
#         confirm = input("Are you sure you want to delete this contact? (yes/no): ").strip().lower()
#         if confirm == 'yes':
#             book.delete(input_name)  # <-- Ось тут видалення
#             return f"Contact '{input_name}' deleted successfully."
#         else:
#             return "Delete cancelled."

#     all_names = [rec.name.value for rec in book.get_all()]
#     close_matches = difflib.get_close_matches(input_name, all_names, n=5, cutoff=0.6)

#     if close_matches:
#         print(f"No exact match for '{input_name}'. Did you mean:")
#         for idx, name in enumerate(close_matches, 1):
#             print(f"{idx}. {name}")

#         while True:
#             choice = input("Enter the number of the correct name to delete (or 'exit' to cancel): ").strip()
#             if choice.lower() == 'exit':
#                 return "Delete cancelled."
#             if choice.isdigit() and 1 <= int(choice) <= len(close_matches):
#                 selected_name = close_matches[int(choice) - 1]
#                 record = book.find(selected_name)
#                 print("Selected contact:")
#                 print(format_record(record))
#                 confirm = input("Are you sure you want to delete this contact? (yes/no): ").strip().lower()
#                 if confirm == 'yes':
#                     book.delete(selected_name)  # <-- І тут теж
#                     return f"Contact '{selected_name}' deleted successfully."
#                 else:
#                     return "Delete cancelled."
#             print("Invalid input. Please enter a valid number or 'exit'.")

#     return f"Contact '{input_name}' not found."

def handle_delete(args: list[str], book: AddressBook) -> str:
    if len(args) < 1:
        return "Error: Please provide a name to delete. Example: delete John"

    input_name = args[0].capitalize()
    record = book.find(input_name)

    if record:
        print("Found contact:")
        print(format_record(record))
        if yes_no_prompt("Are you sure you want to delete this contact? (y/n): "):
            book.delete(input_name)
            return f"Contact '{input_name}' deleted successfully."
        else:
            return "Delete cancelled."

    all_names = [rec.name.value for rec in book.get_all()]
    close_matches = difflib.get_close_matches(input_name, all_names, n=5, cutoff=0.6)

    if close_matches:
        print(f"No exact match for '{input_name}'. Did you mean:")
        for idx, name in enumerate(close_matches, 1):
            print(f"{idx}. {name}")

        while True:
            choice = input("Enter the number of the correct name to delete (or 'exit' to cancel): ").strip()
            if choice.lower() == 'exit':
                return "Delete cancelled."
            if choice.isdigit() and 1 <= int(choice) <= len(close_matches):
                selected_name = close_matches[int(choice) - 1]
                record = book.find(selected_name)
                print("Selected contact:")
                print(format_record(record))
                if yes_no_prompt("Are you sure you want to delete this contact? (y/n): "):
                    book.delete(selected_name)
                    return f"Contact '{selected_name}' deleted successfully."
                else:
                    return "Delete cancelled."
            print("Invalid input. Please enter a valid number or 'exit'.")

    return f"Contact '{input_name}' not found."