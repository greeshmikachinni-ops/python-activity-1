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
