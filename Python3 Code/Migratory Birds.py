# Migratory Birds Solution from RookieRank2 Challenge

#https://www.hackerrank.com/contests/rookierank-2/challenges/migratory-birds

#!/bin/python3

import sys


n = int(input().strip())
types = list(map(int, input().strip().split(' ')))

d = {'1':0 ,'2':0 ,'3':0 ,'4':0 ,'5':0}
for num in types:
    if num == 1:
        d['1'] += 1
    if num == 2:
        d['2'] += 1
    if num == 3:
        d['3'] += 1
    if num == 4:
        d['4'] += 1
    if num == 5:
        d['5'] += 1

print(d)
mxmum = max(d, key= d.get)
print(mxmum)
    
