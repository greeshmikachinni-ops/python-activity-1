# Case Study 10: Multi-Product Price Fluctuation Analysis

## 1. Problem Statement
Process historical product prices stored in lists, calculate percentage changes, identify maximum fluctuations, and flag products exceeding a supplied threshold.

## 2. Objectives
- Analyze multi-period price histories across multiple products using nested lists.
- Calculate period-over-period percentage price changes and overall net price drift.
- Identify the single largest price jump/drop and flag volatile products exceeding a threshold.

## 3. Assumptions
- Each product has 4 sequential monthly price observations.
- A single-period price change with an absolute magnitude > 15.0% flags the product as volatile.

## 4. Algorithm
1. Start the program.
2. Define `products` list and 2D list `price_history`.
3. Set volatility threshold `THRESHOLD = 15.0`.
4. For each product, iterate through its price list from index 1 to end.
5. Compute `pct_change = ((curr - prev) / prev) * 100`.
6. Track the maximum absolute percentage fluctuation across all products.
7. If `abs(pct_change) > THRESHOLD`, flag the product as volatile.
8. Display period changes, overall change, maximum fluctuation, and flagged products.
9. Stop the program.

## 5. Flowchart
```
[Start]
   |
   v
[Read Products & Historical Price Lists]
   |
   v
[Loop Each Product]
   |
   v
[Loop Consecutive Price Pairs: Compute % Change]
   |
   +--> [Track Global Max Absolute % Fluctuation]
   |
   +--> [|Pct Change| > 15%?] --Yes--> [Flag Product as Volatile]
   |
   v
[Display Period Changes, Max Fluctuation & Volatile Products]
   |
   v
[End]
```

## 6. Pseudocode
```
BEGIN
    SET products = ["Olive Oil", "Coffee Beans", "Almonds"]
    SET prices = [[500, 520, 610, 590], [300, 310, 315, 325], [800, 650, 670, 700]]
    SET max_fluct = 0, max_prod = ""

    FOR i FROM 0 TO LENGTH(products) - 1 DO
        volatile = FALSE
        FOR j FROM 1 TO LENGTH(prices[i]) - 1 DO
            pct = ((prices[i][j] - prices[i][j-1]) / prices[i][j-1]) * 100
            IF ABS(pct) > max_fluct THEN
                max_fluct = ABS(pct)
                max_prod = products[i]
            ENDIF
            IF ABS(pct) > 15.0 THEN
                volatile = TRUE
            ENDIF
        ENDFOR
        PRINT products[i], volatile
    ENDFOR
    PRINT max_prod, max_fluct
END
```

## 7. Python Source Code
Refer to [`code.py`](./code.py) in this directory.

```python
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
```

## 8. Test Cases
| Test Case | Product | Price Series | Period Changes | Max Abs Change | Volatile (>15%)? |
| :--- | :--- | :--- | :--- | :--- | :--- |
| TC1 | Olive Oil | `[500, 520, 610, 590]` | +4.0%, +17.31%, -3.28% | 17.31% | Yes |
| TC2 | Coffee Beans | `[300, 310, 315, 325]` | +3.33%, +1.61%, +3.17% | 3.33% | No |
| TC3 | Almonds | `[800, 650, 670, 700]` | -18.75%, +3.08%, +4.48% | 18.75% (Global Max) | Yes |

## 9. Output Screenshots
*(Run `python code.py` in your terminal and attach the screenshot here before final GitHub submission.)*

## 10. Conclusion
The price fluctuation analyzer tracks multi-product market volatility over time, isolating sharp price shocks and aiding procurement and pricing decisions.
