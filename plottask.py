# Weekly Task 8
# Author : Agnieszka Waszczuk
# Write a program called plottask.py that displays:
# a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2, 
# and a plot of the function  h(x)=x3 in the range [0, 10], 
# on the one set of axes.
# Some marks will be given for making the plot look nice (legend etc)
# ref https://www.w3schools.com/python/numpy/numpy_random_normal.asp
#     https://www.w3schools.com/python/matplotlib_plotting.asp


# import the numpy and matplotlib.pyplot
import numpy as np
import matplotlib.pyplot as plt

# 1. a histogram of a normal distribution of a 1000 values 
# with a mean of 5 and standard deviation of 2             

# create variables with data

nov = 1000 # number of values
sd = 2 # standard deviation - spread/width of the distribution
m = 5 # mean - center of the distribution

# use random.normal() method to create a list with data
# to draw random samples from a normal (Gaussian) distribution
data = np.random.normal(loc=m,scale=sd, size = nov)
  
# Plotting the histogram.
plt.hist(data, bins=25, density=True, alpha=0.6, color='b',label='Normal Distribution')

# add a title for plot
plt.title('Normal Distrubtion of a 1000 values with a mean of 5 and standard dev of 2')

# add labels to axises
plt.xlabel('x', color='#1C2833')
plt.ylabel('y', color='#1C2833')

# add legend to the plot
plt.legend(loc='upper left')

# add grid to the plot
plt.grid()

# display a plot  
plt.show()


# use linspace() method to create an array of spaced numbers (100)
# within a specified range (0,10)

x = np.linspace(start=0,stop=10,num=100)

# create a function h(x)=3x
y = 3*x

# Plot h(x) versus x as lines
plt.plot(x, y, 'r', label='h(x)=3x') # r = red

# add a title for plot
plt.title('Graph of h(x)=x3')

# add labels to axises
plt.xlabel('x', color='#1C2833')
plt.ylabel('h(x)', color='#1C2833')

# add legend to the plot
plt.legend(loc='upper left')

# add grid to the plot
plt.grid()

# display a plot  
plt.show()