import random

roll_again = "yes"
sum = 0

while roll_again.lower() == "yes":
  for i in range(1):  
    result = random.randint(1, 6)
    sum += result
    print(f"You rolled a {result}.")

  print(f"Total sum: {sum}")
  roll_again = input("Roll again? (yes/no): ")

