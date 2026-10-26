stock_a = int(input("Branch A current stock: "))
target_a = int(input("Branch A target stock: "))
stock_b = int(input("Branch B current stock: "))
target_b = int(input("Branch B target stock: "))

if min(stock_a, target_a, stock_b, target_b) < 0:
    print("Invalid quantity")
else:
    surplus_a = max(0, stock_a - target_a)
    shortage_b = max(0, target_b - stock_b)
    transfer = min(surplus_a, shortage_b)

    stock_a -= transfer
    stock_b += transfer

    print("Units transferred from A to B:", transfer)
    print("Branch A stock after transfer:", stock_a)
    print("Branch B stock after transfer:", stock_b)
