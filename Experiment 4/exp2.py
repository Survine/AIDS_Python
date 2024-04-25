total_amount = float(input("Enter the total amount in your account: "))
withdraw_amount = float(input("Enter the amount you want to withdraw from your account: "))

if withdraw_amount <= total_amount:
    print(f"Rupees {withdraw_amount:.2f} have been withdrawn")
    choice = input("Do you want to check the remaining balance? (Enter 'Y' or 'N'): ")
    if choice.upper() == 'Y':
        remaining_balance = total_amount - withdraw_amount
        print(f"Remaining balance: {remaining_balance:.2f}")
    print("Thank you for using our services")
else:
    print("Transaction can't be processed due to insufficient funds in your account")