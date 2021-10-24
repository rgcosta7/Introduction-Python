'''
Event end time calculator
Name: Raul Costa
Date: 18/10/2021
Version: 1.0
'''

# Ask user for starting time and duration
hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# Calculate the finishing time
mins = (mins + dura)
hour = hour + mins // 60

# Print the result
print(f'{hour}:{mins % 60}')
