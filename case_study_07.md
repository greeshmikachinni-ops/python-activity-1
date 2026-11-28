# Case Study 7: Student Marks Matrix Analysis

## 1. Problem Statement
Analyse a matrix of student marks across subjects, calculate row-wise and column-wise statistics, identify top performers, and detect subjects with low average performance.

## 2. Objectives
- Represent multi-student, multi-subject marks using a 2D nested list.
- Compute row-wise totals and averages for each student and identify the class topper.
- Compute column-wise subject averages and flag subjects scoring below a defined threshold.

## 3. Assumptions
- Marks are out of 100 across 4 subjects: Math, Physics, Chemistry, and Computer Science.
- A subject with a class average below 70.0 is flagged for academic intervention.

## 4. Algorithm
1. Start the program.
2. Define student names list, subject names list, and 2D nested list `marks`.
3. Iterate row-by-row to compute each student's total and average marks; track the highest total to identify the top performer.
4. Iterate column-by-column (`j` from 0 to num_subjects - 1) and sum `marks[i][j]` across all students `i`.
5. Divide each column sum by the number of students to get subject averages.
6. Flag any subject whose average is below 70.0.
7. Print student-wise results, top performer, and subject-wise performance summary.
8. Stop the program.

## 5. Flowchart
```
[Start]
   |
   v
[Define Students, Subjects & 2D Marks Matrix]
   |
   v
[Loop Rows (Students): Compute Total, Avg & Track Max Total]
   |
   v
[Loop Columns (Subjects): Sum Marks Vertically & Compute Subject Avg]
   |
   v
[Check Each Subject Avg < 70.0?] --Yes--> [Flag Subject as Low Performing]
   |
   v
[Display Student Report, Topper & Subject Analysis]
   |
   v
[End]
```

## 6. Pseudocode
```
BEGIN
    SET students = ["Ananya", "Bikram", "Charan", "Divya"]
    SET subjects = ["Math", "Physics", "Chemistry", "CS"]
    SET marks = [[88, 76, 92, 95], [65, 58, 62, 70], [91, 84, 89, 94], [72, 60, 68, 78]]

    SET max_total = -1, topper = ""
    FOR i FROM 0 TO LENGTH(students) - 1 DO
        row_total = SUM(marks[i])
        row_avg = row_total / LENGTH(subjects)
        IF row_total > max_total THEN
            max_total = row_total
            topper = students[i]
        ENDIF
        PRINT students[i], row_total, row_avg
    ENDFOR

    FOR j FROM 0 TO LENGTH(subjects) - 1 DO
        col_sum = 0
        FOR i FROM 0 TO LENGTH(students) - 1 DO
            col_sum = col_sum + marks[i][j]
        ENDFOR
        sub_avg = col_sum / LENGTH(students)
        IF sub_avg < 70.0 THEN
            PRINT "Low Performance Alert:", subjects[j]
        ENDIF
    ENDFOR
END
```

## 7. Python Source Code
Refer to [`code.py`](./code.py) in this directory.

```python
# Case Study 42: Student Marks Matrix Analysis

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
```

## 8. Test Cases
| Test Case | Metric Evaluated | Input Matrix Subset | Expected Output |
| :--- | :--- | :--- | :--- |
| TC1 (Row Stats) | Charan's Total & Avg | `[91, 84, 89, 94]` | Total: 358, Avg: 89.50 (Top Performer) |
| TC2 (Col Stats) | Physics Average | `[76, 58, 84, 60]` | Avg: 69.50 (< 70.0 -> Flagged Low) |
| TC3 (Col Stats) | CS Average | `[95, 70, 94, 78]` | Avg: 84.25 (Satisfactory) |

## 9. Output Screenshots
*(Run `python code.py` in your terminal and attach the screenshot here before final GitHub submission.)*

## 10. Conclusion
Nested list traversal enables structured two-dimensional data analytics, simultaneously evaluating individual student standing and curriculum-level subject performance.
