opening = int(input("Opening stock: "))
received = int(input("Quantity received: "))
dispatched = int(input("Quantity dispatched: "))
physical = int(input("Physical closing stock: "))

if opening < 0 or received < 0 or dispatched < 0 or physical < 0:
    print("Invalid quantity")
else:
    expected = opening + received - dispatched
    difference = physical - expected
    print("Expected closing stock:", expected)

    if difference == 0:
        print("Stock matches")
    elif difference > 0:
        print("Surplus stock:", difference)
    else:
        print("Stock shortage:", abs(difference))
