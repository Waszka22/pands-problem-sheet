# Weelky Task 7 
# Author : Agnieszka Waszczuk 
# Write a program that reads in a text file and outputs the number of e's it contains
# $ python es.py moby-dick.txt


# Open file name 
# We create FILENAME that contain text file called "moby-dick"

# import sys 
import sys
# use sys.argv[1], sys.argv[0] is the first argument
filename = sys.argv[1]

with open(filename, 'r') as f:
    es = f.read()
    count = es.count("e")
    print ("The count is:", count)
    

# Ref:
# https://www.w3schools.com/python/python_file_open.asp
# https://www.geeksforgeeks.org/how-to-use-sys-argv-in-python/
# https://www.knowledgehut.com/blog/programming/sys-argv-python-examples