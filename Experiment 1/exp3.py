print("1 for celsius to fahrenheit")
print("2 for fahrenheit to celsius")
choice = int(input("Enter your choice"))
temp = float(input("Enter your tempertaure: "))
if choice == 1:
    print(f"Your Fahrenheit temperature is {(temp*9/5) + 32}")
elif choice == 2:
    print(f"Your Celsius temperature is {(temp-32)*5/9}")
else:
    print("Invalid input")