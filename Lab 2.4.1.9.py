'''
Name: Raul Costa
Date: 04/10/2021
'''
pound = 0.74
euro = 0.86
amount = float(input("How many USD do you want convert to Pounds? "))
usd_eur = amount * euro
usd_pound = amount * pound
print(f'You can convert the {amount}USD into {usd_eur:.2f}EUR or to {usd_pound:.2f}GBP if you prefer!')
