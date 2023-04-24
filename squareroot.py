# Weekly task 6
# Author: Agnieszka Waszczuk
# Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.
# You should create a function called <tt>sqrt</tt> that does this.

request = 'y'

# the program will run everytime when you put 'y'
while request == 'y':

    user_number = input('Please give me a number: ')

    # check if the input is a positive number
    while not user_number.isdigit():
        user_number = input(f'You gave me {user_number} Please give me a positive number: ')

    # convert input from string type to float type
    user_number = float(user_number)

    # define a fucntion newtow method
    def newton_method(number):
        '''newton method return root square of the input'''

        first_site = user_number/2
        second_site = user_number/first_site
        count=0

        while round(first_site*first_site,8) != user_number:
            first_site = (first_site+second_site)/2
            second_site = user_number/first_site
            count+=1

        print(f'the root of {user_number} is {first_site}')
        print(f'Number of iterations to get root square: {count}')

    # run function newton_method
    newton_method(number=user_number)

    request = input('Do you want to check another number (Y/N)?').lower()

print('OVER')

    
# Ref: 
# https://www.codeleaks.io/python-square-root-function/
# https://www.w3schools.com/python/ref_string_isdigit.asp#:~:text=The%20isdigit()%20method%20returns,considered%20to%20be%20a%20digit.   
# https://www.youtube.com/watch?v=C_FFlau09_8 
# https://www.youtube.com/watch?v=yB4vZ87GioM
# https://www.youtube.com/watch?v=99ABkygm2Xg