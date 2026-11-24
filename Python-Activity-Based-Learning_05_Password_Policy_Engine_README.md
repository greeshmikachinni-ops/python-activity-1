# Case Study 29: Password Policy Validation Engine

## 1. Problem Statement
Evaluate sample password strings against minimum length, character-category, repetition, and prohibited-substring rules; explain each failed condition.

## 2. Objectives
- Validate password strength using string traversal and character classification methods.
- Detect consecutive repeated characters and disallowed dictionary substrings.
- Provide detailed, human-readable diagnostic feedback for every failed rule.

## 3. Assumptions
- Minimum length is 8 characters; no spaces allowed.
- Must contain at least 1 uppercase letter, 1 lowercase letter, 1 digit, and 1 special character (!@#$%^&*).
- No character may repeat 3 or more times consecutively (e.g., 'aaa').
- Must not contain prohibited substrings: 'password', 'admin', '1234', 'qwerty' (case-insensitive).

## 4. Algorithm
1. Start the program.
2. Define prohibited substrings list and special characters string.
3. For each test password, initialize an empty list `reasons`.
4. Check length >= 8 and absence of spaces.
5. Iterate through characters to verify presence of uppercase, lowercase, digit, and special character.
6. Check adjacent characters `pwd[i] == pwd[i+1] == pwd[i+2]` for triple repetition.
7. Convert password to lowercase and check if any prohibited substring is present using `in`.
8. If `reasons` is empty, mark password as VALID; otherwise, mark INVALID and print all reasons.
9. Stop the program.

## 5. Flowchart
```
[Start]
   |
   v
[Read Password String]
   |
   v
[Check Length >= 8 & No Spaces] ---> [Append Failure if False]
   |
   v
[Check Upper, Lower, Digit, Special Char] ---> [Append Failure if Missing]
   |
   v
[Check Consecutive Triplets (aaa)] ---> [Append Failure if Found]
   |
   v
[Check Prohibited Substrings] ---> [Append Failure if Found]
   |
   v
[Failure List Empty?] --Yes--> [Print VALID]
   |No
   v
[Print INVALID & List All Failed Rules]
   |
   v
[End]
```

## 6. Pseudocode
```
BEGIN
    SET prohibited = ["password", "admin", "1234", "qwerty"]
    FOR EACH pwd IN sample_passwords DO
        SET errors = []
        IF LENGTH(pwd) < 8 THEN APPEND "Too short" TO errors
        IF " " IN pwd THEN APPEND "Contains spaces" TO errors
        CHECK has_upper, has_lower, has_digit, has_special
        IF NOT all four THEN APPEND missing category errors
        FOR i FROM 0 TO LENGTH(pwd) - 3 DO
            IF pwd[i] == pwd[i+1] AND pwd[i+1] == pwd[i+2] THEN
                APPEND "Consecutive repeated characters" TO errors
            ENDIF
        ENDFOR
        FOR EACH word IN prohibited DO
            IF word IN LOWER(pwd) THEN
                APPEND "Contains prohibited substring" TO errors
            ENDIF
        ENDFOR
        PRINT validation result and errors
    ENDFOR
END
```

## 7. Python Source Code
Refer to [`code.py`](./code.py) in this directory.

```python
# Case Study 29: Password Policy Validation Engine

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
```

## 8. Test Cases
| Test Case | Input Password | Expected Result | Failed Rules Reported |
| :--- | :--- | :--- | :--- |
| TC1 | `pass123` | INVALID | Length < 8, no uppercase, no special char, contains 'pass'/'123' |
| TC2 | `Admin@1234` | INVALID | Contains prohibited substrings 'admin' and '1234' |
| TC3 | `Gooood@99` | INVALID | Consecutive character repetition ('ooo') |
| TC4 | `V@lidP9x!` | VALID | None |

## 9. Output Screenshots
*(Run `python code.py` in your terminal and attach the screenshot here before final GitHub submission.)*

## 10. Conclusion
The password policy engine demonstrates how string indexing, membership testing, and boolean flags combine to enforce strict security compliance with actionable user feedback.
