# Case Study 9: Food Waste Monitoring System

## 1. Problem Statement
Compare prepared meals, meals served, and leftovers across several days; calculate wastage percentages and identify days exceeding acceptable limits.

## 2. Objectives
- Track daily canteen meal production, consumption, and leftover figures.
- Validate data consistency (`served + leftovers == prepared`) and calculate daily wastage percentages.
- Flag days exceeding acceptable food waste thresholds and compute overall weekly efficiency.

## 3. Assumptions
- Monitoring spans 7 days of a week.
- Acceptable daily food wastage limit is 10.0% of prepared meals.
- Leftovers are computed or verified against `prepared - served`.

## 4. Algorithm
1. Start the program.
2. Define lists for `days`, `prepared_meals`, and `served_meals`.
3. Initialize `total_prepared = 0` and `total_leftovers = 0`.
4. Loop over the 7 days; compute `leftovers = prepared - served`.
5. Calculate `wastage_pct = (leftovers / prepared) * 100`.
6. Accumulate `total_prepared` and `total_leftovers`.
7. If `wastage_pct > 10.0`, print an excess wastage alert for that day.
8. Compute and print overall weekly wastage percentage.
9. Stop the program.

## 5. Flowchart
```
[Start]
   |
   v
[Read Daily Prepared & Served Meals Lists]
   |
   v
[Loop Each Day: Leftovers = Prepared - Served]
   |
   v
[Compute Wastage % = (Leftovers / Prepared) * 100]
   |
   v
[Wastage % > 10%?] --Yes--> [Flag Day as Exceeding Acceptable Limit]
   |
   v
[Compute Overall Weekly Wastage %]
   |
   v
[Display Daily & Weekly Summary]
   |
   v
[End]
```

## 6. Pseudocode
```
BEGIN
    SET days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    SET prepared = [400, 420, 380, 450, 500, 300, 280]
    SET served = [375, 360, 355, 390, 470, 250, 265]
    SET total_prep = 0, total_waste = 0

    FOR i FROM 0 TO 6 DO
        leftovers = prepared[i] - served[i]
        waste_pct = (leftovers / prepared[i]) * 100
        total_prep = total_prep + prepared[i]
        total_waste = total_waste + leftovers
        PRINT days[i], leftovers, waste_pct
        IF waste_pct > 10.0 THEN
            PRINT "ALERT: High wastage on", days[i]
        ENDIF
    ENDFOR
    PRINT "Overall Wastage %:", (total_waste / total_prep) * 100
END
```

## 7. Python Source Code
Refer to [`code.py`](./code.py) in this directory.

```python
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
```

## 8. Test Cases
| Test Case | Day | Prepared | Served | Leftovers | Wastage % | Threshold Status (>10%) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| TC1 | Monday | 400 | 375 | 25 | 6.25% | Acceptable |
| TC2 | Tuesday | 420 | 360 | 60 | 14.29% | EXCEEDED (Flagged) |
| TC3 | Saturday | 300 | 250 | 50 | 16.67% | EXCEEDED (Flagged) |

## 9. Output Screenshots
*(Run `python code.py` in your terminal and attach the screenshot here before final GitHub submission.)*

## 10. Conclusion
The food waste monitoring system quantifies daily kitchen efficiency, pinpointing high-wastage days to support data-driven meal preparation adjustments.
