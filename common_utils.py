import random 
import string
import pyperclip

LOWERCASE_LETTERS = string.ascii_lowercase
UPPERCASE_LETTERS = string.ascii_uppercase
SPECIAL = string.punctuation
DIGITS = string.digits

def generate_password(length: int, chars: list):
    all_chars = ""

    if "lowercase" in chars:
        all_chars += LOWERCASE_LETTERS
    if "uppercase" in chars:
        all_chars += UPPERCASE_LETTERS
    if "digits" in chars:
        all_chars += DIGITS
    if "special" in chars:
        all_chars += SPECIAL

    pwd = ""
    for _ in range(length):
        pwd += random.choice(all_chars)

    return pwd

def copy_to_clip(pwd: str):
    pyperclip.copy(pwd)
