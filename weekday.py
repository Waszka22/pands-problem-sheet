# Weekly Tast 05 
# Authore Agnieszka Waszczuk 
# Write a program that outputs whether or not today is a weekday. (The program should be called weekday.py)
# An example of running this program on a Thursday is given below.
# An example of running it on a Saturday is as follows:
# Yes, unfortunately today is a weekday.
# It is the weekend, yay!


# import the time module
import datetime

weekday = datetime.datetime.today().weekday()

# use weekday from Monday to Friday (from 0 to 4)
if weekday < 5:
    print ('Yes, unfortunately today is a weekday.')
else:  # 5 Sat, 6 Sun
    print ('It is the weekend, yay!')

print (weekday)


# REF: https://pynative.com/python-get-the-day-of-week/