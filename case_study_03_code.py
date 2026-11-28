# Case Study 3: ATM Transaction Sequence Simulation

balance = 15000
MAX_WITHDRAWAL = 10000
MIN_BALANCE = 1000

transactions = [
    ("D", 5000),
    ("W", 12000),
    ("W", 450),
    ("W", 4000),
    ("W", 15500),
    ("D", -200),
    ("X", 1000),
    ("W", 3000)
]

valid_txns = 0
rejected_txns = 0
total_deposited = 0
total_withdrawn = 0

print(f"Initial Balance: ₹{balance}\n" + "-" * 55)

for idx, (t_type, amount) in enumerate(transactions, start=1):
    if t_type == "D":
        if amount > 0:
            balance += amount
            total_deposited += amount
            valid_txns += 1
            print(f"Txn {idx}: DEPOSIT  ₹{amount:<6} -> SUCCESS | Balance: ₹{balance}")
        else:
            rejected_txns += 1
            print(f"Txn {idx}: DEPOSIT  ₹{amount:<6} -> REJECTED (Invalid amount)")

    elif t_type == "W":
        if amount <= 0:
            rejected_txns += 1
            print(f"Txn {idx}: WITHDRAW ₹{amount:<6} -> REJECTED (Invalid amount)")
        elif amount % 100 != 0:
            rejected_txns += 1
            print(f"Txn {idx}: WITHDRAW ₹{amount:<6} -> REJECTED (Must be multiple of ₹100)")
        elif amount > MAX_WITHDRAWAL:
            rejected_txns += 1
            print(f"Txn {idx}: WITHDRAW ₹{amount:<6} -> REJECTED (Exceeds ₹{MAX_WITHDRAWAL} limit)")
        elif balance - amount < MIN_BALANCE:
            rejected_txns += 1
            print(f"Txn {idx}: WITHDRAW ₹{amount:<6} -> REJECTED (Minimum balance ₹{MIN_BALANCE} required)")
        else:
            balance -= amount
            total_withdrawn += amount
            valid_txns += 1
            print(f"Txn {idx}: WITHDRAW ₹{amount:<6} -> SUCCESS | Balance: ₹{balance}")
    else:
        rejected_txns += 1
        print(f"Txn {idx}: UNKNOWN  '{t_type}'     -> REJECTED (Invalid transaction type)")

print("-" * 55)
print("TRANSACTION SUMMARY:")
print(f"Total Processed : {len(transactions)}")
print(f"Valid Txns      : {valid_txns}")
print(f"Rejected Txns   : {rejected_txns}")
print(f"Total Deposited : ₹{total_deposited}")
print(f"Total Withdrawn : ₹{total_withdrawn}")
print(f"Final Balance   : ₹{balance}")
