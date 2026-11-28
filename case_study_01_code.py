# Case Study 1: Progressive Electricity Billing

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
