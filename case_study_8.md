# Case Study 49: Tuple-Based Product Catalogue Audit

## 1. Problem Statement
Store product identifiers, prices, and stock quantities in tuples; detect invalid records, calculate inventory values, and identify items requiring replenishment.

## 2. Objectives
- Store immutable product records as tuples inside a master catalogue list.
- Use tuple unpacking to inspect fields and detect malformed or negative entries.
- Compute total valid inventory valuation and flag low-stock products.

## 3. Assumptions
- Each tuple follows `(product_id, product_name, unit_price, stock_qty)`.
- A record is invalid if `product_id` is empty, `unit_price <= 0`, or `stock_qty < 0`.
- Valid products with `stock_qty < 10` require replenishment.

## 4. Algorithm
1. Start the program.
2. Define the list of product tuples.
3. Initialize `total_inventory_value = 0`, `invalid_records = []`, and `replenish_list = []`.
4. Iterate over the catalogue and unpack `(pid, name, price, qty)`.
5. Validate that `pid` is non-empty, `price > 0`, and `qty >= 0`.
6. If invalid, add record to `invalid_records` and continue to next item.
7. If valid, compute `item_value = price * qty` and add to `total_inventory_value`.
8. If `qty < 10`, add `(pid, name, qty)` to `replenish_list`.
9. Print valid inventory valuation, invalid records, and replenishment alerts.
10. Stop the program.

## 5. Flowchart
```
[Start]
   |
   v
[Read List of Product Tuples]
   |
   v
[Unpack (pid, name, price, qty)]
   |
   v
[Valid pid, price > 0, qty >= 0?] --No--> [Add to Invalid Records List]
   |Yes
   v
[Add (price * qty) to Total Inventory Value]
   |
   v
[qty < 10?] --Yes--> [Add to Replenishment List]
   |
   v
[Display Audit Summary, Invalid Records & Low Stock]
   |
   v
[End]
```

## 6. Pseudocode
```
BEGIN
    SET catalogue = [("P101", "Mouse", 500, 25), ("P102", "Keyboard", -1200, 10), ...]
    SET total_value = 0
    FOR EACH record IN catalogue DO
        UNPACK pid, name, price, qty FROM record
        IF pid == "" OR price <= 0 OR qty < 0 THEN
            PRINT "Invalid Record:", record
        ELSE
            total_value = total_value + (price * qty)
            IF qty < 10 THEN
                PRINT "Replenish Needed:", pid, name
            ENDIF
        ENDIF
    ENDFOR
    PRINT "Total Inventory Value:", total_value
END
```

## 7. Python Source Code
Refer to [`code.py`](./code.py) in this directory.

```python
# Case Study 49: Tuple-Based Product Catalogue Audit

catalogue = [
    ("P101", "Wireless Mouse", 500.0, 25),
    ("P102", "Mechanical Keyboard", 2500.0, 4),
    ("P103", "USB-C Cable", -150.0, 15),
    ("P104", "Webcam HD", 1800.0, 8),
    ("", "24-inch Monitor", 12000.0, 5),
    ("P106", "Laptop Stand", 900.0, -2)
]

total_inventory_value = 0.0
invalid_records = []
replenish_items = []

print("--- Valid Product Inventory ---")
for record in catalogue:
    pid, name, price, qty = record

    if not pid or price <= 0 or qty < 0:
        invalid_records.append(record)
        continue

    item_value = price * qty
    total_inventory_value += item_value
    print(f"{pid} | {name:<20} | Price: ₹{price:<8.2f} | Qty: {qty:<3} | Value: ₹{item_value:.2f}")

    if qty < 10:
        replenish_items.append((pid, name, qty))

print(f"\nTotal Valid Inventory Value: ₹{total_inventory_value:.2f}")

print("\n--- Invalid Records Detected ---")
for rec in invalid_records:
    print(f"Invalid Tuple: {rec}")

print("\n--- Replenishment Required (Stock < 10) ---")
for pid, name, qty in replenish_items:
    print(f"ALERT: {pid} ({name}) has only {qty} units left.")
```

## 8. Test Cases
| Test Case | Tuple Record | Validation Status | Inventory Value | Replenishment Flag |
| :--- | :--- | :--- | :--- | :--- |
| TC1 | `('P101', 'Wireless Mouse', 500.0, 25)` | Valid | ₹12,500.00 | No (Stock >= 10) |
| TC2 | `('P102', 'Mechanical Keyboard', 2500.0, 4)` | Valid | ₹10,000.00 | Yes (Stock < 10) |
| TC3 | `('P103', 'USB Cable', -150.0, 15)` | Invalid (Negative Price) | Excluded | N/A |
| TC4 | `('', 'Monitor', 12000.0, 5)` | Invalid (Missing ID) | Excluded | N/A |

## 9. Output Screenshots
*(Run `python code.py` in your terminal and attach the screenshot here before final GitHub submission.)*

## 10. Conclusion
Using tuples with structured unpacking ensures data integrity during inventory audits, cleanly isolating corrupted entries from financial valuation and stock replenishment workflows.
