'''
The best plant ever
Name: Raul Costa
Date: 1/11/2021
Version: 1.0
'''
# Ask the user to guess the best plan
plant=input("Type the best plant ever: ")

# Compare the user input
if plant == "Spathiphyllum":
    # Print if the user type the right plant
    print("Spathiphyllum is the best plant ever!")
elif plant == "spathiphyllum":
    # Print if the user miss capital letter
    print("No, I want a big Spathiphyllum!")
else:
    # Print if the wrong plant was typed
    print(f'Spathiphyllum! Not {plant}!!')
