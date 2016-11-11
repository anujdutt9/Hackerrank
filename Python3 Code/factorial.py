# Solution to Hackerrank Problem at:
# https://www.hackerrank.com/challenges/extra-long-factorials?h_r=next-challenge&h_v=zen

#!/bin/python3

import sys

def fact(num):
    prod = 1
    while num > 1:
        prod *= (num * (num-1))
        num = num - 2
    return prod


n = int(input().strip())
print(fact(n))

