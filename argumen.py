# Weelky Task 7 
# Author : Agnieszka Waszczuk 
# Write a program that reads in a text file and outputs the number of e's it contains
# $ python es.py moby-dick.txt
# Ref:https://www.w3schools.com/python/python_file_open.asp



# Open file name 
# We create FILENAME that contain text file called "moby-dick"
FILENAME = "moby-dick.txt"

# 'r' means reading, opening the file called FILENAME with the purpose of reading 

with open(FILENAME, 'r') as f:
    for data in f:
        print (data)
    