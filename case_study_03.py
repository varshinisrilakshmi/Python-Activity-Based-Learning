marks = []

for subject in range(1, 4):
    mark = int(input("Enter marks for subject " + str(subject) + ": "))
    marks.append(mark)

valid = True
for mark in marks:
    if mark < 0 or mark > 100:
        valid = False

if not valid:
    print("Invalid marks")
else:
    total = sum(marks)
    average = total / 3
    if all(mark >= 35 for mark in marks):
        result = "PASS"
    else:
        result = "FAIL"

    print("Total:", total)
    print("Average:", round(average, 2))
    print("Result:", result)
