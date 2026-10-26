attendance = float(input("Enter attendance (%): "))
average = float(input("Enter average marks (%): "))

if attendance < 0 or attendance > 100 or average < 0 or average > 100:
    print("Invalid input")
elif attendance < 60 or average < 40:
    print("High academic risk")
elif attendance < 75 or average < 60:
    print("Medium academic risk")
else:
    print("Low academic risk")
