# Solution to Hackerrank Problem at Week of Code 31
# Advanced Sorting
# Passed all Cases, Code Accepted for all cases

import sys


def swap(a,x,y):
    temp = a[x]
    a[x] = a[y]
    a[y] = temp


q = int(input().strip())
for a0 in range(q):
    # n: length of array
    n = int(input().strip())
    # a: array
    a = list(map(int, input().strip().split(' ')))
    f = True	
    for i in range(0, n-1):
        if(a[i] > a[i+1]):
            swap(a, i, i+1)
            if (abs(a[i]-a[i+1]) == 1):
                pass
            else:
                f = False
    if(f == True):
        print('Yes')
    else:
        print('No')
