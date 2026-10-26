marks = float(input("Enter aggregate marks (%): "))
attendance = float(input("Enter attendance (%): "))
income = float(input("Enter annual family income (Rs): "))

if marks < 0 or marks > 100 or attendance < 0 or attendance > 100 or income < 0:
    print("Invalid input")
elif marks >= 80 and attendance >= 75 and income <= 250000:
    print("Eligible for scholarship")
else:
    print("Not eligible for scholarship")
