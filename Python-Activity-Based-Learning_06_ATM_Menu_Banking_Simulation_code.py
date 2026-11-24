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
