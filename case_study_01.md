# Case Study 1: Progressive Electricity Billing

## 1. Problem Statement
Calculate household bills using multiple consumption slabs, fixed charges, surcharges, and rebates, then compare bills across several months and identify unusual increases.

## 2. Objectives
- Implement multi-tier slab-based electricity tariff calculations.
- Incorporate fixed charges, surcharges, and rebates based on consumption levels.
- Compare monthly billing amounts to detect and flag unusual spikes in electricity usage.

## 3. Assumptions
- Slab 1 (0-100 units): ₹1.50/unit
- Slab 2 (101-300 units): ₹2.50/unit
- Slab 3 (>300 units): ₹4.00/unit
- Fixed charge is ₹50 per month.
- A 5% rebate is applied if consumption is under 100 units; a 10% surcharge applies if consumption exceeds 400 units.
- An increase of more than 30% compared to the previous month is flagged as unusual.

## 4. Algorithm
1. Start the program.
2. Input or define the list of monthly unit consumptions.
3. For each month's units, calculate base energy charges using progressive slabs.
4. Apply rebate if units <= 100, or surcharge if units > 400.
5. Add the fixed monthly charge to compute the final bill.
6. Store all monthly bills in a list.
7. Iterate through the bills list from the second month onwards and compute percentage change from the previous month.
8. Flag any month where the increase exceeds 30%.
9. Display all monthly bills and unusual spike alerts.
10. Stop the program.

## 5. Flowchart
```
[Start]
   |
   v
[Read Monthly Units List]
   |
   v
[Loop through each month's units]
   |---> [Units <= 100?] --Yes--> [Base = Units * 1.50; Apply 5% Rebate]
   |          |No
   |          v
   |     [Units <= 300?] --Yes--> [Base = 150 + (Units - 100) * 2.50]
   |          |No
   |          v
   |     [Base = 150 + 500 + (Units - 300) * 4.00]
   |          |
   |          v
   |     [Units > 400?] --Yes--> [Add 10% Surcharge]
   |
   v
[Add Fixed Charge (₹50) -> Store in Bills List]
   |
   v
[Compare consecutive bills for >30% increase]
   |
   v
[Print Bills & Alerts]
   |
   v
[End]
```

## 6. Pseudocode
```
BEGIN
    SET monthly_units = [95, 180, 210, 420, 440, 290]
    SET bills = []
    FOR EACH units IN monthly_units DO
        IF units <= 100 THEN
            base = units * 1.50
            rebate = base * 0.05
            surcharge = 0
        ELSE IF units <= 300 THEN
            base = (100 * 1.50) + ((units - 100) * 2.50)
            rebate = 0
            surcharge = 0
        ELSE
            base = (100 * 1.50) + (200 * 2.50) + ((units - 300) * 4.00)
            rebate = 0
            IF units > 400 THEN
                surcharge = base * 0.10
            ELSE
                surcharge = 0
            ENDIF
        ENDIF
        total_bill = base - rebate + surcharge + 50
        APPEND total_bill TO bills
    ENDFOR

    FOR i FROM 1 TO LENGTH(bills) - 1 DO
        pct_increase = ((bills[i] - bills[i-1]) / bills[i-1]) * 100
        IF pct_increase > 30 THEN
            PRINT "Unusual increase in Month", i + 1
        ENDIF
    ENDFOR
END
```

## 7. Python Source Code
Refer to [`code.py`](./code.py) in this directory.

```python
# Case Study 2: Progressive Electricity Billing

def calculate_monthly_bill(units):
    fixed_charge = 50.0
    rebate = 0.0
    surcharge = 0.0

    if units <= 100:
        base_charge = units * 1.50
        rebate = base_charge * 0.05
    elif units <= 300:
        base_charge = (100 * 1.50) + ((units - 100) * 2.50)
    else:
        base_charge = (100 * 1.50) + (200 * 2.50) + ((units - 300) * 4.00)
        if units > 400:
            surcharge = base_charge * 0.10

    total_bill = base_charge - rebate + surcharge + fixed_charge
    return round(total_bill, 2)


# Sample 6-month household consumption data (in kWh/units)
months = ["January", "February", "March", "April", "May", "June"]
monthly_units = [95, 180, 210, 420, 440, 290]
monthly_bills = []

print("--- Monthly Electricity Billing Summary ---")
for i in range(len(months)):
    bill = calculate_monthly_bill(monthly_units[i])
    monthly_bills.append(bill)
    print(f"{months[i]:<10} | Units: {monthly_units[i]:<4} | Bill: ₹{bill:.2f}")

print("\n--- Unusual Increase Detection (>30% MoM) ---")
for i in range(1, len(monthly_bills)):
    prev_bill = monthly_bills[i - 1]
    curr_bill = monthly_bills[i]
    pct_increase = ((curr_bill - prev_bill) / prev_bill) * 100
    if pct_increase > 30.0:
        print(f"ALERT: {months[i]} bill (₹{curr_bill:.2f}) increased by {pct_increase:.2f}% compared to {months[i-1]} (₹{prev_bill:.2f}).")
```

## 8. Test Cases
| Test Case | Input Units | Expected Base + Adj | Fixed Charge | Final Bill | Alert Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| TC1 (Rebate) | 95 | ₹142.50 - ₹7.12 = ₹135.38 | ₹50.00 | ₹185.38 | Baseline Month 1 |
| TC2 (Slab 2) | 180 | ₹350.00 | ₹50.00 | ₹400.00 | +115.77% (Unusual Spike) |
| TC3 (Surcharge) | 420 | ₹1130.00 + ₹113.00 = ₹1243.00 | ₹50.00 | ₹1293.00 | +172.21% (Unusual Spike) |

## 9. Output Screenshots
*(Run `python code.py` in your terminal and attach the screenshot here before final GitHub submission.)*

## 10. Conclusion
The progressive electricity billing system accurately evaluates tiered energy consumption, applies conditional rebates and surcharges, and proactively detects anomalous month-over-month billing spikes using fundamental Python loops and conditionals.
