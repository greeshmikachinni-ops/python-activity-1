# Case Study 53: Food Waste Monitoring System

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
prepared_meals = [400, 420, 380, 450, 500, 300, 280]
served_meals = [375, 360, 355, 390, 470, 250, 265]
MAX_WASTE_PCT = 10.0

total_prepared = 0
total_leftovers = 0
flagged_days = []

print("--- Daily Canteen Food Waste Report ---")
for i in range(len(days)):
    prep = prepared_meals[i]
    serv = served_meals[i]
    leftovers = prep - serv
    wastage_pct = (leftovers / prep) * 100

    total_prepared += prep
    total_leftovers += leftovers

    status = "EXCEEDED" if wastage_pct > MAX_WASTE_PCT else "OK"
    if status == "EXCEEDED":
        flagged_days.append((days[i], wastage_pct))

    print(f"{days[i]:<10} | Prep: {prep:<3} | Served: {serv:<3} | Leftover: {leftovers:<3} | Waste: {wastage_pct:5.2f}% [{status}]")

overall_waste_pct = (total_leftovers / total_prepared) * 100
print("\n--- Weekly Summary ---")
print(f"Total Meals Prepared : {total_prepared}")
print(f"Total Leftovers      : {total_leftovers}")
print(f"Overall Wastage Rate : {overall_waste_pct:.2f}%")
print(f"Days Exceeding {MAX_WASTE_PCT}% : {[d for d, _ in flagged_days]}")
