# Case Study 4: Multi-Product Shopping Budget Constraint

## 1. Problem Statement
Evaluate a shopping basket containing multiple products and quantities, apply discount conditions, and determine which purchases must be reduced to remain within a fixed budget.

## 2. Objectives
- Calculate item-wise and overall cart totals from structured product lists.
- Apply tiered cart discount rules when total spend crosses a threshold.
- Identify high-cost items and iteratively reduce quantities until the basket fits within the fixed budget.

## 3. Assumptions
- Fixed shopping budget is ₹3,000.
- A 10% discount is applied if the raw subtotal exceeds ₹2,500.
- If the discounted total still exceeds ₹3,000, items are sorted by unit price (highest first) and reduced one unit at a time until within budget.

## 4. Algorithm
1. Start the program.
2. Initialize budget = 3000 and basket list containing [product_name, unit_price, quantity].
3. Compute raw subtotal by summing (unit_price * quantity) for all items.
4. Apply 10% discount if subtotal > 2500.
5. Check if discounted total <= budget. If yes, print approval message.
6. If discounted total > budget, sort items by unit price in descending order.
7. Loop through sorted items and reduce quantity by 1 while quantity > 0 and total > budget, recalculating discounted total after each reduction.
8. Display adjusted basket and final payable amount.
9. Stop the program.

## 5. Flowchart
```
[Start]
   |
   v
[Read Budget (₹3000) & Basket Items]
   |
   v
[Calculate Subtotal & Apply 10% Discount if > ₹2500]
   |
   v
[Final Total <= Budget?] --Yes--> [Approve Basket & Print Summary]
   |No
   v
[Sort Items by Unit Price Descending]
   |
   v
[Reduce Quantity of Most Expensive Items Until Total <= Budget]
   |
   v
[Print Reduced Items & Final Basket]
   |
   v
[End]
```

## 6. Pseudocode
```
BEGIN
    SET budget = 3000
    SET basket = [["Headphones", 1500, 1], ["Shirt", 800, 2], ["Book", 400, 2]]
    COMPUTE total = discounted_sum(basket)

    IF total <= budget THEN
        PRINT "Within budget!"
    ELSE
        SORT basket BY unit_price DESCENDING
        FOR EACH item IN basket DO
            WHILE item.qty > 0 AND total > budget DO
                item.qty = item.qty - 1
                COMPUTE total = discounted_sum(basket)
                PRINT "Reduced", item.name
            ENDWHILE
        ENDFOR
    ENDIF
    PRINT final basket and total
END
```

## 7. Python Source Code
Refer to [`code.py`](./code.py) in this directory.

```python
# Case Study 19: Multi-Product Shopping Budget Constraint

def calculate_payable(cart):
    subtotal = sum(price * qty for _, price, qty in cart)
    discount = subtotal * 0.10 if subtotal > 2500 else 0.0
    return subtotal, discount, subtotal - discount


budget = 3000.0
# Format: [Product Name, Unit Price, Quantity]
basket = [
    ["Wireless Headphones", 1500.0, 1],
    ["Formal Shirt", 800.0, 2],
    ["Programming Book", 450.0, 2]
]

sub, disc, payable = calculate_payable(basket)
print(f"Budget: ₹{budget:.2f}")
print(f"Initial Subtotal: ₹{sub:.2f} | Discount: ₹{disc:.2f} | Payable: ₹{payable:.2f}\n")

if payable <= budget:
    print("Status: Basket is within budget! No reductions needed.")
else:
    print("Status: Budget exceeded! Reducing highest-priced items...")
    # Sort descending by unit price using simple bubble sort (syllabus compliant)
    n = len(basket)
    for i in range(n):
        for j in range(0, n - i - 1):
            if basket[j][1] < basket[j + 1][1]:
                basket[j], basket[j + 1] = basket[j + 1], basket[j]

    for item in basket:
        while item[2] > 0 and payable > budget:
            item[2] -= 1
            sub, disc, payable = calculate_payable(basket)
            print(f" -> Reduced 1 unit of '{item[0]}' (New Payable: ₹{payable:.2f})")

print("\n--- Final Adjusted Basket ---")
for name, price, qty in basket:
    print(f"{name:<22} | Price: ₹{price:<7.2f} | Final Qty: {qty}")
print(f"Final Payable Amount: ₹{payable:.2f} (Remaining Budget: ₹{budget - payable:.2f})")
```

## 8. Test Cases
| Test Case | Initial Basket | Raw Subtotal | Discounted Total | Action Required | Final Payable |
| :--- | :--- | :--- | :--- | :--- | :--- |
| TC1 (Over Budget) | Headphones(1500x1), Shirt(800x2), Book(400x2) | ₹3,900 | ₹3,510 | Reduce 1 Headphones (-₹1500) | ₹2,400 (No disc.) |
| TC2 (Within Budget) | Shirt(800x2), Book(400x2) | ₹2,400 | ₹2,400 | None | ₹2,400 |

## 9. Output Screenshots
*(Run `python code.py` in your terminal and attach the screenshot here before final GitHub submission.)*

## 10. Conclusion
The budget constraint evaluator automates discount computation and greedy quantity optimization, helping shoppers stay strictly within financial limits while maximizing retained items.
