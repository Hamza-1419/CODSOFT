# CODSOFT Python Internship
# Task 3 - Password Generator

import random
import string

def generate_password(length):
    # combine all characters: letters, digits, symbols
    all_chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

print("=== PASSWORD GENERATOR ===")

while True:
    try:
        length = int(input("\nEnter password length (minimum 4): "))
        if length < 4:
            print("⚠️ Password too short! Try again.")
            continue
    except ValueError:
        print("⚠️ Please enter a valid number.")
        continue

    pwd = generate_password(length)
    print(f"🔑 Your new password: {pwd}")

    again = input("\nDo you want to generate another password? (yes/no): ").lower()
    if again != 'yes':
        print("👋 Thank you for using Password Generator!")
        break