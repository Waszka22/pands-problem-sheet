# Week Task 4 
# Author: Agnieszka Waszczuk 
# At each step calculate the next value by taking the current value and, 
# if it is even, divide it by two, but if it is odd, multiply it by three and add one
# Program end if the current value is one.

your_number = input('Please give me a positive number: ')

# check if the number is positive number
while not your_number.isnumeric():
    print(f'your input is "{your_number}" but need to be positve number only')
    your_number = input('Please give me a positive number: ')

your_number = int(your_number)

print(f'your number is {your_number} and is positive')


# create empty list for the values
score = [your_number,]

while your_number !=1:
    if your_number%2 == 0:
        your_number = your_number/2
        score.append(int(your_number))
        #print(int(your_number))
    else:
        your_number = your_number*3+1
        #print(int(your_number))
        score.append(int(your_number))

#1 printing an int list in a single line
print(*score)

#2 printing an int list in a single line
for x in score:
    print(x, end=' ')

# Reference:
# https://www.youtube.com/watch?v=VuMqOd73ek8
# https://medium.com/the-art-of-python/the-collatz-sequence-in-python-eb7e1f1b4f9e
# https://stackoverflow.com/questions/61789065/automate-the-boring-stuff-with-python-collatz-sequence
# https://github.com/thomaskellough/Automate-The-Boring-Stuff/blob/master/Practice-Projects/Ch%2003%20-%20Collatz%20Sequence.py