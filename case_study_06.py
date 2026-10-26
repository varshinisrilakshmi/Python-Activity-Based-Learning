ids = input("Enter transaction IDs separated by spaces: ").split()
duplicates = []

for transaction_id in ids:
    if ids.count(transaction_id) > 1 and transaction_id not in duplicates:
        duplicates.append(transaction_id)

if len(duplicates) == 0:
    print("No duplicate transactions")
else:
    print("Duplicate transaction IDs:", duplicates)
