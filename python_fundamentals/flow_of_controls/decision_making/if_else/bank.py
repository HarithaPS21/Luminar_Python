fixed_amount=10000
print("Your fixed amount is Rs.",fixed_amount)
amount=int(input("Enter the amount to be withdrawed "))
if amount>fixed_amount:
    print("Insufficient balance")
else:
    print("Your balance is Rs,",fixed_amount-amount)