# Solution to Hackerrank Problem at:
# https://www.hackerrank.com/challenges/strange-code

#!/bin/python3
import sys

t = int(input())
total = 0
x = 3
while total < t:
    total += x
    print('total: ',total)
    x *= 2
x /= 2

print (int(total - x + (x-t)+1))
