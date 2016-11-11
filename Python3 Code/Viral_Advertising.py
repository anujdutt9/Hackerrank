# Solution to Hackerrank Question at:
# https://www.hackerrank.com/challenges/strange-advertising?h_r=next-challenge&h_v=zen


from math import floor

n = int(input())
a = 5
total = floor(a/2)

for _ in range(n-1):
    a = floor(a/2) * 3
    total += floor(a/2)

print(total)

