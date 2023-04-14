def get_length_from_user() -> int:
    while True:
        length = input("Enter the length of the password: ")
        try:
            length = int(length)
            if length == 0:
                print("Password length must be greater than zero! Please try again.")
                continue
            break
        except ValueError:
            print("Not a valid length! Please try again.")

    return length

def get_chars_from_user() -> list:
    avail_chars = ("lowercase", "uppercase", "digits", "special")
    chars = []


    while True:
        for item in avail_chars:
            choice = input(f"Do you want to include {item} characters in your password? [Y/n] [Default - y]\n(Everything except n will be treated as yes): ")
            if choice.lower() == "n":
                continue

            chars.append(item)

        if chars:
            break
        print("At least one category should be selected! Please try again.")
        print("-------------------------------------------------------------------")

    return chars
