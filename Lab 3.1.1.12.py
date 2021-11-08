'''
Find Kind of year
Name: Raul Costa
Date: 8/11/2021
Version: 1.0
'''

# Ask the year to the user
year = int(input("Enter a year: "))

# Check if the year is before 1582
if year < 1582:
    print("Not within the Gregorian calendar period")
# Check if the year isn't divide by 4
elif year % 4 != 0 :
    print("Common Year")
# Check if the year isn't divide by 100
elif year % 100 != 100 :
    print("Leap Year")

# Check if the year isn't divide by 400
elif year % 400 != 400 :
    print("Common Year")

# Print if none of the above apply
else:
    print("Leap Year")
