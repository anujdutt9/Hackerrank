# Solution to Hackerrank Problem at:
# https://www.hackerrank.com/challenges/beautiful-binary-string

#!/bin/python3
import sys

n = int(input().strip())
B = list(map(int, list(input().strip())))

count = 0

for i in range(2,n):
    if (B[i]==0 and B[i-1]==1 and B[i-2]==0):
        B[i]=1
        count += 1
print(count)
