# A left rotation operation on an array of size n shifts each of the array's elements 1 unit to the left. For example, 
# if 2 left rotations are performed on array[1,2,3,4,5] , then the array would become [3,4,5,1,2].
# Given an array of n integers and a number,d , perform d left rotations on the array. 
# Then print the updated array as a single line of space-separated integers.

# Solution:

n,d = input().strip().split(' ')

arr = []
for arr_temp in input().strip().split(' '):
    arr.append(arr_temp)

print(*(arr[int(d):] + arr[:int(d)]))

