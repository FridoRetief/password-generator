#optimised suboptimal code!
import random
import string

generated_passwords = set()

min_length = int(input("Enter the minimum length for the password: "))

include_numbers = input("Include numbers in the password? (yes/no): ").lower() == "yes"
include_special_chars = input("include special characters in the password? (yes/no): ").lower == "yes"

characters = string.ascii_letters
if include_numbers:
    characters += string.digits
if include_special_chars:
    characters += string.punctuation

def generate_password(min_length):
    while True:
        password = "".join(random.choice(characters) for _ in range(min_length))
        if password not in generated_passwords:
            generated_passwords.add(password)
            return password

for _ in range(5):
    password = generate_password(min_length)
    print("Generated Password:", password)
