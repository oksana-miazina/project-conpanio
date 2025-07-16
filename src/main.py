from colorama import init
from nav import start_nav, ExitException
from data import load_data, save_data

def main() -> None:
    init(autoreset=True)  # for colorama (cross-platform color support)
    book = load_data()

    try:
       start_nav(book)
    except ExitException:
       save_data(book)

if __name__ == "__main__":
    main()
