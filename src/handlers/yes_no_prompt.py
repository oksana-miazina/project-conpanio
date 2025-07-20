from ui import prompt_user, print_error

def yes_no_prompt(message: str) -> bool:
    while True:
        ans = prompt_user(message).strip().lower()
        if ans in ("y", "yes"):
            return True
        elif ans in ("n", "no"):
            return False
        else:
            print_error("Please answer 'yes' or 'no' (y/n).")
