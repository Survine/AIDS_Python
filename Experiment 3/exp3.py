import random
num = random.randrange(1,100)
print(num)
guess = int(input("Enter your guess from 1 to 100: "))
print(num)
if guess == num:
    print("Your guess was correct")
elif guess + 20 > num:
    print("Your guess was too high")
elif guess - 20 < num:
    print("Your guess was too low")
