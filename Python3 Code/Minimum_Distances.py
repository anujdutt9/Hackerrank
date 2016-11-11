# Solution to Hackerrrank Problem at:
# https://www.hackerrank.com/challenges/utopian-tree?h_r=next-challenge&h_v=zen

n = int(input().strip())
A = [int(A_temp) for A_temp in input().strip().split(' ')]

a = []
d = 0

for i in range(len(A)):
    for j in range(len(A)):
        if (A[i] == A[j] and i != j):
            d = abs(i-j)
            a.append(d)

if not a:
    print('-1')
else:
    print(min(a))
