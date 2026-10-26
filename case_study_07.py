marks = [
    [80, 75, 90],
    [60, 70, 65],
    [95, 88, 92]
]

for index, student_marks in enumerate(marks, start=1):
    total = sum(student_marks)
    average = total / len(student_marks)
    print("Student", index, "marks:", student_marks)
    print("Total:", total, "Average:", round(average, 2))
