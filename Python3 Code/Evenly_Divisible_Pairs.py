# Hackerrank Question:

# Python 3

# You are given an array of 'n' integers, a0,a1...an-1, and a positive integer, k.
# Find and print the number of pairs where i<j and (ai + aj) is evenly divisible by k.

n,k = list(map(int,input().split()))         # map returns input numbers to list

a = list(map(int,input().split()))           # input array of numbers

total_pairs = 0

for x,c in enumerate(a):
    # c = x
    for y,d in enumerate(a):
        # d = y
        if (x < y and (c+d) % k == 0):
            total_pairs += 1

print(total_pairs)
