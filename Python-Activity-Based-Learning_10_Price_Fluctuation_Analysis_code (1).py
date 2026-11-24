# Case Study 63: Multi-Product Price Fluctuation Analysis

products = ["Olive Oil (1L)", "Coffee Beans (500g)", "Almonds (1kg)"]
price_history = [
    [500.0, 520.0, 610.0, 590.0],
    [300.0, 310.0, 315.0, 325.0],
    [800.0, 650.0, 670.0, 700.0]
]
VOLATILITY_THRESHOLD = 15.0

max_abs_fluctuation = 0.0
max_fluct_product = ""
volatile_products = []

print("--- Product Price Fluctuation Report ---")
for i in range(len(products)):
    name = products[i]
    prices = price_history[i]
    changes = []
    is_volatile = False

    for j in range(1, len(prices)):
        prev_p = prices[j - 1]
        curr_p = prices[j]
        pct_change = ((curr_p - prev_p) / prev_p) * 100
        changes.append(round(pct_change, 2))

        if abs(pct_change) > max_abs_fluctuation:
            max_abs_fluctuation = abs(pct_change)
            max_fluct_product = f"{name} (Period {j} -> {j+1}: {pct_change:+.2f}%)"

        if abs(pct_change) > VOLATILITY_THRESHOLD:
            is_volatile = True

    net_change = ((prices[-1] - prices[0]) / prices[0]) * 100
    if is_volatile:
        volatile_products.append(name)

    print(f"Product: {name}")
    print(f"  Prices        : {prices}")
    print(f"  Period % Chg  : {changes}")
    print(f"  Net % Change  : {net_change:+.2f}% | Volatile Flag: {is_volatile}\n")

print("--- Summary ---")
print(f"Maximum Single-Period Fluctuation : {max_fluct_product}")
print(f"Flagged Volatile Products (>15%)  : {volatile_products}")
