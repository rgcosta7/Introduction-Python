'''
Tax Calculator
Name: Raul Costa
Date: 1/11/2021
Version: 1.0
'''
# Input the income
income = float(input("Enter the annual income: "))

# Compare the input if lower or highrer than 85528
if income <= 85528:
    # Calculate the tax at 18%
    tax = income * 0.18
    # Deduct tax relief
    tax = tax - 556.02
else:
    # Calculate the income surplus
    income = income - 85528
    # Calculate surplus tax at 32% and add the standart tax of 14839.02
    tax = 0.32 * income + 14839.02

# Check if the Tax is less than 0 and round it
if tax > 0:
    tax = round(tax, 0)
else:
    tax = 0.0

# Print the Tax value
print(f'The tax is: {tax} thalers')
