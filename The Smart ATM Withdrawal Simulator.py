bank_balance = 800

withdraw_amount = float(input("How much do you want to withdraw?: "))
withdraw_balance = bank_balance - withdraw_amount

if withdraw_amount <= 800:
    print(f"Withdraw successful! Remainig balance: {withdraw_balance}")
elif withdraw_amount <= 0:
    print("Invalid amount")
else:
    print("Declined. Insufficient funds")