from cli_utils import *
from common_utils import *

def main():
    length = get_length_from_user()
    chars = get_chars_from_user()

    pwd = generate_password(length, chars)
    copy_to_clip(pwd)

    print("The generated password is:", pwd)
    print("The password has been copied to the clipboard.")


if __name__ == '__main__':
    main()
