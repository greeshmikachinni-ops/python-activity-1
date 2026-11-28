# Case Study 5: Password Policy Validation Engine

def validate_password(pwd):
    errors = []
    special_chars = "!@#$%^&*()-_=+"
    prohibited = ["password", "admin", "1234", "qwerty"]

    if len(pwd) < 8:
        errors.append("Minimum length of 8 characters not met.")
    if " " in pwd:
        errors.append("Password must not contain spaces.")

    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    for ch in pwd:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_digit = True
        elif ch in special_chars:
            has_special = True

    if not has_upper:
        errors.append("Missing at least one uppercase letter (A-Z).")
    if not has_lower:
        errors.append("Missing at least one lowercase letter (a-z).")
    if not has_digit:
        errors.append("Missing at least one numeric digit (0-9).")
    if not has_special:
        errors.append("Missing at least one special character (!@#$%^&*).")

    # Check for 3 consecutive identical characters
    for i in range(len(pwd) - 2):
        if pwd[i] == pwd[i + 1] == pwd[i + 2]:
            errors.append(f"Contains 3 consecutive identical characters ('{pwd[i]*3}').")
            break

    # Check prohibited substrings
    lower_pwd = pwd.lower()
    for word in prohibited:
        if word in lower_pwd:
            errors.append(f"Contains prohibited substring ('{word}').")

    return errors


test_passwords = ["pass123", "Admin@1234", "Gooood@99", "V@lidP9x!"]

for p in test_passwords:
    failures = validate_password(p)
    print(f"Testing Password: '{p}'")
    if not failures:
        print(" -> RESULT: VALID\n")
    else:
        print(" -> RESULT: INVALID")
        for reason in failures:
            print(f"    * {reason}")
        print()
