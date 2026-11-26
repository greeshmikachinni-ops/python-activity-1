# Case Study 13: ATM Transaction Sequence Simulation

## 1. Problem Statement
Process a sequence of deposits and withdrawals, maintain a simulated balance, enforce withdrawal limits, reject invalid transactions, and produce a transaction summary.

## 2. Objectives
- Simulate sequential banking operations using tuples and lists.
- Enforce per-transaction withdrawal caps, minimum balance requirements, and positive amount validation.
- Maintain accurate counts of successful and rejected operations for a final audit summary.

## 3. Assumptions
- Initial account balance is ₹15,000.
- Maximum single withdrawal limit is ₹10,000.
- Minimum balance of ₹1,000 must be maintained after any withdrawal.
- Withdrawal amounts must be multiples of ₹100; deposit amounts must be strictly positive.

## 4. Algorithm
1. Start the program.
2. Initialize balance = 15000, valid_count = 0, rejected_count = 0, total_deposited = 0, total_withdrawn = 0.
3. Define a list of transaction tuples (type, amount).
4. Iterate through each transaction in the list.
5. If type is 'D' (Deposit): verify amount > 0; if valid, add to balance and update counters, else reject.
6. If type is 'W' (Withdrawal): verify amount > 0, amount % 100 == 0, amount <= 10000, and (balance - amount) >= 1000; if all pass, deduct from balance, else reject with reason.
7. If type is unknown, mark as rejected.
8. Print final balance and transaction summary.
9. Stop the program.

## 5. Flowchart
╔════════════════════════════════════════════════════════╗
║                        [ START ]                       ║
╚═══════════════════════════╦════════════════════════════╝
                            ║
                            ▼
╔════════════════════════════════════════════════════════╗
║           [ Init Balance = 15000 & Counters ]          ║
╚═══════════════════════════╦════════════════════════════╝
                            ║
                            ▼
╔════════════════════════════════════════════════════════╗
║         [ Loop through Transactions (Type, Amount) ]   ║
╚═════════════╦═══════════════════════════╦══════════════╝
              │ Deposit ('D')             │ Withdrawal ('W')
              ▼                           ▼
╔══════════════════════════╗    ╔════════════════════════╗
║     [ Amount > 0? ]      ║    ║ [ Valid Multiple,      ║
╚═════════════╦════════════╝    ║   <=10k, Min Bal >=1k? ]║
              │ Yes             ╚════════════╦═══════════╝
              ▼                              │ Yes
╔══════════════════════════╗                 ▼
║  [ Balance += Amount ]   ║    ╔════════════════════════╗
╚═════════════╦════════════╝    ║  [ Balance -= Amount ] ║
              │ No              ╚════════════╦═══════════╝
              ▼                              │ No
╔══════════════════════════╗                 ▼
║  [ Reject Transaction ]  ║    ╔════════════════════════╗
╚══════════════════════════╝    ║  [ Reject Transaction ]║
                                ╚════════════════════════╝
                            ║
                            ▼
╔════════════════════════════════════════════════════════╗
║             [ Print Final Balance & Summary ]          ║
╚═══════════════════════════╦════════════════════════════╝
                            ║
                            ▼
╔════════════════════════════════════════════════════════╗
║                         [ END ]                        ║
╚════════════════════════════════════════════════════════╝
## 6. Pseudocode
```
BEGIN
    SET balance = 15000
    SET transactions = [("D", 5000), ("W", 12000), ("W", 450), ("W", 4000), ("W", 16000), ("D", -200)]
    SET valid = 0, rejected = 0

    FOR EACH (t_type, amt) IN transactions DO
        IF t_type == "D" THEN
            IF amt > 0 THEN
                balance = balance + amt
                valid = valid + 1
            ELSE
                rejected = rejected + 1
            ENDIF
        ELSE IF t_type == "W" THEN
            IF amt > 0 AND amt MOD 100 == 0 AND amt <= 10000 AND (balance - amt) >= 1000 THEN
                balance = balance - amt
                valid = valid + 1
            ELSE
                rejected = rejected + 1
            ENDIF
        ELSE
            rejected = rejected + 1
        ENDIF
    ENDFOR
    PRINT balance, valid, rejected
END
```

## 7. Python Source Code
Refer to [`code.py`](./code.py) in this directory.

```python
# Case Study 13: ATM Transaction Sequence Simulation

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
```

## 8. Test Cases
| Test Case | Operation | Amount | Rule Checked | Outcome | Resulting Balance |
| :--- | :--- | :--- | :--- | :--- | :--- |
| TC1 | Deposit ('D') | ₹5,000 | Positive amount | Accepted | ₹20,000 |
| TC2 | Withdraw ('W') | ₹12,000 | Exceeds ₹10,000 limit | Rejected | ₹20,000 |
| TC3 | Withdraw ('W') | ₹450 | Not a multiple of ₹100 | Rejected | ₹20,000 |
| TC4 | Withdraw ('W') | ₹4,000 | All constraints satisfied | Accepted | ₹16,000 |
| TC5 | Withdraw ('W') | ₹15,500 | Violates ₹1,000 min balance | Rejected | ₹16,000 |

## 9. Output Screenshots
*(Run `python code.py` in your terminal and attach the screenshot here before final GitHub submission.)*

## 10. Conclusion
The ATM transaction simulator reliably enforces multi-condition banking rules on sequential transactions, safeguarding account constraints and generating an auditable summary.
