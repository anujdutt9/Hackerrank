# Solution to Hackerrank Problem at:
# https://www.hackerrank.com/challenges/utopian-tree

T = int(input())
h = 1

for _ in range(T):
    N = int(input())
    for i in range(1,N+1):
        if (N == 0):
           break
        if (i%2 != 0):
           h *= 2
        if (i %2 == 0):
            h += 1
    print(h)
    del(h)
    h = 1

