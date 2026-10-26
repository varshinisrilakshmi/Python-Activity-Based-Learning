start1 = int(input("First shift start (minutes after midnight): "))
end1 = int(input("First shift end: "))
start2 = int(input("Second shift start: "))
end2 = int(input("Second shift end: "))

shift1 = (start1, end1)
shift2 = (start2, end2)

if shift1[0] >= shift1[1] or shift2[0] >= shift2[1]:
    print("Invalid shift")
elif shift1[0] < shift2[1] and shift2[0] < shift1[1]:
    print("Shift conflict")
else:
    print("No shift conflict")
