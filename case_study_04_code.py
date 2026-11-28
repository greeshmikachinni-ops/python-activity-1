# Case Study 4: Multi-Product Shopping Budget Constraint

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
