import random

LETTERS = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
NUMBERS = list("0123456789")
SYMBOLS = list("!@#$%^&*")
COMBINED = LETTERS + NUMBERS + SYMBOLS


def get_user_length():
    print("===== Password Generator =====\n")

    while True:
        try:
            user_length = int(input("Enter password length: "))

            if user_length < 3:
                print("Password length must be at least 3.\n")
                continue

            return user_length

        except ValueError:
            print("Please enter a valid number.\n")


def generate_password(length, combined, letters, numbers, symbols):
    password = []

    # Ensure at least one character from each category
    password.append(random.choice(letters))
    password.append(random.choice(numbers))
    password.append(random.choice(symbols))

    # Fill the remaining characters
    for _ in range(length - 3):
        password.append(random.choice(combined))

    random.shuffle(password)

    return "".join(password)


def print_password(password):
    print("\nGenerated Password:")
    print(password)


def count_characters(password, characters):
    count = 0

    for char in password:
        if char in characters:
            count += 1

    return count


def main():
    password_length = get_user_length()

    password = generate_password(
        password_length,
        COMBINED,
        LETTERS,
        NUMBERS,
        SYMBOLS,
    )

    print_password(password)

    print("\nPassword Statistics")
    print("-------------------")
    print(f"Letters: {count_characters(password, LETTERS)}")
    print(f"Numbers: {count_characters(password, NUMBERS)}")
    print(f"Symbols: {count_characters(password, SYMBOLS)}")


if __name__ == "__main__":
    main()