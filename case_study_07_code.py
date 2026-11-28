# Case Study 7: Student Marks Matrix Analysis

students = ["Ananya", "Bikram", "Charan", "Divya"]
subjects = ["Math", "Physics", "Chemistry", "CS"]

# Rows = Students, Columns = Subjects
marks_matrix = [
    [88, 76, 92, 95],
    [65, 58, 62, 70],
    [91, 84, 89, 94],
    [72, 60, 68, 78]
]

print("--- Student-Wise Performance (Row Analysis) ---")
topper_name = ""
highest_total = -1

for i in range(len(students)):
    total = sum(marks_matrix[i])
    avg = total / len(subjects)
    print(f"{students[i]:<10} | Marks: {marks_matrix[i]} | Total: {total} | Avg: {avg:.2f}%")
    if total > highest_total:
        highest_total = total
        topper_name = students[i]

print(f"\nTop Performer: {topper_name} with {highest_total}/{len(subjects)*100} marks.")

print("\n--- Subject-Wise Performance (Column Analysis) ---")
for j in range(len(subjects)):
    col_total = 0
    for i in range(len(students)):
        col_total += marks_matrix[i][j]
    sub_avg = col_total / len(students)
    status = "FLAGGED: Low Average (<70%)" if sub_avg < 70.0 else "Satisfactory"
    print(f"{subjects[j]:<10} | Class Avg: {sub_avg:.2f}% | Status: {status}")
