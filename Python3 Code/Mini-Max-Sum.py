# Mini-Max-Sum
# https://www.hackerrank.com/challenges/mini-max-sum


#!/bin/python3

import sys

arr = list(map(int, input().strip().split(' ')))

def minMaxSum(a):
    x = sum(a)
    print(x-max(a), x-min(a))

minMaxSum(arr)
