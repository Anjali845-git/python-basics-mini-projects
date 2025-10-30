# password_generator.py
# Generates a random password of desired length

import random
import string

def generate_password(length=10):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    length = int(input("Enter desired password length: "))
    print("Generated Password:", generate_password(length))
