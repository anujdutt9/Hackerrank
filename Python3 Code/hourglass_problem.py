# Given a 6x6 2D Array, A:

# 1 1 1 0 0 0
# 0 1 0 0 0 0
# 1 1 1 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0

# We define an hourglass in A to be a subset of values with indices falling in this pattern in A's graphical representation:

# a b c
#   d
# e f g

# There are 16 hourglasses in A, and an hourglass sum is the sum of an hourglass' values.
# Calculate the hourglass sum for every hourglass in , then print the maximum hourglass sum.


# Solution:

arr = []           # Define the array

# Input elements of Matrix and put it into array
for arr_i in range(6):
    arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
    arr.append(arr_t)

# Define an array for storing output
a = []

# Calculate the total for each hourglass
for i in range(0,4):
    for j in range(0, 4):
        total = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
        a.append(total)
    
# Print the Max value of total in the array 
print(max(a))


# Code to Print the Hourglass for which we have the Max value of Total from Array

##for i in range(0,4):
##    for j in range(0, 4):
##        total = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
##        if(total == max(a)):
##            print(str(arr[i][j]) + '' + str(arr[i][j+1]) + '' + str(arr[i][j+2]))
##            print(' '+ str(arr[i+1][j+1]))
##            print(str(arr[i+2][j]) + '' + str(arr[i+2][j+1]) + '' + str(arr[i+2][j+2]))
##            break

#---------------- EOC -----------------#
