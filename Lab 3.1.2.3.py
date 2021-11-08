'''
Guess the number
Name: Raul Costa
Date: 8/11/2021
Version: 1.0
'''
# Set the secre number!
secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

# Ask the user to guess the secret number
guess = int(input("Can you guess the number?\nFrom 0-1000 guess my number!! "))

# Compare the user number with the secret number and keep asking till the number is right
while guess != secret_number:
    print("Ha ha! You're stuck in my loop!!")
    guess = int(input("Pick again: "))

# Print statment if the user get the number right
print("Well done, muggle! You are free now.")
