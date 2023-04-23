
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

