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
Add the two amounts
Print out the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount. 
```

Craeta two variable for the input values and convert input from string to interger. Request enter amount1 and amount2. 
Function input() allows user input amount. 
Sum both amounts and divide them via 100 to get Euro Units.

The sytntax used: 

``` python
total =(amount1 + amount2)/ 100
```
 This task was helpful to understand all operators in Python 

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

For this task we import the math module. Created while loop() to prompt positive number. Using the sqrt() function to calculate a square root. The square returns float point value.

```python
result = math.sqrt(float(positive_number))
print(f'The square root of {positive_number} is : {result}')
```

Reference to understand we use [Youtube](https://www.youtube.com/watch?v=C_FFlau09_8), [Codeleaks](https://www.codeleaks.io/python-square-root-function/)

## Weekly Task 07 Argument 
```
Write a program that reads in a text file and outputs the number of e's it contains. Think about what is being asked here, document any assumptions you are making.
The program should take the filename from an argument on the command line. I have not shown you how to do this, you need to look it up.
```

We create FILENAME that contain text file called "moby-dick".
'r' means reading, opening the file called FILENAME with the purpose of reading. 
```python
with open(FILENAME, 'r') as f:
    for data in f:
        print (data)
```

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
