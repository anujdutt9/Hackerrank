# Input "N": Size of Array
# Input elements of Array
# Print reversed Array

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
print(' '.join(str(i) for i in reversed(arr))) 

