import random
import string

def generate_password(length=12):
    """Generate a secure random password with letters, digits, and symbols."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    try:
        length = int(input("Enter password length: "))
        
        if length < 6 or length > 50:
            print("Error: Password length should be between 6 and 50 characters.")
        else:
            print("Generated Password:", generate_password(length))
    
    except ValueError:
        print("Error: Please enter a valid number.")
