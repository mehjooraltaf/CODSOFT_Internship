import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")

    while True:
        try:
            length = int(input("\nEnter the desired password length: "))
            if length < 4:
                print("Please choose a length of at least 4 for a secure password.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        password = generate_password(length)
        print(f"Generated Password: {password}")

        again = input("\nGenerate another password? (yes/no): ")
        if again.lower() != "yes":
            print("Goodbye!")
            break

main()
