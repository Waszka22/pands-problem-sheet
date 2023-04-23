# Weelky Task 7 
# Author : Agnieszka Waszczuk 
# Write a program that reads in a text file and outputs the number of e's it contains
# $ python es.py moby-dick.txt
# Ref:https://www.w3schools.com/python/python_file_open.asp

# import sys 
import sys


filename = sys.argv[1]

with open(filename, 'r') as my_file:
    es = f.read()
    count = es.count("e")
    print (count)
