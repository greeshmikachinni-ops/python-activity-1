# Case Study 6: ATM Menu-Driven Banking Simulation

## 1. Problem Statement
Implement repeated menu operations for deposits, withdrawals, balance inquiries, and transaction summaries, with validation and specified account limits.

## 2. Objectives
- Build an interactive, loop-driven menu system supporting multiple banking operations.
- Enforce daily withdrawal limits and positive deposit validations.
- Maintain a session transaction log using lists and display a complete summary upon exit.

## 3. Assumptions
- Starting balance is ₹10,000; daily cumulative withdrawal limit is ₹15,000.
- Menu options: 1 = Deposit, 2 = Withdraw, 3 = Balance Inquiry, 4 = Mini Statement, 5 = Exit.
- For automated testing/reproducibility, a predefined sequence of user inputs can also be simulated cleanly.

## 4. Algorithm
1. Start the program.
2. Initialize balance = 10000, daily_withdrawn = 0, daily_limit = 15000, and history = [].
3. Enter a `while True` loop displaying the ATM menu.
4. Read user choice.
5. If choice == 1: read deposit amount, validate > 0, update balance, append to history.
6. If choice == 2: read withdrawal amount, validate > 0, <= balance, and (daily_withdrawn + amount) <= daily_limit; update balance and daily_withdrawn, append to history.
7. If choice == 3: print current balance.
8. If choice == 4: print all entries in history.
9. If choice == 5: print exit summary and break loop.
10. Stop the program.

## 5. Flowchart
```
[Start]
   |
   v
[Init Balance = 10000, Daily Limit = 15000, History = []]
   |
   v
[Display Menu: 1.Deposit 2.Withdraw 3.Balance 4.Statement 5.Exit] <---+
   |                                                                  |
   +--> [Choice 1] --> [Validate & Add Deposit] ----------------------+
   +--> [Choice 2] --> [Validate Balance & Daily Limit, Deduct] ------+
   +--> [Choice 3] --> [Display Current Balance] ---------------------+
   +--> [Choice 4] --> [Print Transaction History] -------------------+
   +--> [Choice 5] --> [Print Goodbye & Exit Loop]
                            |
                            v
                          [End]
```

## 6. Pseudocode
```
BEGIN
    SET balance = 10000, daily_withdrawn = 0, daily_limit = 15000
    SET history = []
    WHILE TRUE DO
        DISPLAY menu
        READ choice
        IF choice == 1 THEN
            READ amt
            IF amt > 0 THEN
                balance = balance + amt
                APPEND "Deposited " + amt TO history
            ENDIF
        ELSE IF choice == 2 THEN
            READ amt
            IF amt > 0 AND amt <= balance AND (daily_withdrawn + amt) <= daily_limit THEN
                balance = balance - amt
                daily_withdrawn = daily_withdrawn + amt
                APPEND "Withdrew " + amt TO history
            ENDIF
        ELSE IF choice == 3 THEN
            PRINT balance
        ELSE IF choice == 4 THEN
            PRINT history
        ELSE IF choice == 5 THEN
            BREAK
        ENDIF
    ENDWHILE
END
```

## 7. Python Source Code
Refer to [`code.py`](./code.py) in this directory.

```python
# Case Study 38: ATM Menu-Driven Banking Simulation

balance = 10000.0
daily_limit = 15000.0
daily_withdrawn = 0.0
history = []

# Simulated user inputs for non-blocking execution; replace with input() for interactive mode
simulated_inputs = [
    ("3", None),
    ("1", 5000.0),
    ("2", 12000.0),
    ("2", 4000.0),
    ("4", None),
    ("5", None)
]

step = 0
while step < len(simulated_inputs):
    print("\n--- ATM BANKING MENU ---")
    print("1. Deposit  2. Withdraw  3. Balance Inquiry  4. Mini Statement  5. Exit")
    choice, amt = simulated_inputs[step]
    step += 1
    print(f"Selected Option: {choice}")

    if choice == "1":
        if amt is not None and amt > 0:
            balance += amt
            history.append(f"Deposited: ₹{amt:.2f}")
            print(f"Success: ₹{amt:.2f} deposited.")
        else:
            print("Error: Deposit amount must be positive.")

    elif choice == "2":
        if amt is None or amt <= 0:
            print("Error: Invalid withdrawal amount.")
        elif amt > balance:
            print("Error: Insufficient account balance.")
        elif daily_withdrawn + amt > daily_limit:
            print(f"Error: Exceeds daily withdrawal limit of ₹{daily_limit:.2f}.")
        else:
            balance -= amt
            daily_withdrawn += amt
            history.append(f"Withdrew : ₹{amt:.2f}")
            print(f"Success: ₹{amt:.2f} withdrawn.")

    elif choice == "3":
        print(f"Current Available Balance: ₹{balance:.2f}")

    elif choice == "4":
        print("--- Session Mini Statement ---")
        if not history:
            print("No transactions recorded in this session.")
        else:
            for entry in history:
                print(" *", entry)

    elif choice == "5":
        print(f"Thank you for banking with us! Final Balance: ₹{balance:.2f}")
        break
    else:
        print("Invalid menu choice. Please try again.")
```

## 8. Test Cases
| Test Case | Menu Choice | Input Amount | Expected Outcome | Balance After |
| :--- | :--- | :--- | :--- | :--- |
| TC1 | 3 (Balance) | N/A | Displays ₹10,000 | ₹10,000 |
| TC2 | 1 (Deposit) | ₹5,000 | Deposit accepted, logged | ₹15,000 |
| TC3 | 2 (Withdraw) | ₹12,000 | Withdrawal accepted (within ₹15k daily limit) | ₹3,000 |
| TC4 | 2 (Withdraw) | ₹4,000 | Rejected (exceeds daily limit & balance) | ₹3,000 |
| TC5 | 4 (Statement) | N/A | Displays Deposit ₹5,000 and Withdraw ₹12,000 | ₹3,000 |

## 9. Output Screenshots
*(Run `python code.py` in your terminal and attach the screenshot here before final GitHub submission.)*

## 10. Conclusion
The menu-driven ATM simulation illustrates state persistence across loop iterations, input validation, and session logging using standard control structures.
