start1 = int(input("Class 1 start time (minutes after midnight): "))
end1 = int(input("Class 1 end time: "))
start2 = int(input("Class 2 start time: "))
end2 = int(input("Class 2 end time: "))

class1 = (start1, end1)
class2 = (start2, end2)

if class1[0] >= class1[1] or class2[0] >= class2[1]:
    print("Invalid time interval")
elif class1[0] < class2[1] and class2[0] < class1[1]:
    print("Timetable conflict")
else:
    print("No timetable conflict")
