# Case Study 4: Employee Payroll and Deduction Analysis

## 1. Problem Statement
Calculate gross salary from basic pay, allowances, overtime, and incentives; apply progressive deductions and generate a formatted salary statement.

## 2. Objectives
- Compute gross earnings by aggregating basic salary, HRA, DA, overtime wages, and performance incentives.
- Apply progressive income tax slabs alongside standard Provident Fund (PF) deductions.
- Generate a clean, structured, and readable payslip statement.

## 3. Assumptions
- HRA is 20% of Basic Pay; DA is 10% of Basic Pay.
- Overtime is paid at ₹400 per hour.
- Provident Fund (PF) deduction is fixed at 12% of Basic Pay.
- Progressive Income Tax: 0% up to ₹30,000; 10% on amount between ₹30,001 and ₹60,000; 20% on amount above ₹60,000.

## 4. Algorithm
1. Start the program.
2. Read employee details: name, ID, basic pay, overtime hours, and incentives.
3. Calculate HRA (20% of basic) and DA (10% of basic).
4. Calculate overtime pay (overtime hours * 400).
5. Compute Gross Salary = Basic + HRA + DA + Overtime Pay + Incentives.
6. Calculate PF = 12% of Basic Pay.
7. Calculate Progressive Tax based on Gross Salary slabs.
8. Compute Total Deductions = PF + Tax, and Net Salary = Gross Salary - Total Deductions.
9. Print the formatted salary statement.
10. Stop the program.

## 5.Flowchart
╔══════════════════════════════════════════════════════════════╗
║                           [ START ]                          ║
╚══════════════════════════════╦═══════════════════════════════╝
                               ║
                               ▼
╔══════════════════════════════════════════════════════════════╗
║   / Input: Employee ID, Name, Basic, OT Hours, Incentives /  ║
╚══════════════════════════════╦═══════════════════════════════╝
                               ║
                               ▼
╔══════════════════════════════════════════════════════════════╗
║  [ HRA = Basic * 0.20 ]                                      ║
║  [ DA = Basic * 0.10 ]                                       ║
║  [ OT_Pay = OT_Hours * 400 ]                                 ║
║  [ Gross = Basic + HRA + DA + OT_Pay + Incentives ]          ║
║  [ PF = Basic * 0.12 ]                                       ║
╚══════════════════════════════╦═══════════════════════════════╝
                               ║
                               ▼
                   ┌───────────────────────┐
                   │   Is Gross <= ₹30k?   │
                   └─────┬───────────┬─────┘
                    Yes  │           │  No
        ┌────────────────┘           └────────────────┐
        ▼                                              ▼
╔═══════════════════════╗                  ┌───────────────────────┐
║      [ Tax = 0 ]      ║                  │   Is Gross <= ₹60k?   │
╚═══════════════╦═══════╝                  └─────┬───────────┬─────┘
                │                           Yes  │           │  No
                │               ┌────────────────┘           └────────────────┐
                │               ▼                                              ▼
                │   ╔═════════════════════════════════════╗      ╔═════════════════════════════════════════════════╗
                │   ║ [ Tax = (Gross - 30000) * 0.10 ]    ║      ║ [ Tax = (30000 * 0.10) + ((Gross - 60000) * 0.20) ] ║
                │   ╚══════════════════╦══════════════════╝      ╚════════════════════════╦════════════════════════╝
                │                      │                                          │
                └──────────────────────┼──────────────────────────────────────────┘
                                       ▼
╔══════════════════════════════════════════════════════════════╗
║  [ Total_Deductions = PF + Tax ]                             ║
║  [ Net_Salary = Gross - Total_Deductions ]                   ║
╚══════════════════════════════╦═══════════════════════════════╝
                               ║
                               ▼
╔══════════════════════════════════════════════════════════════╗
║          / Print Formatted Salary Statement (Payslip) /        ║
╚══════════════════════════════╦═══════════════════════════════╝
                               ║
                               ▼
╔══════════════════════════════════════════════════════════════╗
║                            [ END ]                           ║
╚══════════════════════════════════════════════════════════════╝

## 6. Pseudocode
```
BEGIN
    INPUT emp_id, name, basic, ot_hours, incentives
    hra = basic * 0.20
    da = basic * 0.10
    ot_pay = ot_hours * 400
    gross = basic + hra + da + ot_pay + incentives

    pf = basic * 0.12
    IF gross <= 30000 THEN
        tax = 0
    ELSE IF gross <= 60000 THEN
        tax = (gross - 30000) * 0.10
    ELSE
        tax = (30000 * 0.10) + ((gross - 60000) * 0.20)
    ENDIF

    total_deductions = pf + tax
    net_salary = gross - total_deductions
    PRINT formatted salary slip
END
```

## 7. Python Source Code
Refer to [`code.py`](./code.py) in this directory.

```python
# Case Study 4: Employee Payroll and Deduction Analysis

employees = [
    ("EMP01", "Aarav Sharma", 20000, 2, 1000),
    ("EMP02", "Priya Nair", 40000, 5, 3000),
    ("EMP03", "Rohan Verma", 55000, 10, 5000)
]

for emp_id, name, basic, ot_hours, incentives in employees:
    hra = basic * 0.20
    da = basic * 0.10
    ot_pay = ot_hours * 400.0
    gross_salary = basic + hra + da + ot_pay + incentives

    pf = basic * 0.12
    if gross_salary <= 30000:
        tax = 0.0
    elif gross_salary <= 60000:
        tax = (gross_salary - 30000) * 0.10
    else:
        tax = (30000 * 0.10) + ((gross_salary - 60000) * 0.20)

    total_deductions = pf + tax
    net_salary = gross_salary - total_deductions

    print("=" * 45)
    print(f"SALARY STATEMENT | ID: {emp_id} | Name: {name}")
    print("=" * 45)
    print(f"Basic Pay          : ₹{basic:10.2f}")
    print(f"HRA (20%)          : ₹{hra:10.2f}")
    print(f"DA (10%)           : ₹{da:10.2f}")
    print(f"Overtime Pay       : ₹{ot_pay:10.2f}")
    print(f"Incentives         : ₹{incentives:10.2f}")
    print("-" * 45)
    print(f"GROSS SALARY       : ₹{gross_salary:10.2f}")
    print("-" * 45)
    print(f"Provident Fund     : ₹{pf:10.2f}")
    print(f"Income Tax         : ₹{tax:10.2f}")
    print(f"TOTAL DEDUCTIONS   : ₹{total_deductions:10.2f}")
    print("=" * 45)
    print(f"NET SALARY PAYABLE : ₹{net_salary:10.2f}")
    print("=" * 45 + "\n")
```

## 8. Test Cases
| Test Case | Basic Pay | OT Hours | Incentives | Gross Salary | Total Deductions | Net Salary |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| TC1 (Low Bracket) | ₹20,000 | 2 | ₹1,000 | ₹27,800.00 | ₹2,400.00 (PF only) | ₹25,400.00 |
| TC2 (Mid Bracket) | ₹40,000 | 5 | ₹3,000 | ₹57,000.00 | ₹7,500.00 (PF+Tax) | ₹49,500.00 |
| TC3 (High Bracket) | ₹55,000 | 10 | ₹5,000 | ₹80,500.00 | ₹13,700.00 (PF+Tax) | ₹66,800.00 |

## 9. Output Screenshots
*(Run `python code.py` in your terminal and attach the screenshot here before final GitHub submission.)*

## 10. Conclusion
The payroll processing script automates complex allowance aggregations and multi-tier tax deductions, eliminating manual calculation errors and producing standardized employee salary statements.
