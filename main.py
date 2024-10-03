employeeName = input("Employee's name: ")
shiftsWorked = int(input("Number of shifts: "))
numberOfTransactions = int(input("Number's of transactions: "))
transactionValue = float(input("Transaction dollar value: "))

productivityScore = (transactionValue / numberOfTransactions / shiftsWorked)

if productivityScore <= 30:
    bonus = 50.00
elif 31 <= productivityScore <= 69:
    bonus = 75.00
elif 70 <= productivityScore <= 199:
    bonus = 100.00
else:
    bonus = 200.00

print("Employee Name:", employeeName)
print("Bonus: $", bonus)