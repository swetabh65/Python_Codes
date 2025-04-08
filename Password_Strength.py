import re

def check_password_strength(password: str) -> bool:
    """
    Check if the password meets the following strength criteria:
    - At least password length should be 8 characters long
    - Must contains both uppercase and lowercase letters
    - Should contains at least one digit
    - Should contains at least one special character (!@#$%^&*()-_+= etc.)
    """
    if len(password) < 8:
        print("Make sure that the password must be of at least 8 characters long.")
        return False

    if not re.search(r'[A-Z]', password):
        print("Password must contain at least one uppercase letter.")
        return False

    if not re.search(r'[a-z]', password):
        print("Password must contain at least one lowercase letter.")
        return False

    if not re.search(r'\d', password):
        print("Password must contain at least one digit.")
        return False

    if not re.search(r'[!@#$%^&*()_\-+=<>?/\\|{}\[\]~`]', password):
        print("Password must contain at least one special character (e.g., !, @, #, ^).")
        return False

    return True

if __name__ == "__main__":
    user_password = input("Enter a password to validate its strength: ")
    if check_password_strength(user_password):
        print("The entered password is strong.")
    else:
        print("Kindly try again with a stronger password.")
