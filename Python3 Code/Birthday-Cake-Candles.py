# Birthday-Cake-Candles
# https://www.hackerrank.com/challenges/birthday-cake-candles?h_r=next-challenge&h_v=zen


#!/bin/python3

import sys
from collections import Counter

def birthdayCakeCandles(n, ar):
    d = Counter(ar)
    largest_key = max(Counter.keys(d))
    return d.get(largest_key)
    # Complete this function

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = birthdayCakeCandles(n, ar)
print(result)
