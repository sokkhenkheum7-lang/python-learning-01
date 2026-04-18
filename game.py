
# print("Welcome to the number guessing game!")
# coin = random.randint(0, 1)  # 0 = Front, 1 = Back
# if coin == 0:
#     print("Front side")
# else:
#     print("Back side")

# print("Good bye!") 
import random
user_num = int(input("Enter your number: "))
print("You entered:", user_num)

# Random number from 0 to 3
coin = random.randint(0, 3)

# Check if user wins
if coin in [0, 1, 2, 3]:  # You always win here
    print("You win")
else:
    print("You lose")

