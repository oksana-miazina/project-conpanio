import os
import pickle

from book.AddressBook import AddressBook

DATA_DIR = ".user_data"
DATA_FILE = os.path.join(DATA_DIR, "addressbook.pkl")

def save_data(book, filename=DATA_FILE):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "wb") as f:
        pickle.dump(book, f)

def load_data(filename=DATA_FILE):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()
