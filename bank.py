# Weekly Task 02
# Author: Agnieszka Waszczuk 
# Craeta two variable for the input values and convert input from string to interger
# Reference https://www.w3schools.com/python/python_operators.asp

# Create two variables for the input values and convert input from string to integer
amount1 = abs(int(input('Enter amount1(in cent)')))
amount2 = abs(int(input('Enter amount2(in cent)')))

# sum both amounts and convert numeric value to string
total = str(amount1 + amount2)

# use len() method to calculate position of decimal point
length = len(total)

if length >= 3:
    output = '€'+total[:length-2]+'.'+total[-2:]
elif length == 2:
   output = '€'+total[:length-2]+'0.'+total[-2:]
else:
    output = '€'+total[:length-2]+'0.0'+total[-2:]


# Print out the total with € sign in front of the number and 2 decimal places
print(f'The sum of these is {output}')
