# pands-problem-sheet

___
This repository is used for the weekly task given by the lecture Programming and scripting module on Higher Diploma in Data Analytics course at ATU.
___

## Table of content  :
 
* helloword
* accounts 
* bank
* collatz
* weekday 
* squareroot 
* arguments 
* plottask 
* weekday 
* squareroot 


## Weekly task 01 Helloword

Writing first code "Hello World" in Python.



## Wekly task 02 Bank

``` 
Write a program called bank.py The program should:
Prompt the user and read in two money amounts (in cent)
Print out the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount. 
```
Created two variables for the input values and convert the input from a string to an integer. The two amounts were added together and divided to obtain the Euro units.
The total with € sign in front of the number and 2 decimal places.
```python
print(f'The sum of these in € {total:.2f}')
```

 This task was helpful to understand all operators in Python. 

Reference for this weekly task  [Python Operators](https://www.w3schools.com/python/python_operators.asp) and YouTube





## Wekly task 03 Accounts

```
Bank account numbers can stored as 10 character strings, for security reasons some applications only display the last 4 characters (with the other other characters replaced with Xs).

Write a python program called accounts.py that reads in a 10 character account number and outputs the account number with only the last 4 digits showing (and the first 6 digits replaced with Xs).
```

 Website for this reserching we used [Output](https://realpython.com/python-input-output/) and  [While Loop ](https://www.w3schools.com/python/python_while_loops.asp) but also YouTube was helpfull. 

First, an input was created asking for a 10-digit account number. We use a while loop to check if the user has entered the correct number of digits.
 If no 10-digits request numbers have been entered, it will be prompted again to add correct amount of digits.

The sytntax used: 
  ```python
  while len (account_no) !=10:
    print(f'\nYou entered {len(account_no)} digits. You need to enter 10 digits') 
    print('Plase try again')
    account_no = input ('Plase enter an 10 digits account number: ')
  ```
 Used [-4] thta shows only the last 4 digits of the account

## Wekly task 04 Collatz

```
Write a program, called collatz.py, that asks the user to input any positive integer and outputs the successive values of the following calculation.
At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one.
```
We create 2 while loops. First statement is requesting to add positive value and second stamnet is calucating. 
At each step calculate the next value by taking the current value and,if it is even, divide it by two, but if it is odd, multiply it by three and add one program end if the current value is one.

The sytntax used: 
```python
while your_number !=1:
    if your_number%2 == 0:
        your_number = your_number/2
        score.append(your_number)
        #print(int(your_number))
    else:
        your_number = your_number*3+1
        #print(int(your_number))
        score.append(your_number)

        print([int(x) for x in score])
```

For this weekly task we used many soureces to understand problem [YouTube](https://www.youtube.com/watch?v=VuMqOd73ek8), [Medium](https://medium.com/the-art-of-python/the-collatz-sequence-in-python-eb7e1f1b4f9e), [Automate-The-Boring-Stuff](https://github.com/thomaskellough/Automate-The-Boring-Stuff/blob/master/Practice-Projects/Ch%2003%20-%20Collatz%20Sequence.py) and [Stack Overflow](https://stackoverflow.com/questions/61789065/automate-the-boring-stuff-with-python-collatz-sequence)

## Weekly Task 05 Weekday

```
Write a program that outputs whether or not today is a weekday. (The program should be called weekday.py)

```
 For this task we imported the time module:

```python 
import datetime

weekday = datetime.datetime.today().weekday()
```
The method weekday () returns the day of the week as an integer, where Monday is 0 and Sunday is 6.

Helpful pages for this task [PYnative](https://pynative.com/python-get-the-day-of-week/)




## Weekly Task 06 Square Root 

```
Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.
You should create a function called <tt>sqrt</tt> that does this.
Create your own sqrt function and not to use the built in functions x ** .5 or math.sqrt(x).
```
The program will run everytime when 'y' is added, with question : ''Do you want to check another number. 
The method isdigit() was used to returns True if all the characters are digits, or False if not. Also we used newton method return root square of the input.

Syntax: 
```python
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

```
This weekly task was difficult and requires a lot of time to research.
Reference to understand we use: [Youtube: Newton’s - Method In Python](https://www.youtube.com/watch?v=99ABkygm2Xg),  [Youtube: Newtona](https://www.youtube.com/watch?v=C_FFlau09_8), [Codeleaks](https://www.codeleaks.io/python-square-root-function/) and [3school](https://www.w3schools.com/python/ref_string_isdigit.asp#:~:text=The%20isdigit()%20method%20returns,considered%20to%20be%20a%20digit.).

## Weekly Task 07 Argument 
```
Write a program that reads in a text file and outputs the number of e's it contains. Think about what is being asked here, document any assumptions you are making.
The program should take the filename from an argument on the command line. I have not shown you how to do this, you need to look it up.
```

We create filename that contain text file called "moby-dick".
'r' means reading, opening the fille with the purpose of reading. 
Import modules sys and use sys.argv[1]

```python
with open(filename, 'r') as f:
    es = f.read()
    count = es.count("e")
    print ("The count is:", count)
```
Refrerence for task:
---
[w3school](https://www.w3schools.com/python/python_file_open.asp)
[Geeksforgreeks](https://www.geeksforgeeks.org/how-to-use-sys-argv-in-python/)
[Knoweledgehut](https://www.knowledgehut.com/blog/programming/sys-argv-python-examples) 


## Weekly Task 08 Plottask 

```
Write a program called plottask.py that displays:
a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2, and a plot of the function  h(x)=x3 in the range [0, 10], on the one set of axes.
```
For this exercise we impoted libraries numpy and matplotlib.pyplot. 
          

Create variables with data:

* nov = 1000 (number of values)
* sd = 2 (standard deviation - spread/width of the distribution)
* m = 5  (mean - center of the distribution)

Syntax we use for this task: 

```python 
data = np.random.normal(loc=m,scale=sd, size = nov)
```
Plot used linspace() method to create an array of spaced numbers (100)
within a specified range (0,10)

Reference for normal distribution we used [3school](https://www.w3schools.com/python/numpy/numpy_random_normal.aspand) and for plot [3school](https://www.w3schools.com/python/matplotlib_plotting.asp)



### Language 
* Python 
## Important Library 
* math 
* pandas 
* matplotlib. pyplot 
* numpy
* datetime
### Technologies 
* Visual Studio Code
* Cmder 