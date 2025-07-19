def yes_no_prompt(message: str) -> bool:
    while True:
        ans = input(message).strip().lower()
        if ans in ("y", "yes"):
            return True
        elif ans in ("n", "no"):
            return False
        else:
            print("Please answer 'yes' or 'no' (y/n).")
