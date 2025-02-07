import secrets
import string

def generate_password(length, use_uppercase, use_lowercase, use_digits, use_symbols):
    """
    Generate a secure password based on user preferences.

    Parameters:
    - length (int): Length of the desired password.
    - use_uppercase (bool): Whether to include uppercase letters.
    - use_lowercase (bool): Whether to include lowercase letters.
    - use_digits (bool): Whether to include digits.
    - use_symbols (bool): Whether to include symbols.

    Returns:
    - str: Generated password.
    """
    # Create a pool of characters based on user preferences
    character_pool = ''
    if use_uppercase:
        character_pool += string.ascii_uppercase
    if use_lowercase:
        character_pool += string.ascii_lowercase
    if use_digits:
        character_pool += string.digits
    if use_symbols:
        character_pool += string.punctuation

    # Ensure the character pool is not empty
    if not character_pool:
        raise ValueError("At least one character type must be selected.")

    # Generate the password
    password = ''.join(secrets.choice(character_pool) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")

    # Get password length from user
    while True:
        try:
            length = int(input("Enter the desired password length: "))
            if length <= 0:
                print("Please enter a positive integer.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Get character type preferences from user
    use_uppercase = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
    use_lowercase = input("Include lowercase letters? (y/n): ").strip().lower() == 'y'
    use_digits = input("Include digits? (y/n): ").strip().lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").strip().lower() == 'y'

    try:
        # Generate and display the password
        password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_symbols)
        print(f"Generated password: {password}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
