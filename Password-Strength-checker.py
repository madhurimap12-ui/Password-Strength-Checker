import re

def check_password_strength(password):
    strength = 0
    criteria = []

    # Length
    if len(password) >= 8:
        strength += 1
        criteria.append("✔ Length OK")
    else:
        criteria.append("✘ Too short")

    # Uppercase
    if re.search(r"[A-Z]", password):
        strength += 1
        criteria.append("✔ Has uppercase")
    else:
        criteria.append("✘ No uppercase")

    # Lowercase
    if re.search(r"[a-z]", password):
        strength += 1
        criteria.append("✔ Has lowercase")
    else:
        criteria.append("✘ No lowercase")

    # Numbers
    if re.search(r"[0-9]", password):
        strength += 1
        criteria.append("✔ Has number")
    else:
        criteria.append("✘ No number")

    # Special characters
    if re.search(r"[@$!%*?&]", password):
        strength += 1
        criteria.append("✔ Has special char")
    else:
        criteria.append("✘ No special char")

    # Final rating
    if strength <= 2:
        rating = "Weak"
    elif strength == 3 or strength == 4:
        rating = "Medium"
    else:
        rating = "Strong"

    return rating, criteria

# Main program
pwd = input("Enter a password: ")
rating, details = check_password_strength(pwd)
print("Password Strength:", rating)
print("\n".join(details))
