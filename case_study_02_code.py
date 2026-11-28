# Case Study 2: Employee Payroll and Deduction Analysis

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
